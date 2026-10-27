# 50 keyword pages (added 2026-10-27), batch 751-800.
# Places near 대포항 again; owner saw this exact keyword list in the thread and asked for it to be built.
# Store facts only from the listing / photos. Hours unconfirmed. Area facts kept general (no distances or minutes).
# Store facts only from the listing / photos. Hours unconfirmed (point to the phone). No invented reviews or prices.
from pages2 import add as _add, L, A

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

TEL = "0507-1364-4060"
WHERE = ("가게 위치는?","속초시 대포항길 10, 대포항 안쪽 상가 1층입니다.")
OFF = ("휴무일은?","매주 수요일입니다.")
TOGO = ("포장되나요?","네, 전 메뉴 포장됩니다.")
SIZE = ("사이즈는 어떻게 되나요?","찜은 소(2인), 중(3인), 대(4인)입니다.")
PARK = ("주차는?",A("daepohang-parking","주차 안내")+"를 참고하세요.")
KIDS = ("아이와 가도 되나요?","네, 아기 의자가 있고 맵지 않은 생선구이와 순대가 있습니다.")
HOURS = ("몇 시까지 하나요?",f"영업시간은 전화({TEL})로 확인해 주세요.")
SHOP = f"<p>대포항생선찜본점은 속초시 대포항길 10, 대포항 안쪽 상가 1층에 있습니다. 노란색과 분홍색 네온 간판을 찾으세요. 매주 수요일은 쉬고, 전 메뉴 포장됩니다. 전화 {TEL}.</p>"
MENU_ALL = L("가오리찜 (소·중·대)", "생선모듬찜 (소·중·대)", "대구뽈찜 (소·중·대)", "코다리찜 (소·중·대)", "모듬생선구이", "누룽지 오징어순대 17,000원", "속초 아바이순대", "소주, 맥주, 막걸리, 청하, 백세주 · 공깃밥, 음료수")
def j(w, a, b):
    return a if (ord(w[-1]) - 0xAC00) % 28 else b




GAORI = A('sokcho-gaori-jjim','가오리찜'); MODEUM = A('sokcho-saengseon-modeum-jjim','생선모듬찜'); GUI = A('sokcho-saengseon-gui','모듬생선구이')
SQUID = A('sokcho-nurungji-squid-sundae','누룽지 오징어순대'); KODARI = A('sokcho-kodari-jjim','코다리찜'); DAEGU = A('sokcho-daegu-ppol-jjim','대구뽈찜'); ABAI = A('sokcho-abai-sundae','아바이순대')

