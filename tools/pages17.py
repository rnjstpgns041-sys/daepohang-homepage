# 50 keyword pages (added 2026-10-26), batch 701-750.
# Owner asked for places near 대포항 and approved this exact keyword list in the thread first.
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



def pg(slug, kw, cat, img, lede, s1h, s1, s2h, s2, more, faq):
    add(slug, kw, cat, img, lede,
     [(s1h, f"<p>{s1}</p>"), (s2h, f"<p>{s2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))],
     faq)

GAORI = A('sokcho-gaori-jjim','가오리찜'); MODEUM = A('sokcho-saengseon-modeum-jjim','생선모듬찜'); GUI = A('sokcho-saengseon-gui','모듬생선구이')
SQUID = A('sokcho-nurungji-squid-sundae','누룽지 오징어순대'); KODARI = A('sokcho-kodari-jjim','코다리찜'); ABAI = A('sokcho-abai-sundae','아바이순대')

# ---------- 대포항 안·바로 옆 ----------
pg("daepohang-twigim-alley", "대포항 튀김골목", "대포항", "storefront.jpg", "튀김골목 구경하고, 식사는 항구 안쪽 생선찜.",
 "대포항 튀김골목", "대포항 하면 새우튀김을 비롯한 튀김 가게들이 줄지어 있는 골목이 먼저 떠오릅니다. 손에 들고 먹으며 항구를 구경하는 재미가 있습니다.",
 "튀김 다음엔 든든한 한 끼", f"튀김은 간식으로 두고, 식사는 같은 대포항 안쪽 상가 1층에서 {GAORI}이나 {GUI}로 드셔 보세요.",
 [A("daepohang-twigim","대포항 튀김 먹고 식사"), A("daepohang-meokgeori","대포항 먹거리")], [WHERE, PARK])
pg("daepohang-hoecenter-restaurant", "대포항 회센터 근처 식당", "대포항", "storefront.jpg", "회센터 옆에서 회 말고 익힌 생선 요리를.",
 "회센터 근처에서", "대포항 회센터 주변에는 횟집이 많습니다. 일행 중 회를 못 먹는 사람이 있거나 따뜻한 음식이 당길 때는 고르기가 어렵습니다.",
 "익힌 생선 요리", f"대포항생선찜본점은 같은 대포항 안쪽에 있는 생선찜, 생선구이 전문점입니다. 회는 하지 않습니다. {MODEUM}과 {GUI}를 추천합니다.",
 [A("daepohang-hoetjip","대포항 횟집"), A("daepohang-not-hoe","대포항 회 말고 먹을거")], [("회도 파나요?","아니요. 생선찜, 생선구이, 순대 전문점입니다."), WHERE])
pg("daepohang-breakwater", "대포항 방파제 산책", "대포항", "storefront.jpg", "방파제 따라 바다 보고, 돌아와서 생선찜.",
 "방파제 산책", "대포항 방파제 쪽으로 걸으면 정박한 고깃배와 탁 트인 동해를 함께 볼 수 있습니다. 바람이 세게 부는 날에는 겉옷을 챙기세요.",
 "산책 후 식사", f"산책을 마치고 항구 안쪽으로 돌아오면 바로 식사할 수 있습니다. 바람에 언 몸은 뜨끈한 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}으로 녹이세요.",
 [A("daepohang-walk","대포항 산책"), A("daepohang-fishing-boats","대포항 고깃배 구경")], [WHERE, SIZE])
pg("daepohang-suljip", "대포항 술집", "대포항", "squid-sundae.jpg", "대포항에서 술 한잔, 안주는 생선찜과 오징어순대.",
 "항구에서 한잔", "대포항의 저녁은 불빛이 켜진 항구를 보며 한잔하기 좋습니다. 소주, 맥주, 막걸리, 청하, 백세주가 있습니다.",
 "안주로 좋은 메뉴", f"양념이 진한 {KODARI}과 바삭한 {SQUID}가 안주로 인기입니다. 매운 안주가 싫다면 {GUI}를 고르세요.",
 [A("daepohang-anju","대포항 술안주"), A("jjim-sulanju","생선찜 술안주"), A("sokcho-suljip","속초 술집")], [HOURS, TOGO])
pg("daepohang-late-lunch", "대포항 늦은 점심", "대포항", "jjim-table.jpg", "점심때를 놓쳤다면, 대포항에서 늦은 점심.",
 "늦은 점심", "오전 일정이 길어져 점심때를 놓쳤다면 대포항에서 늦은 점심을 드셔 보세요. 붐비는 시간을 피해 여유롭게 식사할 수 있습니다.",
 "가볍게 또는 든든하게", f"가볍게는 {SQUID}, 든든하게는 {GAORI} 소(2인)를 추천합니다. 쉬는 시간이 있을 수 있으니 전화({TEL})로 확인해 주세요.",
 [A("sokcho-late-lunch","속초 늦은 점심"), A("daepohang-lunch","대포항 점심")], [HOURS, OFF])
pg("oeongchihang-matjip", "외옹치항 맛집", "근처", "storefront.jpg", "외옹치항 바로 아래, 대포항 생선찜.",
 "외옹치항", "외옹치항은 대포항 바로 북쪽의 작은 항구입니다. 바다향기로 산책길이 이어져 있어 걸어서 대포항까지 오가는 분들이 많습니다.",
 "추천 메뉴", f"대표 메뉴 {GAORI}, 여러 생선을 함께 담은 {MODEUM}, 맵지 않은 {GUI}가 있습니다.",
 [A("oeongchi-matjip","외옹치 맛집"), A("sokcho-badahyanggiro-matjip","바다향기로 맛집")], [WHERE, PARK])
pg("sangdomun-matjip", "상도문 돌담마을 맛집", "근처", "storefront.jpg", "돌담마을 산책 뒤, 바다 쪽 대포항에서 한 끼.",
 "상도문 돌담마을", "상도문 돌담마을은 속초 도문동에 있는 옛 돌담길 마을입니다. 조용히 걸으며 사진 찍기 좋은 곳입니다.",
 "마을 구경 후 식사", f"마을을 둘러본 뒤 바다 쪽으로 나와 대포항에서 식사하세요. 어르신과 함께라면 맵지 않은 {GUI}를 곁들이세요.",
 [A("domundong-matjip","속초 도문동 맛집"), A("domundong-saengseon-jjim","도문동 생선찜")], [WHERE, PARK])
pg("sorano-matjip", "설악 쏘라노 근처 맛집", "근처", "storefront.jpg", "쏘라노에 묵는 날, 저녁은 바다 쪽 대포항.",
 "쏘라노에서", "설악 쏘라노는 설악산 아래 리조트 단지에 있습니다. 산 쪽 숙소에 묵더라도 저녁 한 끼는 바다 쪽 항구에서 드셔 보세요.",
 "추천 메뉴", f"{GAORI}과 {MODEUM}은 여럿이 나눠 먹기 좋고, 남으면 포장해 숙소로 가져가셔도 됩니다.",
 [A("hanwha-seorak-matjip","한화리조트 설악 맛집"), A("sorano-saengseon-jjim","쏘라노 생선찜")], [WHERE, TOGO])
pg("sorano-saengseon-jjim", "쏘라노 생선찜", "근처", "jjim-table.jpg", "쏘라노 근처에서 생선찜을 찾는다면, 대포항으로.",
 "쏘라노에서", "설악 쏘라노에서 설악산을 다녀온 날, 매콤한 생선찜으로 하루를 마무리해 보세요.",
 "생선찜", f"{MODEUM}은 여러 생선을 매콤한 양념에 쪄 냅니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.",
 [A("sorano-matjip","설악 쏘라노 근처 맛집"), A("fish-jjim-matjip","생선찜 맛집")], [SIZE, TOGO])

# ---------- 외옹치·바다향기로 ----------
pg("oeongchi-squid-sundae", "외옹치 오징어순대", "근처", "squid-sundae.jpg", "외옹치 근처에서 오징어순대를 찾는다면.",
 "외옹치에서", "외옹치 산책 뒤 가볍게 먹을 속초 별미를 찾는다면 오징어순대가 좋습니다.",
 "누룽지 오징어순대", f"{SQUID}는 팬에 지져 겉을 누룽지처럼 바삭하게 만듭니다. 17,000원입니다(바뀔 수 있습니다).",
 [A("oeongchi-matjip","외옹치 맛집"), A("squid-sundae-matjip","오징어순대 맛집")], [TOGO, WHERE])
pg("oeongchi-family", "외옹치 가족 식사", "근처", "hall3.jpg", "외옹치 여행 중 가족 식사, 대포항에서.",
 "가족과 외옹치", "외옹치와 바다향기로는 아이와 어르신도 걷기 편한 바닷길입니다. 걷고 나면 온 가족이 함께 먹을 메뉴가 필요합니다.",
 "가족 주문", f"넷이라면 {GAORI} 대(4인)에 아이 몫으로 맵지 않은 {GUI}를 더하세요. 아기의자도 있습니다.",
 [A("oeongchi-matjip","외옹치 맛집"), A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])
pg("oeongchi-takeout", "외옹치 포장 맛집", "근처", "jjim-table.jpg", "외옹치 숙소에서 먹을 생선찜, 포장해 가세요.",
 "숙소에서 저녁", "외옹치 쪽 숙소에 묵으며 바다를 보며 저녁을 먹고 싶다면 포장이 편합니다.",
 "포장 메뉴", f"전 메뉴 포장됩니다. 미리 전화({TEL})로 주문하고 찾으러 오세요. {A('saengseon-jjim-reheat','생선찜 포장 데우는 법')}도 참고하세요.",
 [A("sokcho-takeout-matjip","속초 포장 맛집"), A("daepohang-takeout","대포항 포장")], [TOGO, HOURS])
pg("badahyanggiro-lunch", "바다향기로 점심", "근처", "gui.jpg", "바다향기로 걷고 나서 점심.",
 "오전 산책 뒤", "바다향기로는 외옹치 해안을 따라 난 산책길입니다. 오전에 걷고 나면 점심때가 됩니다.",
 "점심 메뉴", f"점심에는 맵지 않은 {GUI}나 {SQUID}가 부담 없습니다.",
 [A("sokcho-badahyanggiro-matjip","바다향기로 맛집"), A("oeongchi-lunch","외옹치 점심")], [WHERE, PARK])
pg("badahyanggiro-dinner", "바다향기로 저녁", "근처", "gaori-jjim.jpg", "해 질 녘 바다향기로, 저녁은 대포항.",
 "해 질 녘 산책", "해가 질 무렵 바다향기로는 바다 색이 바뀌는 모습을 보기 좋습니다. 산책을 마치면 저녁 먹을 곳을 찾게 됩니다.",
 "저녁 메뉴", f"저녁에는 대표 메뉴 {GAORI}을 추천합니다. 술 한잔 곁들이셔도 좋습니다.",
 [A("sokcho-badahyanggiro-matjip","바다향기로 맛집"), A("oeongchi-dinner","외옹치 저녁")], [SIZE, HOURS])
pg("badahyanggiro-after-walk", "바다향기로 산책 후 식사", "근처", "jjim-closeup.jpg", "바다향기로 한 바퀴, 그다음은 따뜻한 한 끼.",
 "산책 코스", "바다향기로는 바다 바로 옆을 걷는 길이라 바람이 찰 때가 많습니다. 걷고 나면 따뜻한 음식이 당깁니다.",
 "따뜻한 찜", f"뜨끈한 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이나 {KODARI}으로 몸을 녹이세요.",
 [A("sokcho-badahyanggiro-matjip","바다향기로 맛집"), A("sokcho-walking-course","속초 걷기 좋은 길")], [WHERE, SIZE])

# ---------- 속초해수욕장 ----------
pg("sokcho-beach-saengseon-gui", "속초해수욕장 생선구이", "근처", "gui.jpg", "속초해수욕장 근처에서 생선구이를 찾는다면.",
 "해수욕장에서", "속초해수욕장에서 놀고 난 뒤 맵지 않은 생선구이가 생각난다면 남쪽 대포항으로 오세요.",
 "모듬생선구이", f"{GUI}는 그날 들어온 생선을 노릇하게 구워 한 판에 냅니다.",
 [A("sokcho-beach-matjip","속초해수욕장 근처 맛집"), A("fish-gui-matjip","생선구이 맛집")], [KIDS, TOGO])
pg("sokcho-beach-squid-sundae", "속초해수욕장 오징어순대", "근처", "squid-sundae.jpg", "해수욕장 다음 간식 겸 안주, 오징어순대.",
 "해수욕장에서", "바다에서 놀고 나면 출출해집니다. 속초 별미 오징어순대로 허기를 채워 보세요.",
 "누룽지 오징어순대", f"{SQUID}는 겉이 바삭하고 속은 촉촉합니다. 포장해 숙소에서 드셔도 좋습니다.",
 [A("sokcho-beach-matjip","속초해수욕장 근처 맛집"), A("squid-sundae-matjip","오징어순대 맛집")], [TOGO, WHERE])
pg("sokcho-beach-family", "속초해수욕장 가족 식사", "근처", "hall3.jpg", "해수욕장에서 놀고 온 가족, 다 같이 생선찜.",
 "가족 바다 여행", "속초해수욕장은 가족 여행객이 가장 많이 찾는 바다입니다. 아이들이 실컷 놀고 나면 든든한 식사가 필요합니다.",
 "가족 주문", f"{MODEUM} 대(4인)에 아이 몫으로 {GUI}를 더하세요. 넓은 홀이라 여럿이 앉기 편합니다.",
 [A("sokcho-beach-matjip","속초해수욕장 근처 맛집"), A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])
pg("sokcho-beach-takeout", "속초해수욕장 포장 맛집", "근처", "jjim-table.jpg", "해수욕장 근처 숙소에서 먹을 저녁, 포장해 가세요.",
 "숙소 저녁", "속초해수욕장 근처 숙소에 묵는다면 저녁을 포장해 바다를 보며 드시는 것도 좋습니다.",
 "포장", f"전 메뉴 포장됩니다. 미리 전화({TEL})로 주문하세요.",
 [A("sokcho-takeout-matjip","속초 포장 맛집"), A("sokcho-stay-in-dinner","속초 숙소에서 먹는 저녁")], [TOGO, HOURS])

# ---------- 근처 숙소 ----------
def stay(slug, kw, img, lede, place, s1, s2h, s2, near, near_kw, faq):
    pg(slug, kw, "근처", img, lede, f"{place}에서", s1, s2h, s2, [A(near, near_kw), A("daepohang-matjip","대포항 맛집")], faq)

stay("lotte-resort-lunch", "롯데리조트 속초 점심", "gui.jpg", "롯데리조트 체크아웃 후 점심, 대포항에서.", "롯데리조트 속초",
 "롯데리조트 속초에서 체크아웃하고 나면 점심 먹을 곳을 찾게 됩니다. 외옹치에서 남쪽으로 내려오면 대포항입니다.",
 "점심 메뉴", f"점심에는 {GUI}나 {GAORI} 소(2인)가 좋습니다.", "sokcho-lotte-resort-matjip", "속초 롯데리조트 근처 맛집", [WHERE, PARK])
stay("lotte-resort-takeout", "롯데리조트 속초 포장", "jjim-table.jpg", "롯데리조트 객실에서 먹을 생선찜, 포장해 가세요.", "롯데리조트 속초",
 "리조트 객실에서 바다를 보며 저녁을 먹고 싶다면 포장이 편합니다.",
 "포장 주문", f"전 메뉴 포장됩니다. 전화({TEL})로 미리 주문하고 시간 맞춰 찾으러 오세요.", "sokcho-lotte-resort-matjip", "속초 롯데리조트 근처 맛집", [TOGO, HOURS])
stay("lotte-resort-kids", "롯데리조트 아이랑 식사", "hall3.jpg", "롯데리조트에 아이와 묵는다면, 식사는 대포항.", "롯데리조트 속초",
 "롯데리조트 속초는 아이와 함께 오는 가족이 많습니다. 아이가 먹을 메뉴가 있는 식당을 찾는다면 대포항으로 오세요.",
 "아이 메뉴", f"맵지 않은 {GUI}와 {SQUID}가 아이 몫으로 좋습니다. 아기의자가 있습니다.", "sokcho-lotte-resort-matjip", "속초 롯데리조트 근처 맛집", [KIDS, PARK])
stay("lotte-resort-squid-sundae", "롯데리조트 오징어순대", "squid-sundae.jpg", "롯데리조트에서 가까운 오징어순대.", "롯데리조트 속초",
 "롯데리조트 속초에 묵으며 속초 별미 오징어순대를 맛보고 싶다면 대포항으로 오세요.",
 "누룽지 오징어순대", f"{SQUID}는 17,000원입니다(바뀔 수 있습니다). 포장해서 객실 야식으로 드셔도 좋습니다.", "sokcho-lotte-resort-matjip", "속초 롯데리조트 근처 맛집", [TOGO, WHERE])
stay("cassia-dinner", "카시아 속초 저녁", "gaori-jjim.jpg", "카시아 속초에 묵는 날, 저녁은 대포항.", "카시아 속초",
 "카시아 속초에 묵는 날 저녁, 숙소 밖 항구 식당에서 바다 도시다운 한 끼를 드셔 보세요.",
 "저녁 메뉴", f"대표 메뉴 {GAORI}을 추천합니다. 술 한잔 곁들이기도 좋습니다.", "cassia-sokcho-matjip", "카시아 속초 근처 맛집", [SIZE, HOURS])
stay("cassia-takeout", "카시아 속초 포장", "jjim-table.jpg", "카시아 객실에서 먹을 생선찜 포장.", "카시아 속초",
 "카시아 속초 객실에서 편하게 저녁을 드시고 싶다면 대포항에서 포장해 가세요.",
 "포장 주문", f"전 메뉴 포장됩니다. 전화({TEL})로 미리 주문하세요.", "cassia-sokcho-matjip", "카시아 속초 근처 맛집", [TOGO, HOURS])
stay("cassia-kids", "카시아 아이랑 식사", "hall3.jpg", "카시아 속초에 아이와 묵는다면.", "카시아 속초",
 "아이와 카시아 속초에 묵는 가족이라면, 아이도 함께 먹을 수 있는 메뉴가 있는 대포항 식당을 찾아보세요.",
 "아이 메뉴", f"맵지 않은 {GUI}와 순대가 있고 아기의자도 있습니다.", "cassia-sokcho-matjip", "카시아 속초 근처 맛집", [KIDS, PARK])
stay("maremons-dinner", "마레몬스 저녁", "gaori-jjim.jpg", "마레몬스에 묵는 날 저녁, 대포항 생선찜.", "마레몬스",
 "마레몬스 호텔에 묵는 날, 저녁은 바닷가를 따라 대포항으로 나와 드셔 보세요.",
 "저녁 메뉴", f"{GAORI}이나 {MODEUM}으로 하루를 마무리하세요.", "maremons-matjip", "마레몬스 근처 맛집", [SIZE, HOURS])
stay("maremons-takeout", "마레몬스 포장", "jjim-table.jpg", "마레몬스 객실에서 먹을 저녁, 포장해 가세요.", "마레몬스",
 "마레몬스 객실에서 바다를 보며 저녁을 드시고 싶다면 포장이 좋습니다.",
 "포장 주문", f"전 메뉴 포장됩니다. 전화({TEL})로 미리 주문하세요.", "maremons-matjip", "마레몬스 근처 맛집", [TOGO, HOURS])

# ---------- 대포동·물치 ----------
pg("daepodong-gaori-jjim", "대포동 가오리찜", "근처", "gaori-jjim.jpg", "대포동에서 가오리찜을 찾는다면, 바로 대포항.",
 "대포동", "대포동은 대포항이 있는 동네입니다. 동네 안에서 가오리찜을 찾는다면 대포항 안쪽 상가 1층으로 오세요.",
 "가오리찜", f"{GAORI}은 이 집 대표 메뉴입니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.",
 [A("daepodong-matjip","대포동 맛집"), A("daepohang-gaori-jjim","대포항 가오리찜")], [SIZE, TOGO])
pg("daepodong-lunch", "대포동 점심", "근처", "gui.jpg", "대포동에서 점심 먹을 곳, 대포항 생선구이.",
 "대포동 점심", "대포동 숙소에서 나와 점심을 먹는다면 걸어서 대포항까지 나와 보세요.",
 "점심 메뉴", f"{GUI}는 맵지 않아 점심으로 부담 없고, {SQUID}를 곁들이면 든든합니다.",
 [A("daepodong-matjip","대포동 맛집"), A("daepohang-lunch","대포항 점심")], [WHERE, PARK])
pg("daepodong-dinner", "대포동 저녁", "근처", "jjim-closeup.jpg", "대포동 저녁, 항구 불빛 아래 생선찜.",
 "대포동 저녁", "대포동에 묵는다면 저녁은 걸어서 대포항으로 나와 항구 불빛을 보며 드셔 보세요.",
 "저녁 메뉴", f"{KODARI}이나 {GAORI}에 술 한잔 곁들이기 좋습니다.", [A("daepodong-matjip","대포동 맛집"), A("daepohang-dinner","대포항 저녁")], [SIZE, HOURS])
pg("mulchi-lunch", "물치 점심", "근처", "gui.jpg", "물치에서 점심, 바로 위 대포항으로.",
 "물치에서", "물치는 속초와 맞닿은 양양 북쪽 바닷가 마을입니다. 북쪽으로 조금만 오면 대포항입니다.",
 "점심 메뉴", f"점심에는 {GUI}나 {GAORI} 소(2인)를 추천합니다.", [A("mulchihang-matjip","물치항 근처 맛집"), A("mulchi-saengseon-gui","물치 생선구이")], [WHERE, PARK])
pg("mulchi-dinner", "물치 저녁", "근처", "jjim-table.jpg", "물치 숙소에서 나와 대포항 저녁.",
 "물치에서", "물치 해변 근처에 묵는다면 저녁은 속초 첫 항구 대포항에서 드셔 보세요.",
 "저녁 메뉴", f"{MODEUM}이나 {GAORI}으로 여럿이 나눠 드세요.", [A("mulchihang-matjip","물치항 근처 맛집"), A("mulchi-saengseon-jjim","물치 생선찜")], [SIZE, HOURS])
pg("mulchi-family", "물치해변 가족 식사", "근처", "hall3.jpg", "물치해변에서 놀고 온 가족 식사.",
 "물치해변", "물치해변은 비교적 한적해서 가족 단위로 많이 찾습니다. 물놀이 뒤에는 온 가족이 함께 먹을 메뉴가 필요합니다.",
 "가족 주문", f"찜 대(4인)에 아이 몫으로 {GUI}를 더하세요. 아기의자가 있습니다.", [A("mulchihang-matjip","물치항 근처 맛집"), A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])

# ---------- 근처 명소·동네 ----------
pg("seorak-haemaji-lunch", "설악해맞이공원 점심", "근처", "gui.jpg", "해맞이공원 산책 후 점심.",
 "설악해맞이공원", "설악해맞이공원은 바닷가 산책로와 조형물이 있는 공원입니다. 산책 뒤 점심을 먹기에 대포항이 가깝습니다.",
 "점심 메뉴", f"{GUI}나 {SQUID}로 가볍게, 또는 {GAORI}으로 든든하게.", [A("seorak-haemaji-matjip","설악해맞이공원 맛집"), A("seorak-haemaji-saengseon-gui","설악해맞이공원 생선구이")], [WHERE, PARK])
pg("cheoksan-dinner", "척산온천 저녁", "근처", "jjim-closeup.jpg", "온천에서 몸 녹이고, 저녁은 생선찜.",
 "척산온천", "척산온천에서 온천욕을 하고 나면 따뜻한 저녁이 생각납니다.",
 "저녁 메뉴", f"뜨끈한 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이나 {KODARI}을 추천합니다.", [A("cheoksan-oncheon-matjip","척산온천 근처 맛집"), A("cheoksan-saengseon-jjim","척산온천 생선찜")], [SIZE, HOURS])
pg("waterpia-dinner", "설악워터피아 저녁", "근처", "jjim-table.jpg", "워터피아에서 놀고 난 저녁.",
 "설악워터피아", "워터피아에서 하루 종일 놀고 나면 온 가족이 배고픕니다. 바다 쪽 대포항으로 나와 저녁을 드세요.",
 "저녁 메뉴", f"{MODEUM} 대(4인)에 {GUI}를 더하면 여럿이 넉넉합니다.", [A("seorak-waterpia-matjip","설악워터피아 근처 맛집"), A("waterpia-saengseon-jjim","설악워터피아 생선찜")], [SIZE, HOURS])
pg("waterpia-kids", "워터피아 아이랑 식사", "근처", "hall3.jpg", "워터피아 다녀온 아이와 식사.",
 "아이와 워터피아", "물놀이를 마친 아이들은 금방 배가 고파집니다. 아이가 먹을 수 있는 메뉴가 있는 곳이 편합니다.",
 "아이 메뉴", f"맵지 않은 {GUI}와 {SQUID}가 있고 아기의자도 있습니다.", [A("seorak-waterpia-matjip","설악워터피아 근처 맛집"), A("sokcho-kids-matjip","속초 아이랑 맛집")], [KIDS, PARK])
pg("jeongam-saengseon-gui", "정암해변 생선구이", "근처", "gui.jpg", "정암해변 근처에서 생선구이를 찾는다면.",
 "정암해변", "정암해변은 물치 북쪽의 조용한 해변입니다. 속초 쪽으로 조금만 올라오면 대포항입니다.",
 "모듬생선구이", f"{GUI}는 여러 생선을 노릇하게 구워 한 판에 냅니다.", [A("jeongam-matjip","정암해변 근처 맛집"), A("fish-gui-matjip","생선구이 맛집")], [KIDS, TOGO])
pg("jeongam-lunch", "정암해변 점심", "근처", "jjim-table.jpg", "정암해변 산책 후 점심.",
 "정암해변", "조용한 정암해변을 걷고 나면 점심때입니다. 대포항이 가깝습니다.",
 "점심 메뉴", f"{GAORI} 소(2인)나 {GUI}를 추천합니다.", [A("jeongam-matjip","정암해변 근처 맛집"), A("mulchi-lunch","물치 점심")], [WHERE, PARK])
pg("sokcho-ic-saengseon-jjim", "속초IC 생선찜", "근처", "jjim-table.jpg", "속초IC로 나오면 첫 끼는 생선찜.",
 "속초IC에서", "서울양양고속도로를 타고 속초IC로 나오면 바다 쪽 대포항으로 가기 편합니다. 긴 운전 끝 첫 끼로 생선찜을 드셔 보세요.",
 "생선찜", f"{MODEUM}과 {GAORI}이 있습니다. 소(2인)부터 대(4인)까지 고를 수 있습니다.", [A("sokcho-ic-matjip","속초IC 근처 맛집"), A("fish-jjim-matjip","생선찜 맛집")], [SIZE, PARK])
pg("sokcho-ic-lunch", "속초IC 점심", "근처", "gui.jpg", "속초IC 나와서 점심 먹을 곳.",
 "점심때 도착", "아침 일찍 출발해 점심때 속초IC로 나왔다면 바로 대포항으로 와서 점심을 드세요.",
 "점심 메뉴", f"{GUI}나 {GAORI} 소(2인)가 좋습니다.", [A("sokcho-ic-matjip","속초IC 근처 맛집"), A("sokcho-lunch-matjip","속초 점심 맛집")], [WHERE, PARK])
pg("joyangdong-saengseon-gui", "조양동 생선구이", "근처", "gui.jpg", "조양동에서 생선구이 먹으러 대포항으로.",
 "조양동", "조양동은 속초 남쪽의 주거 동네입니다. 생선구이가 당길 때 대포항까지 나와 보세요.",
 "모듬생선구이", f"{GUI}는 맵지 않아 가족 외식으로 좋습니다.", [A("joyangdong-matjip","조양동 맛집"), A("joyangdong-saengseon-jjim","속초 조양동 생선찜")], [KIDS, TOGO])
pg("joyangdong-family", "조양동 가족 외식", "근처", "hall.jpg", "조양동 가족 외식, 주말엔 대포항 생선찜.",
 "동네 가족 외식", "주말에 가족끼리 외식할 곳을 찾는 조양동 주민이라면 대포항 생선찜 집을 찾아 주세요.",
 "가족 주문", f"{GAORI} 대(4인)와 {GUI}를 함께 시키는 가족이 많습니다. 넓은 홀이라 편하게 앉을 수 있습니다.", [A("joyangdong-matjip","조양동 맛집"), A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])
pg("cheongdaesan-lunch", "청대산 등산 후 점심", "근처", "jjim-closeup.jpg", "청대산 오르고 내려와 점심.",
 "청대산", "청대산은 속초 시내에서 가볍게 오를 수 있는 낮은 산입니다. 정상에서 바다와 설악산이 함께 보입니다.",
 "등산 후 점심", f"땀 흘린 뒤에는 매콤한 {KODARI}이나 든든한 {MODEUM}을 추천합니다.", [A("cheongdaesan-matjip","청대산 맛집"), A("sokcho-hiking-club","속초 산악회 식사")], [WHERE, SIZE])
pg("cheongchoho-dinner", "청초호 저녁", "근처", "jjim-table.jpg", "청초호 야경 보고 저녁.",
 "청초호", "청초호는 속초 시내 가운데 있는 호수로, 저녁이면 호숫가 불빛이 예쁩니다.",
 "저녁 메뉴", f"호수 산책 뒤 남쪽 대포항으로 내려와 {GAORI}이나 {MODEUM}으로 저녁을 드세요.", [A("cheongchoho-matjip","청초호 근처 맛집"), A("cheongchoho-saengseon-jjim","청초호 생선찜")], [SIZE, HOURS])
pg("cheongchoho-gaori-jjim", "청초호 가오리찜", "근처", "gaori-jjim.jpg", "청초호 근처에서 가오리찜을 찾는다면.",
 "청초호에서", "청초호 둘레길을 걷고 나서 쫀득한 가오리찜이 생각난다면 대포항으로 오세요.",
 "가오리찜", f"{GAORI}은 이 집 대표 메뉴입니다. 삭히지 않은 가오리라 냄새가 없습니다.", [A("cheongchoho-matjip","청초호 근처 맛집"), A("gaori-jjim-matjip","가오리찜 맛집")], [SIZE, TOGO])
pg("expo-gaori-jjim", "엑스포공원 가오리찜", "근처", "gaori-jjim.jpg", "엑스포공원 근처에서 가오리찜을 찾는다면.",
 "엑스포공원에서", "엑스포공원과 엑스포타워를 둘러본 뒤 대포항으로 내려와 가오리찜을 드셔 보세요.",
 "가오리찜", f"{GAORI}은 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.", [A("sokcho-expo-matjip","속초 엑스포공원 맛집"), A("gaori-jjim-matjip","가오리찜 맛집")], [SIZE, TOGO])
pg("domundong-saengseon-jjim", "도문동 생선찜", "근처", "jjim-table.jpg", "도문동에서 생선찜 먹으러 대포항으로.",
 "도문동", "도문동은 설악산 쪽 조용한 동네로, 상도문 돌담마을이 있습니다.",
 "생선찜", f"{MODEUM}은 여러 생선을 매콤한 양념에 쪄 냅니다. 소(2인)부터 대(4인)까지 있습니다.", [A("domundong-matjip","속초 도문동 맛집"), A("sangdomun-matjip","상도문 돌담마을 맛집")], [SIZE, TOGO])
pg("haksapyeong-saengseon-jjim", "학사평 생선찜", "근처", "jjim-closeup.jpg", "학사평 순두부 말고 생선찜이 당길 때.",
 "학사평", "학사평은 순두부 마을로 알려진 곳입니다. 다른 끼니에는 바다 쪽으로 나와 생선찜을 드셔 보세요.",
 "생선찜", f"{GAORI}, {KODARI}, {A('sokcho-daegu-ppol-jjim','대구뽈찜')}, {MODEUM}이 있습니다.", [A("haksapyeong-matjip","학사평 근처 맛집"), A("fish-jjim-matjip","생선찜 맛집")], [SIZE, TOGO])

assert len(P) == 50, len(P)
