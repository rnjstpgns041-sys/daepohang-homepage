# 50 keyword pages (added 2026-10-20), batch 451-500.
# Goal from the owner: keywords that bring people to the shop. So: searches for the shop's own name
# (menu, location, parking, takeout), days most restaurants close (월·화), weather, 양양/고성 + meal,
# and "잘하는 집" style dish searches. No pages about dishes the shop doesn't sell (owner removed those).
# Store facts only from the listing / photos. Opening hours are unconfirmed, so pages point to the phone.
from pages2 import add as _add, L, A

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

TEL = "0507-1364-4060"
MENU_LINKS = L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-saengseon-gui","모듬생선구이"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"))
WHERE = ("가게 위치는?","속초시 대포항길 10, 대포항 안쪽 상가 1층입니다.")
OFF = ("휴무일은?","매주 수요일입니다.")
TOGO = ("포장되나요?","네, 전 메뉴 포장됩니다.")
SIZE = ("사이즈는 어떻게 되나요?","찜은 소(2인), 중(3인), 대(4인)입니다.")
PARK = ("주차는?",A("daepohang-parking","주차 안내")+"를 참고하세요.")
PET = ("반려동물 동반 되나요?","네, 반려동물과 함께 오실 수 있습니다.")
KIDS = ("아이와 가도 되나요?","네, 아기 의자가 있고 맵지 않은 생선구이와 순대가 있습니다.")
HOURS = ("몇 시까지 하나요?",f"영업시간은 전화({TEL})로 확인해 주세요.")
SHOP = f"<p>대포항생선찜본점은 속초시 대포항길 10, 대포항 안쪽 상가 1층에 있습니다. 노란색과 분홍색 네온 간판을 찾으세요. 매주 수요일은 쉬고, 전 메뉴 포장됩니다. 전화 {TEL}.</p>"
MENU_ALL = L("가오리찜 (소·중·대)", "생선모듬찜 (소·중·대)", "대구뽈찜 (소·중·대)", "코다리찜 (소·중·대)", "모듬생선구이", "누룽지 오징어순대 17,000원", "속초 아바이순대", "소주, 맥주, 막걸리, 청하, 백세주 · 공깃밥, 음료수")

# ---------- 가게 이름으로 찾는 분 ----------
def brand(slug, kw, lede, sections, faq):
    add(slug, kw, "대포항", "storefront.jpg", lede, sections + [("가게 정보", SHOP)], faq)

brand("brand-menu", "대포항생선찜본점 메뉴", "대포항생선찜본점 메뉴를 한눈에 정리했어요.",
 [("전체 메뉴", MENU_ALL),
  ("찜 사이즈", "<p>찜은 소(2인), 중(3인), 대(4인)입니다. 가격은 계절과 시세에 따라 바뀔 수 있어 전화로 확인해 주세요.</p>"),
  ("처음이라면", f"<p>대표 메뉴는 {A('sokcho-gaori-jjim','가오리찜')}입니다. 맵지 않은 메뉴가 필요하면 {A('sokcho-saengseon-gui','모듬생선구이')}를 더하세요.</p>")],
 [SIZE, TOGO])
brand("brand-location", "대포항생선찜본점 위치", "대포항생선찜본점 찾아오는 길.",
 [("주소", "<p>강원특별자치도 속초시 대포항길 10, 대포항 안쪽 상가 1층입니다.</p>"),
  ("찾는 법", L("내비게이션에 ‘대포항길 10’ 또는 ‘대포항생선찜본점’을 입력하세요.", "대포항 공영주차장에 세우고 항구 안쪽 상가로 걸어오세요.", "노란색과 분홍색 네온 간판이 보이면 도착입니다.")),
  ("더 보기", L(A("daepohang-directions","대포항 가는 법"), A("daepohang-parking","대포항 주차"), A("daepohang-matjip","대포항 맛집")))],
 [PARK, OFF])
brand("brand-parking", "대포항생선찜본점 주차", "대포항생선찜본점에 차를 가지고 오실 때.",
 [("어디에 세우나요", f"<p>가게 앞에는 따로 주차장이 없어서 대포항 공영주차장을 이용하시면 됩니다. 자세한 내용은 {A('daepohang-parking','대포항 주차 안내')}에 있습니다.</p>"),
  ("주말에는", "<p>주말과 연휴에는 항구 주변이 붐빕니다. 이른 시간에 오시거나 조금 떨어진 주차장에 세우고 걸어오시면 편합니다.</p>")],
 [WHERE, TOGO])
