// Owner-only summary. Requires header x-stats-key equal to the STATS_KEY secret.
// Shared D1 setup for the visit/call tracker. Needs a D1 binding named DB.
async function ensure(db) {
  await db.prepare(`CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts INTEGER NOT NULL, day TEXT NOT NULL, type TEXT NOT NULL,
    path TEXT, landing TEXT, src TEXT, q TEXT, dev TEXT)`).run();
  await db.prepare("CREATE INDEX IF NOT EXISTS events_day ON events(day)").run();
}

const json = (o, status = 200) => new Response(JSON.stringify(o), {
  status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

export async function onRequestGet({ request, env }) {
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
