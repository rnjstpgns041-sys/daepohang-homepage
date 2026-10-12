// Records one page view or button tap. Body: {t, p, l, s, q}. No cookies, no IP stored.
// Shared D1 setup for the visit/call tracker. Needs a D1 binding named DB.
async function ensure(db) {
  await db.prepare(`CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts INTEGER NOT NULL, day TEXT NOT NULL, type TEXT NOT NULL,
    path TEXT, landing TEXT, src TEXT, q TEXT, dev TEXT)`).run();
  await db.prepare("CREATE INDEX IF NOT EXISTS events_day ON events(day)").run();
}

const TYPES = new Set(["view", "call", "map", "menu", "copy_phone", "copy_addr"]);
const cut = (v, n) => (typeof v === "string" ? v.slice(0, n) : "");

export async function onRequestPost({ request, env }) {
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
