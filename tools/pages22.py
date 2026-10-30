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
pd("beach","modeum"); pd("mulchi","abai"); pd("mulchi","modeum")
pd("cheoksan","daegu"); pd("cheongchoho","daegu"); pd("cheongchoho","abai")
pd("sokcho-eye","kodari"); pd("sokcho-eye","daegu")
pd("abai","daegu","abai-village-daegu"); pd("jungang-market","kodari"); pd("hanwha","daegu")

# 2026-10-30 rework: owner asked for keywords more people search, so 31 low-volume place combos above
# were swapped for 속초 대포항 + menu, 대포항 + menu 맛집, 대포항 + situation 맛집 and nearby-place 맛집 추천.
DPH = "대포항은 속초 남쪽 끝 항구로, 튀김골목과 회센터가 모여 있는 곳입니다. 대포항생선찜본점은 그 안쪽 상가 1층에서 생선찜과 생선구이를 냅니다."
MAT = A("daepohang-matjip","대포항 맛집")
DPAGE = {"jjim":"daepohang-saengseon-jjim","gaori":"daepohang-gaori-jjim","gui":"daepohang-saengseon-gui","kodari":"daepohang-kodari-jjim",
         "daegu":"daepohang-daegu-ppol-jjim","squid":"daepohang-ojingeo-sundae","abai":"daepohang-abai-sundae"}

page("sokcho-daepohang-matjip", "속초 대포항 맛집", "대포항", "jjim-table.jpg", "속초 대포항에서 회 말고 든든한 한 끼, 생선찜과 생선구이.",
     "속초 대포항", DPH, "무엇을 먹나요", f"대표 메뉴는 {DI['gaori'][1]}이고, 여러 생선을 담은 {DI['modeum'][1]}, 맵지 않은 {DI['gui'][1]}, {DI['squid'][1]}가 있습니다. 찜은 소(2인), 중(3인), 대(4인)로 고릅니다.",
     [MAT, A("daepohang-nearby-matjip","대포항 근처 맛집")], [WHERE, SIZE])
def sd(dk):
    d, link, img, text, ms, mk = DI[dk]
    page(f"sokcho-daepohang-{dk}", f"속초 대포항 {d}", "대포항", img, f"속초 대포항에서 {d}{j(d,'을','를')} 먹는다면.",
         "속초 대포항", DPH, d, f"대포항생선찜본점의 {link}{j(d,'은','는')} {text}",
         [A(DPAGE[dk], f"대포항 {d}"), A(ms, mk)], [WHERE, TOGO if dk in ('squid','gui') else SIZE])
for dk in ("jjim","gaori","gui","kodari","squid"): sd(dk)

def dm(dk):
    d, link, img, text, ms, mk = DI[dk]
    page(f"daepohang-{'saengseon-jjim' if dk=='jjim' else dk}-matjip", f"대포항 {d} 맛집", "대포항", img, f"대포항 {d} 맛집을 찾는다면, 항구 안쪽 대포항생선찜본점.",
         f"대포항에서 {d}", f"대포항에는 회센터와 튀김집이 많지만 {d}{j(d,'을','를')} 제대로 내는 집은 많지 않습니다. 대포항생선찜본점은 찜과 구이, 순대를 전문으로 합니다.",
         "이 집의 " + d, f"{link}{j(d,'은','는')} {text}",
         [A(DPAGE[dk], f"대포항 {d}"), MAT], [WHERE, TOGO if dk in ('abai','squid','gui') else SIZE])
for dk in ("jjim","gaori","gui","kodari","daegu","squid","abai"): dm(dk)

GAORI, GUI, MODEUM, SQUID = DI['gaori'][1], DI['gui'][1], DI['modeum'][1], DI['squid'][1]
PET = ("반려동물 동반 되나요?","네, 반려동물과 함께 오실 수 있습니다.")
KIDS = ("아이와 가도 되나요?","네, 아기 의자가 있고 맵지 않은 생선구이와 순대가 있습니다.")
PARK = ("주차는?","가게 앞 주차장은 따로 없고 대포항 공영주차장을 이용하시면 됩니다.")
def sit(slug, kw, img, lede, h1, p1, h2, p2, more, faq):
    page(slug, kw, "대포항", img, lede, h1, p1, h2, p2, more + [MAT], faq)