brand("brand-takeout", "대포항생선찜본점 포장", "대포항생선찜본점은 전 메뉴 포장됩니다.",
 [("포장 주문", f"<p>찜, 구이, 순대 모두 포장됩니다. 전화({TEL})로 미리 주문하시면 기다리지 않고 받아 가실 수 있습니다.</p>"),
  ("숙소에서 먹을 때", f"<p>찜은 냄비에 옮겨 약불로 데우면 됩니다. {A('saengseon-jjim-reheat','생선찜 데우는 법')}, {A('squid-sundae-reheat','오징어순대 데우는 법')}을 참고하세요.</p>"),
  ("더 보기", L(A("gaori-jjim-takeout","가오리찜 포장"), A("saengseon-gui-takeout","생선구이 포장"), A("daepohang-takeout","대포항 포장")))],
 [SIZE, OFF])
brand("brand-reservation", "대포항생선찜본점 예약", "자리 문의와 포장 예약은 전화 한 통이면 돼요.",
 [("전화로 문의", f"<p>인원과 도착 시간을 알려 주시면 자리를 안내해 드립니다. 전화 {TEL}.</p>"),
  ("여럿이 오신다면", f"<p>가족 모임이나 단체라면 미리 전화 주세요. 찜은 대(4인)를 여러 개 시키거나 종류를 섞어 주문하시면 됩니다. {A('sokcho-group-restaurant','속초 단체 식당')}도 참고하세요.</p>")],
 [SIZE, OFF])
brand("brand-gaori-jjim", "대포항생선찜본점 가오리찜", "대포항생선찜본점의 대표 메뉴, 가오리찜.",
 [("가오리찜", f"<p>쫀득한 가오리 살과 오독한 연골에 매콤달콤한 양념이 배어 있습니다. 삭히지 않아 냄새가 없고, 소(2인), 중(3인), 대(4인)로 주문합니다.</p>"),
  ("더 보기", L(A("sokcho-gaori-jjim","속초 가오리찜"), A("gaori-jjim-how-to-eat","가오리찜 맛있게 먹는 법"), A("gaori-jjim-spicy-level","가오리찜 맵기")))],
 [SIZE, TOGO])
brand("brand-pet", "대포항생선찜본점 애견동반", "강아지와 함께 들어갈 수 있는 대포항 생선찜집.",
 [("반려동물 동반", "<p>대포항생선찜본점은 반려동물과 함께 오실 수 있습니다. 다른 손님을 위해 목줄을 해 주세요.</p>"),
  ("더 보기", L(A("daepohang-pet-friendly","대포항 애견동반"), A("sokcho-pet-friendly-restaurant","속초 애견동반 식당"), A("sokcho-pet-travel","속초 애견동반 여행")))],
 [PET, KIDS])