# place key: (name, intro, near slug, near keyword)
PL = {
 "oeongchi": ("외옹치", "외옹치는 대포항 바로 북쪽 항구 마을로, 바다향기로 산책길이 대포항까지 이어집니다.", "oeongchi-matjip", "외옹치 맛집"),
 "beach": ("속초해수욕장", "속초해수욕장은 속초에서 가장 붐비는 바다로, 남쪽으로 내려오면 대포항입니다.", "sokcho-beach-matjip", "속초해수욕장 근처 맛집"),
 "daepodong": ("대포동", "대포동은 대포항이 있는 동네라 숙소에서 걸어서 항구까지 나올 수 있습니다.", "daepodong-matjip", "대포동 맛집"),
 "mulchi": ("물치", "물치는 속초와 맞닿은 양양 북쪽 바닷가 마을로, 대포항이 가장 가까운 속초 항구입니다.", "mulchihang-matjip", "물치항 근처 맛집"),
 "lotte": ("롯데리조트", "롯데리조트 속초는 외옹치 바닷가 리조트로, 남쪽으로 조금만 오면 대포항입니다.", "sokcho-lotte-resort-matjip", "속초 롯데리조트 근처 맛집"),
 "cassia": ("카시아 속초", "카시아 속초에 묵는다면 숙소 밖 항구 식당에서 바다 도시다운 한 끼를 드셔 보세요.", "cassia-sokcho-matjip", "카시아 속초 근처 맛집"),
 "maremons": ("마레몬스", "마레몬스 호텔에서 바다를 따라 남쪽으로 오면 대포항에 닿습니다.", "maremons-matjip", "마레몬스 근처 맛집"),
 "sorano": ("쏘라노", "설악 쏘라노는 설악산 아래 리조트로, 바다 쪽으로 나오면 대포항이 있습니다.", "sorano-matjip", "설악 쏘라노 근처 맛집"),
 "jeongam": ("정암해변", "정암해변은 물치 북쪽의 조용한 해변으로, 속초 쪽으로 조금 올라오면 대포항입니다.", "jeongam-matjip", "정암해변 근처 맛집"),
 "haemaji": ("설악해맞이공원", "설악해맞이공원은 바닷가 산책로가 있는 공원으로, 대포항과 가깝습니다.", "seorak-haemaji-matjip", "설악해맞이공원 맛집"),
 "cheoksan": ("척산온천", "척산온천에서 온천욕을 한 뒤 바다 쪽으로 나오면 대포항에서 식사할 수 있습니다.", "cheoksan-oncheon-matjip", "척산온천 근처 맛집"),
 "waterpia": ("설악워터피아", "설악워터피아에서 물놀이를 하고 나면 바다 쪽 대포항으로 나와 식사하기 좋습니다.", "seorak-waterpia-matjip", "설악워터피아 근처 맛집"),
 "cheongchoho": ("청초호", "청초호는 속초 시내 가운데 호수로, 둘레길 산책 뒤 남쪽 대포항으로 내려오면 됩니다.", "cheongchoho-matjip", "청초호 근처 맛집"),
 "cheongdaesan": ("청대산", "청대산은 속초 시내에서 가볍게 오르는 낮은 산으로, 정상에서 바다와 설악산이 보입니다.", "cheongdaesan-matjip", "청대산 맛집"),
 "ic": ("속초IC", "서울양양고속도로 속초IC로 나오면 바다 쪽 대포항으로 가기 편합니다.", "sokcho-ic-matjip", "속초IC 근처 맛집"),
 "joyangdong": ("조양동", "조양동은 속초 남쪽 주거 동네로, 대포항까지 나와 외식하기 좋습니다.", "joyangdong-matjip", "조양동 맛집"),
 "expo": ("엑스포공원", "엑스포공원과 엑스포타워를 둘러본 뒤 남쪽 대포항으로 이동해 식사하기 좋습니다.", "sokcho-expo-matjip", "속초 엑스포공원 맛집"),
 "domundong": ("도문동", "도문동은 상도문 돌담마을이 있는 설악산 쪽 조용한 동네입니다.", "domundong-matjip", "속초 도문동 맛집"),
 "haksapyeong": ("학사평", "학사평은 순두부 마을로 알려진 곳입니다. 다른 끼니에는 바다 쪽으로 나와 보세요.", "haksapyeong-matjip", "학사평 근처 맛집"),
}
# dish: (name, link, img, text, more slug, more kw)
DI = {
 "kodari": ("코다리찜", KODARI, "jjim-closeup.jpg", "꾸덕하게 말린 명태를 매콤달콤한 양념에 쪄 내 쫄깃하고 밥반찬으로 좋습니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.", "kodari-jjim-matjip", "코다리찜 맛집"),
 "daegu": ("대구뽈찜", DAEGU, "jjim-closeup.jpg", "대구 머리의 쫀득한 볼살을 뜨끈하게 쪄 냅니다. 찬바람 부는 날 특히 잘 어울립니다.", "daegu-ppol-matjip", "대구뽈찜 맛집"),
 "abai": ("아바이순대", ABAI, "abai-sundae.jpg", "실향민의 손맛에서 시작된 속초 아바이순대입니다. 찜에 곁들이거나 포장해 가기 좋습니다.", "abai-sundae-matjip", "아바이순대 맛집"),
 "modeum": ("생선모듬찜", MODEUM, "jjim-table.jpg", "여러 생선을 한 냄비에 담아 매콤하게 쪄 냅니다. 무엇을 먹을지 고르기 어려울 때 좋습니다.", "fish-jjim-matjip", "생선찜 맛집"),
 "squid": ("오징어순대", SQUID, "squid-sundae.jpg", "팬에 지져 겉을 누룽지처럼 바삭하게 만든 누룽지 오징어순대입니다. 17,000원입니다(바뀔 수 있습니다).", "squid-sundae-matjip", "오징어순대 맛집"),
 "gui": ("생선구이", GUI, "gui.jpg", "그날 들어온 여러 생선을 노릇하게 구워 한 판에 냅니다. 맵지 않아 아이와 어르신도 편합니다.", "fish-gui-matjip", "생선구이 맛집"),
 "gaori": ("가오리찜", GAORI, "gaori-jjim.jpg", "이 집 대표 메뉴입니다. 쫀득한 살과 오독한 연골, 삭히지 않아 냄새가 없습니다.", "gaori-jjim-matjip", "가오리찜 맛집"),
}
MEAL = {
 "점심": ("gui.jpg", f"점심에는 맵지 않은 {GUI}나 {GAORI} 소(2인)가 부담 없습니다. 오후 일정이 있다면 {SQUID}로 가볍게 드셔도 좋습니다."),
 "저녁": ("jjim-table.jpg", f"저녁에는 대표 메뉴 {GAORI}이나 여러 생선을 담은 {MODEUM}을 추천합니다. 소주, 맥주, 막걸리도 있습니다."),
}