sit("daepohang-lunch-matjip","대포항 점심 맛집","gui.jpg","대포항 점심, 맵지 않은 생선구이부터 가오리찜까지.",
    "대포항 점심", "오전에 바다를 보고 대포항에 들렀다면 점심은 항구 안에서 해결하세요. 매일 10시에 문을 엽니다(수요일 휴무).",
    "점심 추천", f"가볍게는 {GUI}나 {SQUID}, 둘이서 든든하게는 {GAORI} 소(2인)가 좋습니다.", [A("daepohang-lunch","대포항 점심")], [WHERE, ("휴무일은?","매주 수요일입니다.")])
sit("daepohang-dinner-matjip","대포항 저녁 맛집","jjim-table.jpg","대포항 저녁, 찜 한 냄비에 소주 한 잔.",
    "대포항 저녁", "해가 지면 대포항 불빛이 켜집니다. 저녁은 21시까지라 너무 늦지 않게 오세요.",
    "저녁 추천", f"저녁엔 {GAORI}이나 {MODEUM}을 가운데 두고 나눠 드세요. 소주, 맥주, 막걸리, 청하, 백세주가 있습니다.", [A("daepohang-dinner","대포항 저녁")], [SIZE, WHERE])
sit("daepohang-family-matjip","대포항 가족 맛집","hall3.jpg","대포항 가족 식사, 넓은 홀과 아기 의자.",
    "가족과 대포항", "가족 여행으로 대포항에 왔다면 아이와 어른이 함께 먹을 메뉴가 필요합니다. 홀이 넓고 아기 의자가 있습니다.",
    "가족 주문", f"넷이라면 {GAORI} 대(4인)에 아이 몫으로 맵지 않은 {GUI}를 더하세요.", [A("daepohang-family-dining","대포항 가족 식사")], [KIDS, SIZE])
sit("daepohang-kids-matjip","대포항 아이랑 맛집","gui.jpg","아이랑 대포항, 맵지 않은 메뉴가 있는 집.",
    "아이와 대포항", "아이와 함께라면 매운 찜만 있는 집은 곤란합니다. 이 집은 맵지 않은 생선구이와 순대가 있고 아기 의자도 있습니다.",
    "아이 메뉴", f"아이는 {GUI}와 {SQUID}를, 어른은 {GAORI}을 드시면 모두 편합니다.", [A("daepohang-with-kids","대포항 아이랑")], [KIDS, WHERE])
sit("daepohang-pet-matjip","대포항 애견동반 맛집","pet.jpg","반려견과 대포항, 함께 들어갈 수 있는 식당.",
    "반려견과 대포항", "대포항 산책을 반려견과 했다면 식사도 같이 하고 싶을 겁니다. 대포항생선찜본점은 반려동물 동반이 됩니다.",
    "메뉴", f"대표 메뉴 {GAORI}, {MODEUM}, {GUI}가 있습니다. 전 메뉴 포장도 됩니다.", [A("daepohang-pet-friendly","대포항 애견동반")], [PET, TOGO])
sit("daepohang-parking-matjip","대포항 주차 맛집","storefront.jpg","대포항에 차 세우고 걸어가는 생선찜집.",
    "차를 가져온다면", "가게 앞 전용 주차장은 없고, 대포항 공영주차장에 세우고 걸어오시면 됩니다.",
    "도착해서", f"노란색과 분홍색 네온 간판을 찾으세요. 대표 메뉴는 {GAORI}입니다.", [A("daepohang-parking","대포항 주차")], [PARK, WHERE])
sit("daepohang-group-matjip","대포항 단체 맛집","hall.jpg","대포항 단체 식사, 넓은 홀에서 찜 여러 냄비.",
    "여럿이 대포항", "모임이나 단체 여행이라면 넓은 홀이 있는 집이 편합니다. 인원이 많으면 미리 전화로 자리를 물어보세요.",
    "단체 주문", f"4명마다 {GAORI}이나 {MODEUM} 대(4인) 하나씩, 가운데 {GUI}를 더하면 좋습니다.", [A("daepohang-group-dining","대포항 단체 식사")], [SIZE, ("단체 예약 되나요?","전화(0507-1364-4060)로 문의해 주세요.")])