# ---------- 요일 · 날씨 ----------
def day(slug, kw, lede, why, tip):
    add(slug, kw, "상황별", "jjim-table.jpg", lede,
     [("이날 속초에서", f"<p>{why}</p>"),
      ("대포항생선찜본점은", f"<p>매주 수요일만 쉽니다. {tip} 영업시간은 전화({TEL})로 확인해 주세요.</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP)],
     [OFF, HOURS])

day("sokcho-monday-matjip", "속초 월요일 맛집", "월요일에 문 여는 속초 생선찜집.",
 "월요일에 쉬는 식당이 적지 않아 헛걸음하기 쉽습니다. 주말 여행을 하루 늘려 월요일까지 머무는 분들이 특히 많이 찾습니다.",
 "월요일에도 문을 엽니다.")
day("sokcho-tuesday-matjip", "속초 화요일 맛집", "화요일 속초 여행, 문 연 식당 찾기.",
 "평일 여행은 한적해서 좋지만, 쉬는 날이 가게마다 달라 미리 확인하는 것이 좋습니다.",
 "화요일에도 문을 엽니다.")
day("sokcho-sunday-matjip", "속초 일요일 맛집", "일요일 속초, 집에 가기 전 한 끼.",
 "일요일에는 오후에 서울로 돌아가는 차가 많아 점심을 일찍 먹고 출발하는 분이 많습니다.",
 "일요일에도 문을 엽니다. 포장해서 가셔도 됩니다.")
day("sokcho-friday-dinner", "속초 금요일 저녁", "금요일 밤 속초 도착, 저녁은 생선찜으로.",
 "금요일 퇴근 후 출발하면 저녁 늦게 속초에 닿는 경우가 많습니다. 도착 시간에 맞춰 미리 전화해 두면 편합니다.",
 "금요일에도 문을 엽니다.")

def weather(slug, kw, lede, about, pick):
    add(slug, kw, "상황별", "jjim-closeup.jpg", lede,
     [("이런 날엔", f"<p>{about}</p>"),
      ("추천", f"<p>{pick}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", L(A("sokcho-winter-matjip","속초 겨울 맛집"), A("sokcho-rainy-day-matjip","속초 비오는날 맛집"), A("sokcho-indoor","속초 실내 가볼만한곳")))],
     [WHERE, TOGO])

weather("sokcho-cold-day", "속초 추운 날 맛집", "바닷바람에 언 몸, 뜨끈한 찜으로 녹이세요.",
 "속초는 바닷바람 때문에 같은 기온이라도 더 춥게 느껴집니다. 항구를 걷고 나면 따뜻한 실내와 뜨끈한 음식이 간절해집니다.",
 f"보글보글 끓는 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이나 {A('sokcho-kodari-jjim','코다리찜')}에 밥 한 공기면 몸이 금방 풀립니다.")
weather("sokcho-warm-food", "속초 따뜻한 음식", "속초에서 먹는 따뜻한 한 끼.",
 "회나 물회처럼 찬 음식이 많은 바닷가에서 따뜻한 밥이 생각날 때가 있습니다. 아이나 부모님과 함께라면 더욱 그렇습니다.",
 f"뜨거운 철판에 나오는 {A('sokcho-saengseon-gui','모듬생선구이')}와 김이 오르는 {A('sokcho-gaori-jjim','가오리찜')}을 추천합니다.")
weather("sokcho-snow-day", "속초 눈 오는 날 맛집", "눈 내리는 속초, 창밖 보며 먹는 생선찜.",
 "눈 오는 날 속초는 풍경이 아름답지만 길이 미끄럽습니다. 멀리 다니기보다 한 곳에서 오래 머무는 일정이 좋습니다.",
 f"항구 앞에서 따뜻한 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}을 나눠 드셔 보세요. 미끄러운 날에는 포장해서 숙소에서 드시는 것도 방법입니다.")

# ---------- 입맛 ----------
def taste(slug, kw, lede, about, pick, more):
    add(slug, kw, "메뉴", "gui.jpg", lede,
     [("이런 분께", f"<p>{about}</p>"),
      ("추천 메뉴", f"<p>{pick}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [KIDS, TOGO])

taste("sokcho-light-food", "속초 담백한 음식", "맵고 짠 게 부담될 때, 담백한 생선구이.",
 "여행 중 자극적인 음식을 이어서 먹다 보면 담백한 한 끼가 생각납니다.",
 f"{A('sokcho-saengseon-gui','모듬생선구이')}는 맵지 않고 생선 본연의 맛이 살아 있습니다. {A('sokcho-abai-sundae','아바이순대')}도 맵지 않습니다.",
 L(A("sokcho-mild-menu","속초 안 매운 메뉴"), A("soft-fish-dish","부드러운 생선 요리"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리")))
taste("sokcho-diet-matjip", "속초 다이어트 맛집", "여행 중에도 가볍게, 생선 위주의 한 끼.",
 "여행 중에도 식단을 신경 쓰는 분이라면 튀김이나 고기보다 생선 요리가 부담이 적습니다.",
 f"기름을 적게 쓰는 {A('sokcho-saengseon-gui','모듬생선구이')}에 밥 양을 조절해 드셔 보세요. 찜은 양념을 덜어 내고 드시면 됩니다.",
 L(A("sokcho-light-food","속초 담백한 음식"), A("saengseon-gui-kinds","생선구이 종류"), A("sokcho-mild-menu","속초 안 매운 메뉴")))
taste("sokcho-bapdoduk-matjip", "속초 밥반찬 맛집", "밥 한 공기가 모자란 생선찜.",
 "반찬 하나에 밥 두 공기가 사라지는 음식을 찾는다면 양념 진한 생선찜이 제격입니다.",
 f"{A('sokcho-kodari-jjim','코다리찜')}과 {A('sokcho-gaori-jjim','가오리찜')}의 양념, 그리고 양념 밴 무까지 밥반찬으로 최고입니다. 마지막엔 남은 양념에 밥을 비벼 드세요.",
 L(A("sokcho-bapdoduk","속초 밥도둑 메뉴"), A("saengseon-jjim-bibim","생선찜 양념 밥 비벼먹기"), A("saengseon-jjim-mu","생선찜 무")))

# ---------- 맛집 찾는 말투 ----------
add("sokcho-hidden-matjip", "속초 숨은 맛집", "주변", "storefront.jpg",
 "항구 안쪽 상가에 숨어 있는 생선찜집.",
 [("큰길에서 안 보이는 집", "<p>대포항생선찜본점은 큰길이 아니라 대포항 안쪽 상가 1층에 있습니다. 항구를 걷다가 노란색과 분홍색 네온 간판을 보고 들어오시는 분이 많습니다.</p>"),
  ("찾아오는 법", f"<p>대포항 공영주차장에 세우고 항구 안쪽으로 걸어오세요. {A('brand-location','위치 안내')}를 참고하세요.</p>"),
  ("추천 메뉴", MENU_LINKS)],
 [WHERE, PARK])
add("sokcho-insaeng-matjip", "속초 인생 맛집", "주변", "jjim-table.jpg",
 "속초에서 꼭 한 번 먹어 볼 생선찜 한 상.",
 [("속초에서 먹어 볼 것", "<p>속초는 생선과 오징어의 도시입니다. 항구 앞에서 먹는 생선찜과 오징어순대는 여행의 기억으로 오래 남습니다.</p>"),
  ("한 상 차림", f"<p>{A('sokcho-gaori-jjim','가오리찜')}에 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 곁들이면 속초다운 한 상이 완성됩니다.</p>"),
  ("가게 정보", SHOP)],
 [SIZE, TOGO])

# ---------- 모임 ----------
add("sokcho-gyemoim", "속초 계모임 식당", "상황별", "jjim-table.jpg",
 "계모임 여행, 다 같이 나눠 먹는 생선찜.",
 [("모임 식사로 좋은 이유", "<p>큰 냄비 찜을 가운데 두고 나눠 먹으면 대화도 자연스럽습니다. 맵지 않은 구이를 함께 시키면 입맛이 달라도 걱정이 없습니다.</p>"),
  ("주문 예시", L("6명: 찜 대 + 찜 소 + 모듬생선구이", "8명: 찜 대 2개 + 모듬생선구이 + 누룽지 오징어순대")),
  ("미리 전화하세요", f"<p>여럿이 오시면 자리를 위해 미리 전화({TEL}) 주세요.</p>")],
 [SIZE, PARK])

# ---------- 양양 · 고성 + 식사 ----------
def town(slug, kw, lede, about, more, faq):
    town_ = kw.split()[0]
    add(slug, kw, "근처", "storefront.jpg", lede,
     [(f"{town_}에서", f"<p>{about}</p>"),
      ("속초 대포항으로", f"<p>대포항은 속초 남쪽 끝이라 {town_}에서 오가기 편합니다. 대포항생선찜본점에서 생선찜, 생선구이, 순대를 한 번에 드실 수 있습니다.</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

town("yangyang-dinner-matjip", "양양 저녁 맛집", "양양에서 놀고 저녁은 속초 대포항에서.",
 "양양 해변에서 하루를 보내면 저녁엔 든든한 밥이 생각납니다. 북쪽으로 조금만 올라오면 속초 대포항입니다.",
 L(A("yangyang-matjip","양양 맛집"), A("yangyang-saengseon-jjim","양양 생선찜"), A("yangyang-surf-matjip","양양 서핑 후 맛집")), [WHERE, TOGO])
town("yangyang-lunch-matjip", "양양 점심 맛집", "양양 여행 중 점심, 생선 한 상.",
 "낙산사나 해변 일정 사이에 점심을 먹을 곳을 찾는다면, 속초 쪽으로 올라오는 길에 대포항을 넣어 보세요.",
 L(A("yangyang-matjip","양양 맛집"), A("naksansa-matjip","낙산사 가는 길 맛집"), A("yangyang-saengseon-gui","양양 생선구이")), [WHERE, PARK])
town("yangyang-family-matjip", "양양 가족 맛집", "양양 가족 여행, 다 같이 먹는 생선찜.",
 "아이와 부모님까지 함께하는 양양 여행이라면 매운 것과 안 매운 것을 함께 시킬 수 있는 식당이 편합니다.",
 L(A("yangyang-matjip","양양 맛집"), A("family-dining-menu","가족 외식 메뉴 추천"), A("sokcho-family-dining","속초 가족 외식")), [KIDS, SIZE])
town("yangyang-kids-matjip", "양양 아이랑 맛집", "아이와 양양 여행, 맵지 않은 생선구이.",
 "해변에서 실컷 논 아이들은 금방 배가 고파집니다. 맵지 않고 가시 바르기 쉬운 메뉴가 있으면 편합니다.",
 L(A("sokcho-kids-matjip","속초 아이랑 맛집"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리"), A("saengseon-gasi-tip","생선 가시 바르는 법")), [KIDS, TOGO])
town("yangyang-pet-restaurant", "양양 애견동반 식당", "강아지와 양양 여행, 함께 들어가는 식당.",
 "양양은 강아지와 함께 오는 여행객이 많지만, 식당은 동반이 안 되는 곳도 있어 미리 확인해야 합니다.",
 L(A("sokcho-pet-friendly-restaurant","속초 애견동반 식당"), A("brand-pet","대포항생선찜본점 애견동반"), A("gangwon-pet-trip","강원도 애견동반 여행")), [PET, TOGO])
town("yangyang-bapjip", "양양 밥집", "양양 여행 중 밥 한 끼 제대로 먹고 싶을 때.",
 "카페와 간식이 많은 양양에서 제대로 된 밥 한 끼가 필요하다면 생선찜이 좋습니다.",
 L(A("sokcho-bapjip","속초 밥집"), A("yangyang-matjip","양양 맛집"), A("sokcho-bapdoduk-matjip","속초 밥반찬 맛집")), [SIZE, TOGO])
town("yangyang-seafood-matjip", "양양 해산물 맛집", "양양 바다 여행, 익힌 생선 요리로 한 끼.",
 "양양 해산물은 회와 물회가 많지만, 익힌 생선 요리를 찾는 분도 많습니다.",
 L(A("sokcho-seafood","속초 해산물 맛집"), A("yangyang-matjip","양양 맛집"), A("donghaean-matjip","동해안 맛집")), [WHERE, KIDS])
town("goseong-dinner-matjip", "고성 저녁 맛집", "고성 여행 후 저녁, 속초 대포항 생선찜.",
 "고성은 조용한 해변이 많은 대신 저녁 먹을 곳이 많지 않은 동네도 있습니다. 숙소가 속초라면 내려오는 길에 저녁을 해결하세요.",
 L(A("goseong-matjip","고성 맛집"), A("goseong-saengseon-jjim","고성 생선찜"), A("goseong-trip-matjip","고성 여행 속초 맛집")), [WHERE, TOGO])
town("goseong-family-matjip", "고성 가족 맛집", "고성 가족 여행, 속초에서 다 같이 먹는 한 끼.",
 "통일전망대, 화진포를 둘러보는 가족 여행이라면 속초로 돌아오는 길에 함께 먹을 식당을 정해 두면 편합니다.",
 L(A("goseong-matjip","고성 맛집"), A("family-trip-korea","국내 가족여행지 추천"), A("sokcho-family-trip","속초 가족여행 코스")), [KIDS, SIZE])
town("goseong-pet-restaurant", "고성 애견동반 식당", "강아지와 고성 여행, 함께 들어가는 식당.",
 "고성 해변은 강아지와 산책하기 좋지만 식당 동반 여부는 곳마다 다릅니다.",
 L(A("brand-pet","대포항생선찜본점 애견동반"), A("sokcho-pet-travel","속초 애견동반 여행"), A("gangwon-pet-trip","강원도 애견동반 여행")), [PET, TOGO])
town("jeongam-matjip", "정암해변 근처 맛집", "양양 정암해변에서 놀고 속초 대포항에서 식사.",
 "정암해변은 양양 북쪽 끝, 속초와 맞닿은 조용한 해변입니다.",
 L(A("mulchihang-matjip","물치항 근처 맛집"), A("seorak-beach-matjip","설악해변 근처 맛집"), A("yangyang-matjip","양양 맛집")), [WHERE, PARK])

# ---------- '잘하는 집' / 메뉴 맛집 ----------
def good(slug, kw, dish, dish_slug, img, about, more):
    add(slug, kw, "메뉴", img, f"{dish} 잘하는 집을 찾는다면, 속초 대포항으로.",
     [(f"{dish} 잘하는 집의 조건", f"<p>{about}</p>"),
      ("대포항생선찜본점", f"<p>{A(dish_slug, dish)}{'을' if (ord(dish[-1]) - 0xAC00) % 28 else '를'} 드실 수 있습니다. 찜은 소(2인), 중(3인), 대(4인)로, 전 메뉴 포장됩니다.</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [SIZE, TOGO])

good("gaori-jjim-good", "가오리찜 잘하는 집", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg",
 "가오리는 잘 말려야 살이 쫀득하고, 양념이 살 속까지 배어야 맛있습니다. 연골이 오독하게 씹히는지도 중요합니다.",
 L(A("gaori-jjim-matjip","가오리찜 맛집"), A("gaori-jjim-taste","가오리찜 맛"), A("brand-gaori-jjim","대포항생선찜본점 가오리찜")))
good("fish-jjim-good", "생선찜 잘하는 집", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "생선찜은 생선이 부서지지 않으면서 양념이 고루 배어야 하고, 바닥에 깐 무까지 맛있어야 합니다.",
 L(A("fish-jjim-matjip","생선찜 맛집"), A("sokcho-saengseon-jjim","속초 생선찜"), A("saengseon-jjim-mu","생선찜 무")))
good("fish-gui-good", "생선구이 잘하는 집", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 "생선구이는 껍질이 바삭하고 속살이 촉촉해야 합니다. 식지 않게 뜨거운 판에 나오면 더 좋습니다.",
 L(A("fish-gui-matjip","생선구이 맛집"), A("sokcho-saengseon-gui","속초 생선구이"), A("saengseon-gui-how-to-eat","생선구이 맛있게 먹는 법")))
good("squid-sundae-good", "오징어순대 잘하는 집", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg",
 "오징어순대는 속이 꽉 차고, 부칠 때 겉이 바삭해야 맛있습니다.",
 L(A("squid-sundae-matjip","오징어순대 맛집"), A("daepohang-nurungji-sundae","대포항 누룽지 오징어순대"), A("squid-sundae-taste","오징어순대 맛")))
good("kodari-jjim-good", "코다리찜 잘하는 집", "코다리찜", "sokcho-kodari-jjim", "jjim-closeup.jpg",
 "코다리는 적당히 말라 살이 쫄깃해야 하고, 양념이 진해야 밥반찬으로 좋습니다.",
 L(A("kodari-jjim-matjip","코다리찜 맛집"), A("kodari-jjim-taste","코다리찜 맛"), A("kodari-jorim","코다리조림")))
good("daegu-ppol-good", "대구뽈찜 잘하는 집", "대구뽈찜", "sokcho-daegu-ppol-jjim", "jjim-closeup.jpg",
 "대구뽈찜은 볼살이 쫀득하고 껍질이 말랑해야 합니다. 양념이 너무 맵기만 하면 대구 맛이 묻힙니다.",
 L(A("daegu-ppol-matjip","대구뽈찜 맛집"), A("daegu-ppol-taste","대구뽈찜 맛"), A("daegu-ppol-how-to-eat","대구뽈찜 먹는 법")))

def menu_matjip(slug, kw, dish, dish_slug, img, about, more):
    add(slug, kw, "메뉴", img, f"{dish}, 속초 대포항에서 드셔 보세요.",
     [(f"{dish}는", f"<p>{about}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [TOGO, WHERE])

menu_matjip("modeum-jjim-matjip", "생선모듬찜 맛집", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 f"여러 생선을 한 냄비에 담아 쪄 내 골라 먹는 재미가 있습니다. 한 가지를 고르기 어려울 때 가장 무난한 선택입니다. {A('sokcho-saengseon-modeum-jjim','속초 생선모듬찜')}을 참고하세요.",
 L(A("modeum-jjim-guide","생선모듬찜 고르는 이유"), A("modeum-jjim-takeout","생선모듬찜 포장"), A("modeum-or-gaori","생선모듬찜 가오리찜 고르기")))
menu_matjip("modeum-gui-matjip", "모듬생선구이 맛집", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 f"그날 들어온 여러 생선을 함께 구워 뜨거운 판에 냅니다. 맵지 않아 아이와 부모님도 잘 드십니다. {A('sokcho-saengseon-gui','속초 생선구이')}를 참고하세요.",
 L(A("modeum-gui-taste","모듬생선구이 맛"), A("saengseon-gui-kinds","생선구이 종류"), A("saengseon-gui-takeout","생선구이 포장")))
menu_matjip("nurungji-sundae-matjip", "누룽지 오징어순대 맛집", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg",
 f"오징어 속을 채워 겉을 누룽지처럼 바삭하게 지져 냅니다. 17,000원입니다. {A('sokcho-nurungji-squid-sundae','속초 누룽지 오징어순대')}를 참고하세요.",
 L(A("nurungji-ojingeo-sundae-how-to-eat","누룽지 오징어순대 먹는 법"), A("nurungji-sundae-price","누룽지 오징어순대 가격"), A("ojingeo-sundae-takeout","오징어순대 포장")))

add("gaori-jjim-2in", "가오리찜 2인", "메뉴", "gaori-jjim.jpg",
 "둘이 먹는 가오리찜, 소 사이즈면 충분해요.",
 [("둘이라면", f"<p>가오리찜 소(2인)가 두 사람에게 알맞습니다. 조금 더 드시고 싶다면 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 곁들이세요.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-jjim-2in","속초 2인 생선찜"), A("jjim-size-guide","생선찜 사이즈 고르기"), A("couple-trip-korea","국내 커플 여행지")))],
 [SIZE, TOGO])
add("gaori-jjim-4in", "가오리찜 4인 가족", "메뉴", "gaori-jjim.jpg",
 "네 식구가 먹는 가오리찜, 대 사이즈에 구이 하나.",
 [("넷이라면", f"<p>가오리찜 대(4인)가 네 사람에게 알맞습니다. 아이가 있다면 맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}를 함께 시키세요.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-jjim-4in","속초 4인 가족 생선찜"), A("jjim-size-guide","생선찜 사이즈 고르기"), A("family-dining-menu","가족 외식 메뉴 추천")))],
 [SIZE, KIDS])

# ---------- 강원도 넓은 키워드 ----------
def gangwon(slug, kw, lede, about, ours, more, faq):
    add(slug, kw, "여행", "storefront.jpg", lede,
     [("강원도에서", f"<p>{about}</p>"),
      ("속초 대포항에서", f"<p>{ours}</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("더 보기", more)],
     faq)

gangwon("gangwon-sea-matjip", "강원도 바다 맛집", "강원도 바다 앞에서 먹는 생선 한 상.",
 "강원도 바닷가 맛집은 항구마다 하나씩 이름난 곳이 있습니다. 회, 물회, 생선 요리가 대표적입니다.",
 "대포항 안쪽 상가의 대포항생선찜본점에서는 가오리찜과 생선구이를 드실 수 있습니다.",
 L(A("gangwon-sea-trip","강원도 바다 여행"), A("donghaean-matjip","동해안 맛집"), A("sokcho-harbor-matjip","속초 항구 맛집")), [WHERE, PARK])
gangwon("gangwon-family-matjip", "강원도 가족 맛집", "강원도 가족 여행, 다 같이 먹기 좋은 식당.",
 "가족 여행에서는 아이와 어른이 모두 먹을 메뉴가 있는 식당이 편합니다.",
 "찜은 인원에 맞춰 소·중·대로 고르고, 맵지 않은 생선구이로 아이 메뉴를 해결하세요. 아기 의자도 있습니다.",
 L(A("family-trip-korea","국내 가족여행지 추천"), A("sokcho-family-dining","속초 가족 외식"), A("gangwon-kids","강원도 아이랑 가볼만한곳")), [KIDS, SIZE])
gangwon("gangwon-squid-sundae", "강원도 오징어순대", "강원도 별미 오징어순대, 속초에서.",
 "오징어순대는 강원도 동해안, 그중에서도 속초가 유명합니다.",
 "대포항생선찜본점의 누룽지 오징어순대는 겉을 바삭하게 지져 냅니다. 17,000원입니다.",
 L(A("squid-sundae-matjip","오징어순대 맛집"), A("ojingeo-sundae-story","오징어순대 이야기"), A("yangyang-squid-sundae","양양 오징어순대")), [TOGO, WHERE])
gangwon("gangwon-local-food", "강원도 향토 음식", "강원도 바닷가 향토 음식, 생선찜과 순대.",
 "강원도 향토 음식은 산 쪽의 감자, 메밀, 옥수수와 바다 쪽의 말린 생선, 오징어, 순대로 나뉩니다.",
 "바다 쪽 향토 음식을 맛보려면 말린 생선으로 만든 가오리찜, 코다리찜과 실향민이 전한 아바이순대를 드셔 보세요.",
 L(A("sokcho-local-food","속초 현지 음식"), A("sokcho-silhyangmin-food","속초 실향민 음식"), A("gangwon-matjip","강원도 맛집")), [TOGO])
gangwon("gangwon-food", "강원도 먹거리", "강원도 여행 먹거리, 바다 쪽이라면 이것.",
 "강원도 먹거리는 막국수, 감자전, 닭갈비 같은 산 쪽 음식과 생선, 오징어 같은 바다 쪽 음식이 있습니다.",
 "속초에 왔다면 생선찜과 오징어순대를 한 번은 드셔 보세요. 대포항생선찜본점에서 한 상으로 드실 수 있습니다.",
 L(A("sokcho-food","속초 먹거리"), A("gangwon-local-food","강원도 향토 음식"), A("sokcho-must-eat","속초 꼭 먹어야 할 음식")), [TOGO, WHERE])
gangwon("gangwon-fish-matjip", "강원도 생선 맛집", "강원도 생선 요리, 찜과 구이를 한 곳에서.",
 "강원도 동해안에서는 계절마다 다른 생선이 올라옵니다. 찜, 구이, 조림, 탕으로 다양하게 먹습니다.",
 "대포항생선찜본점은 찜과 구이를 함께 드실 수 있는 생선 요리 전문점입니다.",
 L(A("gangwon-fish-gui","강원도 생선구이"), A("gangwon-fish-jjim","강원도 생선찜"), A("sokcho-fish-restaurant","속초 생선요리 전문점")), [SIZE, TOGO])

# ---------- 여행 동선 ----------
add("sokcho-before-checkin", "속초 체크인 전 식사", "상황별", "jjim-table.jpg",
 "체크인까지 시간이 남았다면, 대포항에서 한 끼.",
 [("체크인 전 시간 쓰기", "<p>속초에 일찍 도착하면 체크인 시간까지 애매하게 시간이 남습니다. 항구를 걷고 밥을 먹으면 딱 알맞습니다.</p>"),
  ("대포항 코스", f"<p>대포항 산책 → 대포항생선찜본점에서 식사 → 숙소 체크인. {A('daepohang-course','대포항 구경 코스')}도 참고하세요.</p>"),
  ("가게 정보", SHOP)],
 [PARK, SIZE])
add("sokcho-after-checkout", "속초 체크아웃 후 점심", "상황별", "jjim-closeup.jpg",
 "체크아웃하고 출발 전, 든든한 점심 한 끼.",
 [("출발 전 점심", "<p>체크아웃 후 짐을 싣고 바로 출발하기보다, 든든하게 먹고 출발하면 긴 운전이 편합니다.</p>"),
  ("포장도 됩니다", f"<p>집에서 먹을 찜이나 순대를 포장해 가는 분도 많습니다. {A('brand-takeout','포장 안내')}를 참고하세요.</p>"),
  ("가게 정보", SHOP)],
 [TOGO, PARK])
