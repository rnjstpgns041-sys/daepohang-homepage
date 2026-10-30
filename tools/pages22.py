# 50 keyword pages (added 2026-10-30), batch 951-1000.
# Owner asked for places not too far from 대포항, so every keyword is 대포항 근처 / 대포동 / 외옹치·물치 side /
# south Sokcho lodgings, spas and sights x a menu not built for that place yet.
# Store facts only from the listing / photos. No invented reviews or prices. Area facts kept general.
from pages2 import add as _add, L, A
from pages18 import WHERE, TOGO, SIZE, SHOP, j
from pages20 import DI
from pages21 import PL as PL21

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

PL = {**PL21,
 "daepohang-nearby": ("대포항 근처", "대포항에 왔다면 멀리 갈 것 없이 항구 안쪽 상가 1층으로 오세요. 튀김골목과 회센터 구경을 마치고 걸어서 닿는 곳에 있습니다.", "daepohang-nearby-matjip", "대포항 근처 맛집"),
}

def page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    add(slug, kw, cat, img, lede, [(h1, f"<p>{p1}</p>"), (h2, f"<p>{p2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))], faq)

def pd(pk, dk, slug=None):
    n, intro, ns, nk = PL[pk]; d, link, img, text, ms, mk = DI[dk]
    near = n if n.endswith("근처") else f"{n} 근처"
    page(slug or f"{pk}-{dk}", f"{n} {d}", "근처", img, (f"대포항 근처 {d}, 항구 안쪽 상가 1층 대포항생선찜본점." if n.endswith("근처") else f"{near}에서 {d}{j(d,'을','를')} 찾는다면, 대포항으로."),
         f"{n}에서" if not n.endswith("근처") else "대포항 안에서", intro, d, f"대포항생선찜본점의 {link}{j(d,'은','는')} {text}",
         [A(ns, nk), A(ms, mk)], [WHERE, TOGO if dk in ('abai','squid','gui') else SIZE])

# right at the harbour
for dk in ("jjim","gaori","kodari","daegu","squid","abai"): pd("daepohang-nearby", dk)
pd("daepodong","daegu"); pd("daepodong","abai")
# 외옹치·속초해수욕장·물치 side and the lodgings there
pd("beach","modeum"); pd("mulchi","abai"); pd("mulchi","modeum")
pd("lotte","abai","lotte-abai"); pd("cassia","abai"); pd("maremons","abai")
pd("sorano","kodari"); pd("sorano","daegu"); pd("sorano","squid")
pd("jeongam","kodari"); pd("jeongam","squid")
pd("haemaji","daegu"); pd("haemaji","squid")
# south Sokcho spas, water park, lake, neighbourhoods
pd("cheoksan","daegu"); pd("cheoksan","squid"); pd("waterpia","daegu")
pd("cheongchoho","daegu"); pd("cheongchoho","abai")
pd("joyangdong","kodari"); pd("joyangdong","daegu"); pd("joyangdong","squid")
pd("expo","kodari"); pd("expo","daegu")
pd("domundong","gaori"); pd("domundong","kodari"); pd("haksapyeong","gaori"); pd("haksapyeong","kodari")
pd("ic","kodari"); pd("ic","squid")
pd("ipark","kodari"); pd("ipark","squid"); pd("ramada","daegu"); pd("ramada","squid")
pd("sokcho-eye","kodari"); pd("sokcho-eye","daegu"); pd("chilseong","gui"); pd("chilseong","gaori")
pd("abai","daegu","abai-village-daegu"); pd("jungang-market","kodari")
pd("hanwha","daegu"); pd("kensington","squid"); pd("terminal","squid")

assert len(P) == 50, len(P)
