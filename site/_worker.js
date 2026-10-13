// 사장님 전용 통계: 방문·버튼 기록(/api/t)과 요약(/api/stats). 나머지 요청은 정적 파일로 넘깁니다.
// 광고 장부(/api/ledger)도 같은 비밀번호로 열립니다.
// D1 바인딩 이름 DB, 비밀번호 비밀값 STATS_KEY 가 필요합니다.
async function ensure(db) {
  await db.prepare(`CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts INTEGER NOT NULL, day TEXT NOT NULL, type TEXT NOT NULL,
    path TEXT, landing TEXT, src TEXT, q TEXT, dev TEXT)`).run();
  await db.prepare("CREATE INDEX IF NOT EXISTS events_day ON events(day)").run();
}

const TYPES = new Set(["view", "call", "map", "menu", "copy_phone", "copy_addr"]);
const cut = (v, n) => (typeof v === "string" ? v.slice(0, n) : "");

async function track(request, env) {
  if (!env.DB) return new Response(null, { status: 204 });
  let b;
  try { b = JSON.parse(await request.text()); } catch { return new Response(null, { status: 400 }); }
  if (!TYPES.has(b.t)) return new Response(null, { status: 400 });
  const ua = request.headers.get("user-agent") || "";
  if (/bot|crawl|spider|yeti|daum|preview/i.test(ua)) return new Response(null, { status: 204 });
  const dev = /mobi|android|iphone/i.test(ua) ? "모바일" : "PC";
  const now = Date.now();
  const day = new Date(now + 9 * 3600e3).toISOString().slice(0, 10); // 한국 날짜
  await ensure(env.DB);
  await env.DB.prepare("INSERT INTO events (ts,day,type,path,landing,src,q,dev) VALUES (?,?,?,?,?,?,?,?)")
    .bind(now, day, b.t, cut(b.p, 200), cut(b.l, 200), cut(b.s, 40), cut(b.q, 100), dev).run();
  return new Response(null, { status: 204 });
}

const json = (o, status = 200) => new Response(JSON.stringify(o), {
  status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

async function stats(request, env) {
  if (!env.DB || !env.STATS_KEY) return json({ error: "setup" }, 503);
  if (request.headers.get("x-stats-key") !== env.STATS_KEY) return json({ error: "key" }, 401);
  const days = Math.min(Math.max(parseInt(new URL(request.url).searchParams.get("days") || "30", 10) || 30, 1), 3650);
  const from = new Date(Date.now() + 9 * 3600e3 - (days - 1) * 864e5).toISOString().slice(0, 10);
  await ensure(env.DB);
  const q = (sql) => env.DB.prepare(sql).bind(from).all().then((r) => r.results);
  const sum = `SUM(type='view') v, SUM(type='call') c, SUM(type='map') m, SUM(type='copy_phone') cp`;
  const [total, daily, pages, sources, queries, devices] = await Promise.all([
    q(`SELECT ${sum} FROM events WHERE day>=?`),
    q(`SELECT day, ${sum} FROM events WHERE day>=? GROUP BY day ORDER BY day`),
    q(`SELECT landing, ${sum} FROM events WHERE day>=? AND landing<>'' GROUP BY landing ORDER BY v DESC, c DESC LIMIT 200`),
    q(`SELECT src, ${sum} FROM events WHERE day>=? GROUP BY src ORDER BY v DESC`),
    q(`SELECT q, src, COUNT(*) v FROM events WHERE day>=? AND type='view' AND q<>'' GROUP BY q, src ORDER BY v DESC LIMIT 100`),
    q(`SELECT dev, ${sum} FROM events WHERE day>=? GROUP BY dev`),
  ]);
  return json({ from, days, total: total[0], daily, pages, sources, queries, devices });
}

async function ensureLedger(db) {
  await db.prepare(`CREATE TABLE IF NOT EXISTS ledger (
    id INTEGER PRIMARY KEY AUTOINCREMENT, created_at INTEGER NOT NULL,
    kind TEXT NOT NULL DEFAULT 'guest', day TEXT NOT NULL,
    channel TEXT, keyword TEXT, menu TEXT, people INTEGER DEFAULT 0, status TEXT,
    revenue INTEGER DEFAULT 0, cost INTEGER DEFAULT 0, amount INTEGER DEFAULT 0, memo TEXT)`).run();
}

const int = (v) => Math.max(0, Math.min(parseInt(String(v ?? "").replace(/[^0-9]/g, ""), 10) || 0, 1e12));

async function ledger(request, env) {
  if (!env.DB || !env.STATS_KEY) return json({ error: "setup" }, 503);
  if (request.headers.get("x-stats-key") !== env.STATS_KEY) return json({ error: "key" }, 401);
  await ensureLedger(env.DB);
  const db = env.DB;
  if (request.method === "GET") {
    await ensure(db);
    const [rows, calls] = await Promise.all([
      db.prepare("SELECT * FROM ledger ORDER BY day DESC, id DESC").all().then((r) => r.results),
      db.prepare("SELECT day, SUM(type='call') c, SUM(type='view') v FROM events GROUP BY day").all().then((r) => r.results),
    ]);
    return json({ rows, calls });
  }
  if (request.method === "DELETE") {
    const id = int(new URL(request.url).searchParams.get("id"));
    await db.prepare("DELETE FROM ledger WHERE id=?").bind(id).run();
    return json({ ok: true });
  }
  let b;
  try { b = JSON.parse(await request.text()); } catch { return json({ error: "bad" }, 400); }
  const kind = b.kind === "spend" ? "spend" : "guest";
  const today = new Date(Date.now() + 9 * 3600e3).toISOString().slice(0, 10);
  const day = /^\d{4}-\d{2}-\d{2}$/.test(b.day || "") ? b.day : today;
  const v = [kind, day, cut(b.channel, 40), cut(b.keyword, 60), cut(b.menu, 120), int(b.people), cut(b.status, 10),
    int(b.revenue), int(b.cost), int(b.amount), cut(b.memo, 300)];
  const id = int(b.id);
  if (id) {
    await db.prepare("UPDATE ledger SET kind=?,day=?,channel=?,keyword=?,menu=?,people=?,status=?,revenue=?,cost=?,amount=?,memo=? WHERE id=?")
      .bind(...v, id).run();
    return json({ id });
  }
  const r = await db.prepare("INSERT INTO ledger (created_at,kind,day,channel,keyword,menu,people,status,revenue,cost,amount,memo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
    .bind(Date.now(), ...v).run();
  return json({ id: r.meta.last_row_id });
}

export default {
  async fetch(request, env) {
    const { pathname } = new URL(request.url);
    if (pathname === "/api/t" && request.method === "POST") return track(request, env);
    if (pathname === "/api/stats" && request.method === "GET") return stats(request, env);
    if (pathname === "/api/ledger" && ["GET", "POST", "DELETE"].includes(request.method)) return ledger(request, env);
    return env.ASSETS.fetch(request);
  },
};
