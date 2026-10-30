# 50 keyword pages (added 2026-10-30), batch 901-950.
# The 2026-10-29 Naver check showed "place + menu" ranks best, so this batch fills place x menu combos
# not built yet (busy Sokcho markets, sights and lodgings x 오징어순대/아바이순대/코다리찜/대구뽈찜/가오리찜 etc).
# Store facts only from the listing / photos. No invented reviews or prices. Area facts kept general.
from pages2 import add as _add, L, A
from pages18 import WHERE, TOGO, SIZE, SHOP, j, PL as PL18
from pages20 import DI, PL as PL20

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

PL = {**PL18, **PL20,
 "tourist-market": ("속초관광수산시장", "속초관광수산시장은 닭강정, 오징어순대, 건어물 가게가 모인 속초 대표 시장입니다. 시장 구경 뒤 앉아서 먹는 한 끼는 대포항에서 드셔 보세요.", "sokcho-tourist-market-matjip", "속초관광수산시장 근처 맛집"),
 "yeongnangho": ("영랑호", "영랑호는 속초 북쪽의 큰 호수로, 둘레길과 영랑호수윗길 산책으로 유명합니다. 산책을 마치고 남쪽 대포항으로 내려오면 식사할 수 있습니다.", "yeongnangho-matjip", "영랑호 근처 맛집"),
 "yeongnangho-resort": ("영랑호리조트", "영랑호리조트는 영랑호 바로 옆 리조트입니다. 시내를 지나 남쪽 끝 대포항까지 나와 항구 식사를 해 보세요.", "yeongrangho-resort-matjip", "영랑호리조트 근처 맛집"),
 "ipark": ("아이파크 스위트 속초", "아이파크 스위트 속초는 바다가 보이는 숙소입니다. 숙소에서 대포항까지 나와 생선 요리로 한 끼 드셔 보세요.", "ipark-sokcho-matjip", "아이파크 스위트 속초 근처 맛집"),
 "jangsa": ("장사항", "장사항은 속초 북쪽 끝의 작은 항구입니다. 북쪽 항구를 구경했다면 남쪽 끝 항구 대포항에서 식사로 이어 가 보세요.", "jangsahang-matjip", "장사항 맛집"),
 "chilseong": ("칠성조선소", "칠성조선소는 옛 배 만들던 곳을 카페와 전시 공간으로 바꾼 청초호 옆 명소입니다. 커피 한 잔 뒤 식사는 대포항에서 하세요.", "chilseong-shipyard-matjip", "칠성조선소 근처 맛집"),
 "seorakdong": ("설악동", "설악동은 설악산 소공원으로 들어가는 길목 동네입니다. 산에서 나와 바다 쪽으로 오면 대포항이 있습니다.", "seorakdong-matjip", "설악동 맛집"),
 "intercity": ("속초 시외버스터미널", "시외버스로 속초에 도착했다면 시내를 지나 대포항까지 와서 첫 끼를 드세요.", "sokcho-intercity-terminal-matjip", "속초 시외버스터미널 근처 맛집"),
}

def page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    add(slug, kw, cat, img, lede, [(h1, f"<p>{p1}</p>"), (h2, f"<p>{p2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))], faq)

def pd(pk, dk, slug=None):
    n, intro, ns, nk = PL[pk]; d, link, img, text, ms, mk = DI[dk]
    page(slug or f"{pk}-{dk}", f"{n} {d}", "근처", img, f"{n} 근처에서 {d}{j(d,'을','를')} 찾는다면, 대포항으로.",
         f"{n}에서", intro, d, f"대포항생선찜본점의 {link}{j(d,'은','는')} {text}",
         [A(ns, nk), A(ms, mk)], [WHERE, TOGO if dk in ('abai','squid','gui') else SIZE])

# markets: 오징어순대 / 아바이순대 are what people look for there
pd("jungang-market","squid"); pd("jungang-market","abai")
pd("tourist-market","squid"); pd("tourist-market","abai");
pd("abai","abai","abai-village-abai-sundae"); pd("abai","kodari","abai-village-kodari")
pd("yeonggeumjeong","squid"); pd("dongmyeong","squid"); pd("dongmyeong","kodari")
# Seoraksan side
pd("sogongwon","gaori"); pd("cablecar","jjim"); pd("cablecar","gui"); pd("cablecar","gaori")
pd("ulsanbawi","gui"); pd("gwongeumseong","jjim"); pd("sinheungsa","jjim"); pd("biseondae","gui")
pd("seorakdong","gui"); pd("seorakdong","gaori")
# sea and lakes
pd("sokcho-eye","gui"); pd("sokcho-eye","gaori"); pd("sokcho-eye","squid")
pd("cheongchoho","squid"); pd("cheongchoho","kodari")
pd("yeongnangho","gaori"); pd("yeongnangho","squid")
pd("expo","squid"); pd("jangsa","gaori"); pd("lighthouse","gaori"); pd("chilseong","jjim")
pd("haemaji","kodari"); pd("jeongam","jjim")
# lodgings
pd("hanwha","kodari"); pd("hanwha","squid"); pd("cassia","kodari"); pd("cassia","daegu")
pd("maremons","kodari"); pd("maremons","daegu"); pd("kensington","kodari"); pd("delpino","kodari")
pd("ramada","kodari"); pd("ipark","gaori"); pd("yeongnangho-resort","jjim"); pd("yeongnangho-resort","gui")
# spas / water park / roads
pd("cheoksan","kodari"); pd("waterpia","kodari"); pd("waterpia","squid")
pd("terminal","gaori"); pd("intercity","gaori"); pd("ic","gui")

assert len(P) == 50, len(P)