sit("daepohang-parents-matjip","대포항 부모님 맛집","jjim-closeup.jpg","부모님 모시고 대포항, 뜨끈한 생선찜 한 상.",
    "부모님과 대포항", "회가 부담스러운 부모님께는 따뜻한 찜이 좋습니다. 밥반찬이 되는 양념이라 어르신들이 좋아하십니다.",
    "추천", f"{DI['kodari'][1]}이나 {DI['daegu'][1]}, 맵지 않은 {GUI}를 함께 시키세요.", [A("daepohang-parents","대포항 부모님 식사")], [SIZE, WHERE])
sit("daepohang-fish-matjip","대포항 생선 맛집","gui.jpg","대포항 생선 요리, 찜과 구이 둘 다.",
    "대포항 생선 요리", "대포항에서 생선을 회가 아닌 요리로 먹고 싶다면 찜과 구이를 함께 하는 집을 찾으세요.",
    "메뉴", f"찜은 {GAORI}, {MODEUM}, {DI['kodari'][1]}, {DI['daegu'][1]}, 구이는 {GUI}입니다.", [A("daepohang-saengseon-gui","대포항 생선구이")], [SIZE, TOGO])
sit("daepohang-hansik-matjip","대포항 한식 맛집","jjim-table.jpg","대포항 한식, 밥이 당기는 생선찜.",
    "대포항 한식", "여행 중 밥과 반찬이 그리울 때, 매콤한 생선찜 양념에 공깃밥 한 그릇이 제일입니다.",
    "메뉴", f"{GAORI}이나 {DI['kodari'][1]}에 공깃밥을 곁들이고, 남은 양념에 밥을 비벼 드세요.", [A("daepohang-hansik","대포항 한식")], [SIZE, WHERE])
sit("daepohang-bapjip-recommend","대포항 밥집 추천","jjim-closeup.jpg","대포항 밥집, 회센터 말고 찜집.",
    "대포항 밥집", "대포항은 회센터와 튀김이 많아 밥 먹을 곳을 찾기 어렵다는 분이 많습니다. 항구 안쪽 상가 1층에 찜과 구이 밥집이 있습니다.",
    "추천 메뉴", f"둘이면 {GAORI} 소(2인), 셋이면 중(3인)에 {SQUID}를 더해 보세요.", [A("daepohang-bapjip","대포항 밥집")], [SIZE, WHERE])
sit("daepohang-around-matjip","대포항 주변 맛집","storefront.jpg","대포항 주변에서 식사할 곳, 항구 안 생선찜집.",
    "대포항 주변", "외옹치, 속초해수욕장, 물치가 모두 대포항 주변입니다. 어디서 출발하든 대포항 안쪽 상가 1층으로 오시면 됩니다.",
    "메뉴", f"대표 메뉴 {GAORI}, 여러 생선을 담은 {MODEUM}, 맵지 않은 {GUI}가 있습니다.", [A("daepohang-nearby-matjip","대포항 근처 맛집")], [WHERE, TOGO])

def rec(pk, slug, kw):
    n, intro, ns, nk = PL[pk]
    page(slug, kw, "근처", "jjim-table.jpg", f"{n} 맛집 추천, 가까운 대포항 생선찜.",
         f"{n}에서", intro, "추천 메뉴", f"처음이라면 대표 메뉴 {GAORI}을, 매운 걸 못 드시면 {GUI}를 추천합니다. 둘이면 소(2인), 넷이면 대(4인)입니다.",
         [A(ns, nk), MAT], [WHERE, SIZE])
rec("oeongchi","oeongchi-recommend","외옹치 맛집 추천"); rec("beach","sokcho-beach-recommend","속초해수욕장 맛집 추천")
rec("mulchi","mulchihang-recommend","물치항 맛집 추천"); rec("lotte","lotte-resort-recommend","롯데리조트 속초 맛집 추천")
rec("cassia","cassia-recommend","카시아 속초 맛집 추천"); rec("maremons","maremons-recommend","마레몬스 맛집 추천")

assert len(P) == 50, len(P)
