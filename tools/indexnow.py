# Send changed page URLs to IndexNow (Naver + the shared IndexNow endpoint, which passes them to Bing and others).
# Usage: python3 tools/indexnow.py URL [URL ...]   (or URLs on stdin, one per line)
import json, sys, urllib.request

HOST = "daepohang-fish.pages.dev"
KEY = "3cf415cdd028560ad0479ba3fa85047c"
ENDPOINTS = ["https://searchadvisor.naver.com/indexnow", "https://api.indexnow.org/indexnow"]

urls = sys.argv[1:] or [l.strip() for l in sys.stdin if l.strip()]
urls = sorted({u for u in urls if u.startswith(f"https://{HOST}/") and "/stats/" not in u})
if not urls:
    print("nothing to send"); sys.exit(0)
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
failed = False
for ep in ENDPOINTS:
    req = urllib.request.Request(ep, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(ep, r.status, len(urls), "urls")
    except urllib.error.HTTPError as e:
        print(ep, e.code, e.read()[:200]); failed = failed or e.code not in (200, 202)
    except Exception as e:
        print(ep, "error", e); failed = True
sys.exit(1 if failed else 0)