def page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    add(slug, kw, cat, img, lede, [(h1, f"<p>{p1}</p>"), (h2, f"<p>{p2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))], faq)

def place_dish(pk, dk):
    n, intro, ns, nk = PL[pk]; d, link, img, text, ms, mk = DI[dk]
    page(f"{pk}-{dk}-v2" if False else f"{pk}-{dk}", f"{n} {d}", "근처", img, f"{n} 근처에서 {d}{j(d,'을','를')} 찾는다면, 대포항으로.",
         f"{n}에서", intro, d, f"대포항생선찜본점의 {link}{j(d,'은','는')} {text}",
         [A(ns, nk), A(ms, mk)], [WHERE, TOGO if dk in ('abai','squid','gui') else SIZE])

def place_meal(pk, meal):
    n, intro, ns, nk = PL[pk]; img, text = MEAL[meal]
    page(f"{pk}-{'lunch' if meal=='점심' else 'dinner'}", f"{n} {meal}", "근처", img, f"{n}에서 {meal} 먹을 곳, 대포항.",
         f"{n}에서", intro, f"{meal} 메뉴", text,
         [A(ns, nk), A("daepohang-lunch" if meal=="점심" else "daepohang-dinner", "대포항 점심" if meal=="점심" else "대포항 저녁")],
         [WHERE, PARK] if meal=="점심" else [SIZE, HOURS])

def place_takeout(pk):
    n, intro, ns, nk = PL[pk]
    page(f"{pk}-takeout", f"{n} 포장 맛집", "근처", "jjim-table.jpg", f"{n} 숙소에서 먹을 저녁, 대포항에서 포장.",
         f"{n}에서", intro, "포장", f"전 메뉴 포장됩니다. 미리 전화({TEL})로 주문하고 시간 맞춰 찾으러 오세요. 데우는 법은 {A('saengseon-jjim-reheat','생선찜 포장 데우는 법')}을 참고하세요.",
         [A(ns, nk), A("sokcho-takeout-matjip","속초 포장 맛집")], [TOGO, HOURS])

# ---------- 외옹치·속초해수욕장 ----------
for dk in ("kodari","daegu","abai","modeum"): place_dish("oeongchi", dk)
for dk in ("kodari","daegu","abai"): place_dish("beach", dk)
# ---------- 대포동·물치 ----------
place_dish("daepodong","kodari"); place_dish("daepodong","squid"); place_takeout("daepodong")
page("daepodong-family", "대포동 가족 식사", "근처", "hall3.jpg", "대포동에 묵는 가족, 식사는 걸어서 대포항.",
 "대포동에서", PL["daepodong"][1], "가족 주문", f"넷이라면 {GAORI} 대(4인)에 아이 몫으로 맵지 않은 {GUI}를 더하세요. 아기의자가 있고 홀이 넓습니다.",
 [A("daepodong-matjip","대포동 맛집"), A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])
place_dish("mulchi","squid"); place_takeout("mulchi"); place_dish("mulchi","kodari"); place_dish("mulchi","daegu")
# ---------- 근처 숙소 ----------
place_dish("lotte","kodari"); place_dish("lotte","daegu")
place_meal("cassia","점심"); place_dish("cassia","squid")
place_meal("maremons","점심"); place_dish("maremons","squid")
page("maremons-kids", "마레몬스 아이랑 식사", "근처", "hall3.jpg", "마레몬스에 아이와 묵는다면, 식사는 대포항.",
 "마레몬스에서", PL["maremons"][1], "아이 메뉴", f"맵지 않은 {GUI}와 {SQUID}가 아이 몫으로 좋습니다. 아기의자도 있습니다.",
 [A("maremons-matjip","마레몬스 근처 맛집"), A("sokcho-kids-matjip","속초 아이랑 맛집")], [KIDS, PARK])
place_dish("sorano","gui"); place_dish("sorano","gaori"); place_meal("sorano","저녁"); place_meal("sorano","점심")
# ---------- 근처 명소 ----------
place_meal("jeongam","저녁"); place_dish("jeongam","gaori")
place_meal("haemaji","저녁"); place_dish("haemaji","gaori")
place_meal("cheoksan","점심"); place_dish("cheoksan","gaori")
place_meal("waterpia","점심"); place_dish("waterpia","gaori")
place_meal("cheongchoho","점심"); place_dish("cheongdaesan","gui")
# ---------- 동네·길목 ----------
place_dish("ic","gaori"); place_meal("ic","저녁")
place_dish("joyangdong","gaori"); place_meal("joyangdong","점심"); place_meal("joyangdong","저녁")
place_meal("expo","점심"); place_meal("expo","저녁")
place_dish("domundong","gui"); place_dish("haksapyeong","gui")
page("oeongchi-daepohang-walk", "외옹치 대포항 산책 코스", "근처", "storefront.jpg", "외옹치에서 대포항까지 바닷길 걷기.",
 "걷는 길", "외옹치항에서 바다향기로를 따라 걸으면 바다 바로 옆으로 난 길을 지나 대포항까지 이어집니다. 바람이 센 날에는 겉옷을 챙기세요.",
 "도착하면 한 끼", f"대포항에 도착하면 항구 안쪽 상가 1층에서 {GAORI}이나 {GUI}로 식사하세요. 돌아갈 때는 포장해 가셔도 됩니다.",
 [A("badahyanggiro-after-walk","바다향기로 산책 후 식사"), A("daepohang-walk","대포항 산책")], [WHERE, TOGO])
# ---------- 대포항 점심 ----------
for dk, slug in (("daegu","daepohang-daegu-lunch"),("modeum","daepohang-modeum-lunch"),("abai","daepohang-abai-lunch"),("squid","daepohang-squid-lunch")):
    d, link, img, text, ms, mk = DI[dk]
    page(slug, f"대포항 {d} 점심", "대포항", img, f"대포항에서 점심으로 먹는 {d}.",
         "대포항 점심", "대포항을 오전에 둘러보면 점심때가 됩니다. 항구 안쪽 상가 1층에서 바로 식사하실 수 있습니다.",
         d, f"{link}{j(d,'은','는')} {text}", [A("daepohang-lunch","대포항 점심"), A(ms, mk)], [WHERE, PARK])

assert len(P) == 50, len(P)
