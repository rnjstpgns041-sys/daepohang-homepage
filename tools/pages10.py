# 50 more keyword pages (added 2026-10-19). Same shape as pages2-9.
# High-volume heads: region/travel heads (강원도, 강릉, 양양), seasonal food and trips, fish dish names,
# and famous Sokcho foods the shop does not sell (say so plainly, then point to what it does serve).
# Store facts only from the listing / photos; area facts kept general (no distances, minutes or exit names).
# Opening hours are unconfirmed, so pages point to the phone instead of stating times.
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
NOTSOLD = lambda dish: (f"{dish}도 파나요?", "아니요. 생선찜, 생선구이, 순대 전문점입니다.")
SHOP = f"<p>대포항생선찜본점은 속초시 대포항길 10, 대포항 안쪽 상가 1층에 있습니다. 매주 수요일은 쉬고, 전 메뉴 포장됩니다. 전화 {TEL}.</p>"

# ---------- 속초 명물이지만 이 집에는 없는 메뉴 ----------
def notsold(slug, kw, dish, img, lede, about, instead, more):
    add(slug, kw, "메뉴", img, lede,
     [(f"{dish}, 이런 음식", f"<p>{about}</p>"),
      (f"{dish} 대신 생선찜은 어떠세요", f"<p>대포항생선찜본점에서는 {dish}{'을' if (ord(dish[-1])-0xAC00)%28 else '를'} 팔지 않습니다. {instead}</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [NOTSOLD(dish), TOGO])

notsold("sokcho-agujjim", "속초 아구찜", "아구찜", "jjim-table.jpg",
 "속초에서 아구찜이 생각난다면, 비슷하게 매콤한 생선찜도 있어요.",
 "아구찜은 아귀를 콩나물, 미나리와 함께 매콤하게 쪄 낸 음식입니다. 살이 부드럽고 껍질과 내장의 쫄깃한 식감 때문에 찾는 분이 많습니다.",
 f"매콤한 양념에 콩나물을 곁들인 찜을 좋아하신다면 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이나 {A('sokcho-gaori-jjim','가오리찜')}이 잘 맞습니다. 대구뽈찜의 말랑한 껍질과 쫀득한 볼살은 아구찜을 좋아하는 분들이 특히 반깁니다.",
 L(A("sokcho-jjim-matjip","속초 찜 맛집"), A("fish-jjim-matjip","생선찜 맛집"), A("daegu-ppol-vs-gaori","대구뽈찜 가오리찜 비교")))

notsold("sokcho-mulhoe", "속초 물회", "물회", "storefront.jpg",
 "속초 물회 먹으러 가는 길, 따뜻한 한 끼가 필요할 때.",
 "물회는 잘게 썬 회를 새콤달콤한 육수에 말아 먹는 음식입니다. 동해안 항구마다 물회 집이 있고, 여름에 특히 많이 찾습니다.",
 f"찬 음식보다 따뜻한 밥이 당기는 날이나 날것을 못 드시는 일행이 있다면 생선찜과 생선구이가 좋은 대안입니다. 맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}는 아이들도 잘 먹습니다.",
 L(A("daepohang-not-hoe","대포항 회 말고 먹을거"), A("sokcho-hoetjip","속초 횟집"), A("sokcho-seafood","속초 해산물 맛집")))

notsold("sokcho-daege", "속초 대게", "대게", "storefront.jpg",
 "대게는 부담스럽고 바다 음식은 먹고 싶을 때.",
 "대게는 겨울부터 봄까지 동해안에서 많이 찾는 게입니다. 다리살을 쪄서 먹고, 남은 내장에 밥을 볶아 마무리하는 것이 보통입니다.",
 f"대게 가격이 부담스럽거나 일행 중 게를 안 드시는 분이 있다면 생선찜 한 냄비가 든든합니다. 찜은 소(2인), 중(3인), 대(4인)로 인원에 맞춰 고를 수 있습니다.",
 L(A("sokcho-gaseongbi","속초 가성비 맛집"), A("sokcho-seafood","속초 해산물 맛집"), A("sokcho-must-eat","속초 꼭 먹어야 할 음식")))

notsold("sokcho-makguksu", "속초 막국수", "막국수", "storefront.jpg",
 "막국수로 가볍게 먹었다면, 다음 끼니는 생선찜으로.",
 "막국수는 메밀면을 동치미 국물이나 양념에 비벼 먹는 강원도 대표 음식입니다. 속초, 양양, 고성 곳곳에 오래된 막국수 집이 있습니다.",
 f"막국수가 가벼운 한 끼라면 생선찜은 밥 한 공기를 비우는 든든한 한 끼입니다. 여행 일정에 둘을 나눠 넣어 보세요.",
 L(A("gangwon-matjip","강원도 맛집"), A("sokcho-local-food","속초 현지 음식"), A("sokcho-must-eat","속초 꼭 먹어야 할 음식")))

notsold("sokcho-gomchiguk", "속초 곰치국", "곰치국", "jjim-closeup.jpg",
 "속초 겨울 해장 음식, 곰치국과 함께 알아두면 좋은 생선 요리.",
 "곰치국은 물곰(곰치)을 묵은지와 함께 끓인 국입니다. 살이 흐물흐물할 만큼 부드럽고 국물이 시원해서 속초에서는 해장 음식으로 유명합니다.",
 f"국물보다 밥반찬이 필요하다면 양념이 밴 {A('sokcho-kodari-jjim','코다리찜')}이나 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}을 드셔 보세요. 겨울에 특히 많이 찾는 메뉴입니다.",
 L(A("sokcho-haejang","속초 해장"), A("donghae-winter-fish","동해 겨울 생선"), A("sokcho-winter-matjip","속초 겨울 맛집")))

# ---------- 메뉴 / 생선 정보 ----------
add("kodari-jorim", "코다리조림", "메뉴", "jjim-closeup.jpg",
 "꾸덕한 코다리에 양념이 배어드는 맛. 코다리조림과 코다리찜 이야기.",
 [("코다리조림은", "<p>코다리조림은 반쯤 말린 명태를 무와 함께 양념에 졸인 음식입니다. 생태보다 살이 단단해 오래 졸여도 부서지지 않고, 양념이 속까지 뱁니다.</p>"),
  ("조림과 찜의 차이", f"<p>조림은 국물을 바짝 졸이고, 찜은 자작한 양념에 콩나물이나 채소를 더해 쪄 냅니다. 대포항생선찜본점의 {A('sokcho-kodari-jjim','코다리찜')}은 매콤달콤한 양념에 밥을 비벼 먹기 좋게 냅니다.</p>"),
  ("더 보기", L(A("kodari-jjim-recipe","코다리찜 레시피"), A("kodari-jjim-matjip","코다리찜 맛집"), A("saengseon-jjim-vs-jorim","생선찜 생선조림 차이")))],
 [SIZE, TOGO])

add("fish-jorim-matjip", "생선조림 맛집", "메뉴", "jjim-table.jpg",
 "생선조림이 생각날 때, 속초 대포항에서 먹는 생선찜.",
 [("생선조림이 맛있는 이유", "<p>생선조림은 무를 깔고 생선을 올려 간장이나 고추 양념에 졸이는 음식입니다. 생선살보다 양념이 밴 무를 더 좋아하는 분도 많습니다.</p>"),
  ("대포항생선찜본점에서는", f"<p>이 집은 조림보다 자작한 찜에 가깝게 냅니다. 무와 생선에 양념이 깊게 배어 있어 조림을 좋아하는 분들도 잘 드십니다. 여러 생선을 한 번에 맛보려면 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}을 고르세요.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-jorim","속초 생선조림"), A("saengseon-jjim-mu","생선찜 무"), A("fish-jjim-matjip","생선찜 맛집")))],
 [SIZE, TOGO])

add("haemul-jjim-matjip", "해물찜 맛집", "메뉴", "jjim-table.jpg",
 "해물찜처럼 푸짐하게, 생선으로 채운 찜 한 냄비.",
 [("해물찜과 생선찜", "<p>해물찜은 꽃게, 새우, 오징어, 조개 같은 해산물을 콩나물과 함께 매콤하게 쪄 냅니다. 생선찜은 생선살을 중심으로 무와 양념을 더해 밥반찬에 가깝습니다.</p>"),
  ("이 집의 찜", f"<p>대포항생선찜본점은 해물찜이 아니라 생선찜 전문점입니다. 매콤한 찜을 여럿이 나눠 먹고 싶다면 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')} 대(4인)를 추천합니다.</p>"),
  ("추천 메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-jjim-matjip","속초 찜 맛집"), A("jjim-kinds","생선찜 종류"), A("sokcho-agujjim","속초 아구찜")))],
 [NOTSOLD("해물찜"), SIZE])

add("jjim-kinds", "생선찜 종류", "메뉴", "jjim-closeup.jpg",
 "가오리, 코다리, 대구뽈, 모듬. 생선찜 종류별로 맛이 이렇게 달라요.",
 [("종류별 맛", L(f"{A('sokcho-gaori-jjim','가오리찜')}: 쫀득한 살과 오독한 연골. 가장 많이 찾는 대표 메뉴입니다.",
                  f"{A('sokcho-kodari-jjim','코다리찜')}: 반쯤 말린 명태라 쫄깃하고 양념이 잘 뱁니다.",
                  f"{A('sokcho-daegu-ppol-jjim','대구뽈찜')}: 대구 볼살과 껍질의 말랑하고 쫀득한 맛.",
                  f"{A('sokcho-saengseon-modeum-jjim','생선모듬찜')}: 여러 생선을 한 냄비에 담아 골라 먹는 재미가 있습니다.")),
  ("처음이라면", "<p>무엇을 고를지 모르겠다면 가오리찜이나 생선모듬찜으로 시작해 보세요. 찜은 모두 소(2인), 중(3인), 대(4인)로 주문합니다.</p>"),
  ("더 보기", L(A("jjim-size-guide","생선찜 사이즈 고르기"), A("modeum-or-gaori","생선모듬찜 가오리찜 고르기"), A("saengseon-jjim-first-time","생선찜 처음 먹는다면")))],
 [SIZE, TOGO])

add("myeongtae-dishes", "명태 요리", "메뉴", "jjim-closeup.jpg",
 "생태, 동태, 황태, 코다리. 명태로 만드는 요리 정리.",
 [("말린 정도에 따라 달라요", L("생태: 잡은 그대로. 맑은 탕으로 끓입니다.", "동태: 얼린 명태. 찌개와 전에 많이 씁니다.", "황태: 겨우내 얼었다 녹으며 마른 명태. 해장국, 구이로 먹습니다.", "코다리: 반쯤 말린 명태. 찜과 조림에 가장 잘 맞습니다.")),
  ("속초에서 먹는 명태", f"<p>명태는 예전부터 강원도 동해안의 대표 생선이었습니다. 대포항생선찜본점에서는 {A('sokcho-kodari-jjim','코다리찜')}으로 드실 수 있습니다.</p>"),
  ("더 보기", L(A("myeongtae-names","명태 이름 정리"), A("kodari-jorim","코다리조림"), A("kodari-benefits","코다리 효능")))],
 [("코다리찜 사이즈는?","소(2인), 중(3인), 대(4인)입니다."), TOGO])

add("gaori-benefits", "가오리 효능", "메뉴", "gaori-jjim.jpg",
 "쫀득한 가오리, 어떤 점이 좋을까요?",
 [("가오리는 이런 생선", "<p>가오리는 몸이 납작하고 뼈 대신 연골이 있는 생선입니다. 살은 단백질이 많고 기름기가 적은 편이며, 오독오독 씹히는 연골도 함께 먹습니다.</p>"),
  ("맛있게 먹는 방법", f"<p>가오리는 찜으로 먹을 때 가장 인기가 많습니다. 꾸덕하게 말린 가오리를 양념에 쪄 내면 살은 쫀득하고 연골은 고소합니다. 대포항생선찜본점의 대표 메뉴가 {A('sokcho-gaori-jjim','가오리찜')}입니다.</p>"),
  ("알아두세요", "<p>음식은 약이 아닙니다. 건강 상태에 따라 드시는 양은 의사와 상의하세요.</p>"),
  ("더 보기", L(A("gaori-vs-hongeo","가오리 홍어 차이"), A("gaori-jjim-taste","가오리찜 맛"), A("gaori-yeongol","가오리 연골")))],
 [("홍어처럼 냄새 나나요?","아니요. 삭히지 않은 가오리라 냄새가 없습니다."), SIZE])

add("kodari-benefits", "코다리 효능", "메뉴", "jjim-closeup.jpg",
 "반쯤 말린 명태, 코다리는 어떤 점이 좋을까요?",
 [("코다리는 이런 생선", "<p>코다리는 명태를 반쯤 말린 것입니다. 수분이 빠지면서 살이 단단해지고 맛이 진해집니다. 기름기가 적은 흰살생선이라 담백합니다.</p>"),
  ("맛있게 먹는 방법", f"<p>코다리는 양념에 졸이거나 쪄 먹을 때 가장 맛있습니다. 대포항생선찜본점의 {A('sokcho-kodari-jjim','코다리찜')}은 양념에 밥을 비벼 먹는 손님이 많습니다.</p>"),
  ("알아두세요", "<p>음식은 약이 아닙니다. 건강 상태에 따라 드시는 양은 의사와 상의하세요.</p>"),
  ("더 보기", L(A("myeongtae-dishes","명태 요리"), A("kodari-jorim","코다리조림"), A("kodari-jjim-taste","코다리찜 맛")))],
 [SIZE, TOGO])

def gui_info(slug, kw, fish, about, season):
    add(slug, kw, "메뉴", "gui.jpg",
     f"노릇하게 구운 {fish}. 맛있게 굽는 법과 속초에서 먹는 생선구이.",
     [(f"{fish}는", f"<p>{about}</p>"),
      ("맛있게 굽는 법", L("굽기 전에 물기를 키친타월로 닦습니다.", "팬을 충분히 달군 뒤 기름을 두르고 껍질 쪽부터 굽습니다.", "자주 뒤집지 말고 한쪽이 노릇해지면 한 번만 뒤집습니다.")),
      ("속초에서 먹는다면", f"<p>대포항생선찜본점의 {A('sokcho-saengseon-gui','모듬생선구이')}는 그날 들어온 여러 생선을 함께 구워 냅니다. {season} 어떤 생선이 들어가는지는 전화({TEL})로 물어보세요.</p>"),
      ("더 보기", L(A("saengseon-gui-kinds","생선구이 종류"), A("fish-gui-frypan","생선구이 프라이팬"), A("fish-gui-matjip","생선구이 맛집")))],
     [("모듬생선구이는 매운가요?","아니요. 맵지 않아 아이들도 잘 먹습니다."), TOGO])

gui_info("gajami-gui", "가자미구이", "가자미",
 "가자미는 몸이 납작하고 살이 얇은 흰살생선입니다. 구우면 살이 부드럽고 담백해서 생선구이로 가장 흔히 먹습니다. 동해안에서는 참가자미, 물가자미가 많이 잡힙니다.",
 "구성은 계절과 그날 들어온 생선에 따라 달라집니다.")
gui_info("imyeonsu-gui", "임연수구이", "임연수",
 "임연수는 동해안에서 많이 잡히는 생선으로, 껍질이 고소하고 살이 두툼합니다. 강원도에서는 ‘껍질 맛에 먹는 생선’이라고 할 만큼 구이로 사랑받습니다.",
 "임연수가 들어가는 날도 있지만 매일 같지는 않습니다.")
gui_info("godeungeo-gui", "고등어구이", "고등어",
 "고등어는 기름이 많은 등푸른생선입니다. 구우면 껍질은 바삭하고 살은 촉촉해서 밥반찬으로 가장 친숙한 생선구이입니다.",
 "구성은 계절과 그날 들어온 생선에 따라 달라집니다.")

add("sokcho-yangmiri", "속초 양미리", "제철", "gui.jpg",
 "찬바람 불면 속초 항구에 양미리가 올라옵니다.",
 [("양미리는", "<p>양미리는 늦가을부터 겨울까지 동해안에서 많이 잡히는 작고 길쭉한 생선입니다. 속초에서는 연탄불이나 석쇠에 통째로 구워 먹는 것이 대표적이고, 조림으로도 먹습니다.</p>"),
  ("양미리 철 속초 여행", "<p>이맘때 속초 항구 주변에는 양미리를 손질하고 굽는 풍경을 볼 수 있습니다. 항구 구경 뒤에는 따뜻한 생선 요리로 한 끼를 채워 보세요.</p>"),
  ("대포항생선찜본점에서는", f"<p>{A('sokcho-saengseon-gui','모듬생선구이')}는 그날 들어온 생선으로 구성합니다. 양미리가 들어가는지는 전화({TEL})로 확인해 주세요. 찜이 당기면 {A('sokcho-gaori-jjim','가오리찜')}을 추천합니다.</p>"),
  ("더 보기", L(A("dorumuk-season","도루묵 제철"), A("donghae-winter-fish","동해 겨울 생선"), A("sokcho-jecheol-saengseon","속초 제철 생선")))],
 [("양미리 단품이 있나요?",f"매일 같지 않으니 전화({TEL})로 물어봐 주세요."), TOGO])

add("sokcho-ojingeo", "속초 오징어", "메뉴", "squid-sundae.jpg",
 "속초 하면 오징어. 오징어순대부터 오징어 요리까지.",
 [("속초와 오징어", "<p>속초는 오래전부터 오징어잡이 배가 드나드는 항구였습니다. 그래서 오징어회, 오징어순대, 오징어 튀김처럼 오징어로 만든 먹거리가 많습니다.</p>"),
  ("이 집의 오징어 요리", f"<p>대포항생선찜본점에서는 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}(17,000원)를 드실 수 있습니다. 오징어 속에 찹쌀과 채소를 채워 겉을 누룽지처럼 바삭하게 지져 냅니다.</p>"),
  ("더 보기", L(A("sokcho-ojingeo-sundae","속초 오징어순대"), A("ojingeo-sundae-story","오징어순대 이야기"), A("squid-sundae-taste","오징어순대 맛")))],
 [NOTSOLD("오징어회"), TOGO])

add("sundae-matjip", "순대 맛집", "메뉴", "abai-sundae.jpg",
 "흔한 순대 말고, 속초에서 먹는 오징어순대와 아바이순대.",
 [("속초 순대는 다릅니다", "<p>속초 순대는 북쪽에서 내려온 실향민들의 음식에서 시작했습니다. 돼지 창자에 찹쌀과 채소를 넉넉히 채운 아바이순대, 오징어 몸통에 속을 채운 오징어순대가 대표적입니다.</p>"),
  ("이 집에서는", f"<p>{A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}와 {A('sokcho-abai-sundae','속초 아바이순대')}를 함께 드실 수 있습니다. 찜과 곁들이면 한 상이 완성됩니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sundae-kinds","순대 종류"), A("ojingeo-vs-abai-sundae","오징어순대 아바이순대 차이"), A("sokcho-sundae-matjip","속초 순대 맛집")))],
 [("순대도 포장되나요?","네, 전 메뉴 포장됩니다."), KIDS])

add("sundae-kinds", "순대 종류", "메뉴", "abai-sundae.jpg",
 "찹쌀순대, 아바이순대, 오징어순대, 피순대. 순대 종류 정리.",
 [("지역마다 다른 순대", L("찹쌀순대: 당면과 찹쌀을 넣은 가장 흔한 순대.", "아바이순대: 굵은 창자에 찹쌀, 채소, 선지를 넉넉히 채운 함경도식 순대. 속초가 유명합니다.", "오징어순대: 오징어 몸통에 속을 채워 쪄 낸 뒤 달걀옷을 입혀 부칩니다.", "피순대: 선지를 많이 넣어 진한 맛을 내는 순대.")),
  ("속초에서 맛보려면", f"<p>대포항생선찜본점에서는 {A('sokcho-abai-sundae','아바이순대')}와 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 드실 수 있습니다.</p>"),
  ("더 보기", L(A("abai-sundae-story","아바이순대 이야기"), A("ojingeo-sundae-how-made","오징어순대 만드는 법"), A("sundae-matjip","순대 맛집")))],
 [TOGO])

add("fish-dish-kinds", "생선 요리 종류", "메뉴", "jjim-table.jpg",
 "찜, 구이, 조림, 탕. 생선 요리 종류와 고르는 법.",
 [("조리법별 생선 요리", L("찜: 자작한 양념에 쪄 내 밥반찬으로 좋습니다.", "구이: 껍질은 바삭, 살은 촉촉. 맵지 않아 아이도 잘 먹습니다.", "조림: 국물을 바짝 졸여 양념이 진합니다.", "탕: 맑게 또는 맵게 끓여 국물로 먹습니다.")),
  ("한 상에 두 가지", f"<p>여럿이 간다면 매콤한 찜 하나와 맵지 않은 구이 하나를 함께 시키면 모두 만족하기 쉽습니다. 대포항생선찜본점에서는 {A('sokcho-gaori-jjim','가오리찜')}과 {A('sokcho-saengseon-gui','모듬생선구이')} 조합이 인기입니다.</p>"),
  ("더 보기", L(A("jjim-kinds","생선찜 종류"), A("saengseon-gui-kinds","생선구이 종류"), A("jjim-or-gui","생선찜 생선구이 고르기")))],
 [KIDS, TOGO])

add("family-dining-menu", "가족 외식 메뉴 추천", "상황별", "jjim-table.jpg",
 "아이부터 부모님까지, 다 같이 먹기 좋은 외식 메뉴.",
 [("가족 외식 메뉴 고르는 법", L("맵지 않은 메뉴가 하나는 있어야 아이가 편합니다.", "부모님은 밥반찬이 되는 메뉴를 좋아하십니다.", "나눠 먹는 큰 냄비 메뉴가 있으면 주문이 쉬워집니다.")),
  ("생선 한 상이 좋은 이유", f"<p>생선찜은 가운데 두고 나눠 먹기 좋고, {A('sokcho-saengseon-gui','모듬생선구이')}는 맵지 않아 아이가 먹기 좋습니다. 대포항생선찜본점에는 아기 의자도 있습니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-family-dining","속초 가족 외식"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리"), A("sokcho-three-generations","3대 가족 속초 식사")))],
 [KIDS, SIZE])

# ---------- 속초 / 대포항 넓은 키워드 ----------
add("sokcho-trip", "속초 여행", "여행", "storefront.jpg",
 "바다, 설악산, 항구 먹거리. 속초 여행 한눈에 보기.",
 [("속초는 이런 곳", "<p>속초는 동해 바다와 설악산을 함께 즐길 수 있는 도시입니다. 해수욕장, 호수, 항구, 시장이 가까이 모여 있어 짧은 일정에도 여러 곳을 둘러볼 수 있습니다.</p>"),
  ("꼭 넣어 볼 일정", L(f"{A('sokcho-abai-village','아바이마을')}과 갯배", "속초관광수산시장 구경", "영금정이나 속초등대에서 바다 보기", f"{A('daepohang-attractions','대포항')} 산책과 생선 요리 한 끼")),
  ("먹거리", f"<p>속초 먹거리는 오징어순대, 아바이순대, 생선 요리, 닭강정이 대표적입니다. 대포항에서는 {A('sokcho-gaori-jjim','가오리찜')}과 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 한 번에 드실 수 있습니다.</p>"),
  ("더 보기", L(A("sokcho-1bak2il","속초 1박2일 코스"), A("sokcho-attractions","속초 가볼만한곳"), A("sokcho-food","속초 먹거리")))],
 [WHERE, PARK])

add("sokcho-things-to-do", "속초 놀거리", "여행", "storefront.jpg",
 "속초에서 뭐 하고 놀까? 바다부터 실내까지.",
 [("바다에서", L("해수욕장 산책과 모래놀이", "항구에서 고깃배 구경", "바다를 끼고 걷는 해안 산책로")),
  ("산과 호수에서", L("설악산 케이블카나 가벼운 산책", "영랑호, 청초호 둘레길 걷기")),
  ("날씨가 궂다면", f"<p>비가 오거나 추운 날에는 시장 구경과 실내 명소를 엮어 보세요. {A('sokcho-indoor','속초 실내 가볼만한곳')}에 정리해 두었습니다.</p>"),
  ("배고플 때", f"<p>대포항 쪽에서 놀았다면 대포항생선찜본점에서 생선찜으로 한 끼를 채우세요. 전 메뉴 포장도 됩니다.</p>"),
  ("더 보기", L(A("sokcho-attractions","속초 가볼만한곳"), A("sokcho-kids-gabolmanhan","속초 아이랑 가볼만한곳"), A("sokcho-trip","속초 여행")))],
 [KIDS, PET])

add("sokcho-stay-guide", "속초 숙소 추천", "여행", "storefront.jpg",
 "속초 숙소, 어느 쪽에 잡을까? 동네별로 고르는 법.",
 [("동네별 특징", L("속초해수욕장 주변: 바다와 시내가 가까워 뚜벅이 여행에 편합니다.", "대포항, 외옹치 쪽: 항구 먹거리와 바다 산책로가 가깝습니다.", "설악산 쪽: 등산이나 케이블카 일정이 있을 때 좋습니다.", "영랑호, 장사항 쪽: 조용하게 쉬고 싶을 때 좋습니다.")),
  ("고를 때 볼 것", L("차가 있는지, 주차가 되는지", "다음 날 일정과 가까운지", "저녁을 먹으러 나가기 편한지")),
  ("숙소에서 먹는 저녁", f"<p>숙소에서 편하게 먹고 싶다면 포장도 좋습니다. 대포항생선찜본점은 전 메뉴 포장됩니다. {A('sokcho-stay-in-dinner','숙소에서 먹는 저녁')}도 참고하세요.</p>"),
  ("더 보기", L(A("daepohang-stay","대포항 숙소"), A("daepohang-lodging-dinner","대포항 숙소 근처 식당"), A("sokcho-1bak2il","속초 1박2일 코스")))],
 [TOGO, PET])

add("sokcho-jungang-market", "속초 중앙시장", "주변", "storefront.jpg",
 "속초 중앙시장(관광수산시장) 구경하고 생선 한 끼.",
 [("속초 중앙시장은", "<p>속초 중앙시장은 지금의 속초관광수산시장을 부르는 옛 이름입니다. 닭강정, 오징어순대, 건어물, 젓갈 가게가 모여 있어 여행객이 가장 많이 들르는 곳 중 하나입니다.</p>"),
  ("시장 구경 팁", L("주말과 휴가철에는 사람이 많으니 이른 시간이 편합니다.", "포장 먹거리는 숙소에서 먹을 만큼만 사세요.", "근처 공영주차장을 이용하세요.")),
  ("앉아서 먹는 한 끼", f"<p>시장 음식은 대부분 서서 먹거나 포장입니다. 앉아서 밥 한 끼를 하고 싶다면 대포항으로 내려와 생선찜을 드셔 보세요.</p>"),
  ("더 보기", L(A("sokcho-tourist-market-matjip","속초관광수산시장 근처 맛집"), A("sokcho-dakgangjeong","속초 닭강정"), A("sokcho-food","속초 먹거리")))],
 [WHERE, PARK])

add("sokcho-abai-village", "속초 아바이마을", "주변", "abai-sundae.jpg",
 "실향민이 일군 마을, 아바이마을과 아바이순대.",
 [("아바이마을은", "<p>아바이마을은 한국전쟁 때 북쪽에서 내려온 실향민들이 모여 살며 생긴 마을입니다. 청호동 바닷가에 있고, 갯배를 타고 건너는 풍경으로 유명합니다.</p>"),
  ("둘러보기", L("갯배를 타고 건너 보기", "마을 골목과 바닷가 산책", "실향민 음식인 아바이순대 맛보기")),
  ("아바이순대를 대포항에서", f"<p>대포항생선찜본점에서도 {A('sokcho-abai-sundae','속초 아바이순대')}를 드실 수 있습니다. 생선찜과 함께 시키면 속초 음식을 한 상에 모두 맛볼 수 있습니다.</p>"),
  ("더 보기", L(A("abai-village-matjip","아바이마을 근처 맛집"), A("abai-sundae-story","아바이순대 이야기"), A("sokcho-silhyangmin-food","속초 실향민 음식")))],
 [TOGO, WHERE])

add("sokcho-matjip-best", "속초 맛집 베스트", "주변", "jjim-table.jpg",
 "속초에서 꼭 먹어 볼 음식, 메뉴별로 골랐어요.",
 [("메뉴별로 고르기", L("생선 요리: 찜, 구이, 조림", "순대: 오징어순대, 아바이순대", "간식: 닭강정, 튀김", "국물: 곰치국, 해장국", "면: 막국수")),
  ("생선 요리라면", f"<p>대포항생선찜본점은 생선찜, 생선구이, 순대를 한 곳에서 드실 수 있는 집입니다. 대표 메뉴는 {A('sokcho-gaori-jjim','가오리찜')}입니다.</p>"),
  ("추천 메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-matjip","속초 맛집"), A("sokcho-matjip-recommend","속초 맛집 추천"), A("sokcho-must-eat","속초 꼭 먹어야 할 음식")))],
 [WHERE, OFF])

add("daepohang-matjip-recommend", "대포항 맛집 추천", "대포항", "storefront.jpg",
 "대포항에서 회 말고 밥 한 끼, 생선찜 집을 추천해요.",
 [("대포항 먹거리", "<p>대포항은 회센터, 튀김골목, 생선 요리 집이 모여 있는 작은 항구입니다. 회를 먹지 않는 일행이 있거나 따뜻한 밥이 생각나면 생선찜과 생선구이가 좋습니다.</p>"),
  ("대포항생선찜본점", f"<p>대포항 안쪽 상가 1층, 노란색과 분홍색 네온 간판을 찾으세요. {A('sokcho-gaori-jjim','가오리찜')}, {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}, {A('sokcho-saengseon-gui','모듬생선구이')}, {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}가 있습니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("daepohang-matjip","대포항 맛집"), A("daepohang-hoe-center","대포항 회센터"), A("daepohang-parking","대포항 주차")))],
 [PARK, PET])

add("daepohang-hoe-center", "대포항 회센터", "대포항", "storefront.jpg",
 "대포항 회센터 구경하고, 회 말고 먹을 것도 알아두세요.",
 [("대포항 회센터는", "<p>대포항에는 수조에서 고른 생선을 바로 회로 떠 주는 가게들이 모여 있습니다. 회를 떠서 근처 식당에서 먹거나 포장해 가는 손님이 많습니다.</p>"),
  ("회를 못 먹는 일행이 있다면", f"<p>날것을 못 드시는 분이나 아이와 함께라면 익힌 생선 요리가 편합니다. 대포항생선찜본점의 {A('sokcho-saengseon-gui','모듬생선구이')}는 맵지 않고, {A('sokcho-gaori-jjim','가오리찜')}은 밥반찬으로 좋습니다.</p>"),
  ("더 보기", L(A("daepohang-hoetjip","대포항 횟집"), A("daepohang-not-hoe","대포항 회 말고 먹을거"), A("daepohang-twigim","대포항 튀김 먹고 식사")))],
 [NOTSOLD("회"), KIDS])

# ---------- 강원도 / 지역 넓은 키워드 ----------
add("gangneung-matjip", "강릉 맛집", "주변", "storefront.jpg",
 "강릉에서 속초로 올라가는 길, 생선찜 한 끼.",
 [("강릉 먹거리", "<p>강릉은 초당순두부, 장칼국수, 커피거리로 유명합니다. 강릉에서 하루를 보내고 북쪽으로 올라가는 여행이라면 속초에서 생선 요리를 넣어 보세요.</p>"),
  ("강릉에서 속초로", f"<p>강릉에서 바닷길을 따라 올라오면 속초 남쪽 끝인 대포항에 가장 먼저 닿습니다. 대포항생선찜본점에서 {A('sokcho-gaori-jjim','가오리찜')}으로 한 끼를 채우고 속초 여행을 시작하세요.</p>"),
  ("더 보기", L(A("gangneung-sokcho-trip","강릉 속초 여행"), A("jumunjin-matjip","주문진 여행 속초 맛집"), A("donghaean-matjip","동해안 맛집")))],
 [WHERE, PARK])

add("yangyang-course", "양양 여행 코스", "여행", "storefront.jpg",
 "서핑, 낙산사, 해변. 양양 여행 코스와 속초 저녁.",
 [("양양 하루 코스", L("오전: 낙산사와 의상대에서 바다 보기", "점심: 해변 카페나 막국수", "오후: 서핑 해변 구경이나 체험", "저녁: 북쪽으로 올라와 속초에서 식사")),
  ("양양에서 속초로", f"<p>양양 북쪽에서 속초 대포항까지는 바닷길로 이어집니다. 하루 일정을 마치고 대포항에서 생선찜으로 저녁을 드셔 보세요.</p>"),
  ("더 보기", L(A("yangyang-matjip","양양 맛집"), A("yangyang-gabolmanhan","양양 가볼만한곳"), A("sokcho-yangyang-course","속초 양양 여행 코스")))],
 [WHERE, TOGO])

add("gangwon-trip", "강원도 여행", "여행", "storefront.jpg",
 "바다 쪽 강원도 여행이라면, 속초를 꼭 넣어 보세요.",
 [("강원도는 둘로 나뉩니다", "<p>강원도 여행은 크게 산 쪽(춘천, 홍천, 평창, 인제)과 바다 쪽(고성, 속초, 양양, 강릉, 동해, 삼척)으로 나뉩니다. 바다 쪽은 해안도로를 따라 여러 도시를 이어서 여행하기 좋습니다.</p>"),
  ("속초가 좋은 이유", "<p>속초는 바다, 설악산, 시장, 항구가 가까이 모여 있어 짧게 머물러도 볼거리와 먹거리가 많습니다.</p>"),
  ("먹거리", f"<p>강원도 바다 여행에서 생선 요리는 빠질 수 없습니다. 속초 대포항에서는 {A('sokcho-gaori-jjim','가오리찜')}과 {A('sokcho-saengseon-gui','모듬생선구이')}를 드실 수 있습니다.</p>"),
  ("더 보기", L(A("gangwon-matjip","강원도 맛집"), A("gangwon-gabolmanhan","강원도 가볼만한곳"), A("sokcho-trip","속초 여행")))],
 [WHERE])

add("gangwon-gabolmanhan", "강원도 가볼만한곳", "여행", "storefront.jpg",
 "강원도 동해안 가볼만한곳, 북쪽부터 차례로.",
 [("바닷길 따라 북쪽부터", L("고성: 통일전망대, 화진포", "속초: 설악산, 아바이마을, 대포항", "양양: 낙산사, 서핑 해변", "강릉: 경포대, 안목 커피거리", "동해·삼척: 촛대바위, 해안 레일바이크")),
  ("일정 짜는 법", "<p>하루에 한두 도시씩 묶으면 무리가 없습니다. 속초는 가운데쯤이라 숙소를 잡고 위아래로 다니기 좋습니다.</p>"),
  ("속초에서 한 끼", f"<p>대포항생선찜본점은 속초 남쪽 대포항에 있습니다. 양양이나 강릉에서 올라올 때 들르기 좋습니다.</p>"),
  ("더 보기", L(A("gangwon-trip","강원도 여행"), A("sokcho-attractions","속초 가볼만한곳"), A("goseong-gabolmanhan","고성 가볼만한곳")))],
 [WHERE])

add("donghaean-trip", "동해안 여행", "여행", "storefront.jpg",
 "7번 국도 따라 동해안 여행, 어디서 먹고 쉴까.",
 [("동해안 여행의 매력", "<p>동해안은 해안도로를 따라 바다를 보며 달리는 것만으로도 여행이 됩니다. 항구마다 먹거리가 달라 들르는 재미가 있습니다.</p>"),
  ("코스 예시", L("1일차: 강릉, 주문진", "2일차: 양양, 속초 대포항", "3일차: 속초 시내, 고성")),
  ("속초에서는", f"<p>속초 대포항에 들르면 대포항생선찜본점에서 생선찜과 오징어순대를 드셔 보세요. 전 메뉴 포장도 됩니다.</p>"),
  ("더 보기", L(A("donghaean-matjip","동해안 맛집"), A("gangwon-trip","강원도 여행"), A("sokcho-drive","속초 드라이브 코스")))],
 [WHERE, TOGO])

add("gangwon-winter-trip", "강원도 겨울 여행", "여행", "storefront.jpg",
 "눈 덮인 산과 겨울 바다, 강원도 겨울 여행.",
 [("겨울 강원도", "<p>겨울 강원도는 산 쪽은 눈과 스키장, 바다 쪽은 맑은 겨울 바다와 제철 생선이 매력입니다. 동해안은 내륙보다 눈이 덜 쌓이는 날도 많아 바다 여행으로 좋습니다.</p>"),
  ("겨울에 먹을 것", f"<p>겨울 동해안은 도루묵, 양미리, 대구 같은 생선이 맛있는 때입니다. 따뜻한 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이나 {A('sokcho-kodari-jjim','코다리찜')}을 드셔 보세요.</p>"),
  ("준비물", L("두꺼운 겉옷과 장갑", "미끄럼 방지 신발", "눈 소식 확인")),
  ("더 보기", L(A("sokcho-winter-sea","속초 겨울바다 여행"), A("donghae-winter-fish","동해 겨울 생선"), A("winter-sea-trip","겨울 바다 여행지")))],
 [WHERE])

add("gangwon-1bak2il", "강원도 1박2일", "여행", "storefront.jpg",
 "강원도 1박2일, 바다 쪽으로 간다면 이렇게.",
 [("코스 예시", L("1일차 오전: 양양 낙산사", "1일차 오후: 속초 대포항 산책, 생선찜 저녁", "2일차 오전: 설악산 케이블카나 아바이마을", "2일차 오후: 시장 구경 후 출발")),
  ("숙소는 속초에", f"<p>속초에 숙소를 잡으면 위아래로 다니기 편합니다. {A('sokcho-stay-guide','속초 숙소 추천')}을 참고하세요.</p>"),
  ("더 보기", L(A("sokcho-1bak2il","속초 1박2일 코스"), A("gangwon-trip","강원도 여행"), A("gangwon-day-trip","강원도 당일치기")))],
 [WHERE, PARK])

add("gangwon-day-trip", "강원도 당일치기", "여행", "storefront.jpg",
 "하루에 다녀오는 강원도 바다, 속초 당일치기.",
 [("당일치기 요령", L("이른 아침에 출발해 막히는 시간을 피합니다.", "한 도시만 정해 동선을 짧게 잡습니다.", "점심이나 이른 저녁을 먹고 출발하면 돌아오는 길이 편합니다.")),
  ("속초 당일 코스", f"<p>속초 대포항 산책, 시장 구경, 바다 카페를 묶고 대포항생선찜본점에서 한 끼를 드시면 하루가 꽉 찹니다. 남은 음식은 포장해 가세요.</p>"),
  ("더 보기", L(A("sokcho-day-trip","속초 당일치기"), A("seoul-to-sokcho","서울에서 속초"), A("gangwon-1bak2il","강원도 1박2일")))],
 [TOGO, PARK])

add("gangwon-sea-trip", "강원도 바다 여행", "여행", "storefront.jpg",
 "강원도 바다 여행지와 바다 앞 생선 한 끼.",
 [("어느 바다로 갈까", L("조용한 바다: 고성 해변들", "볼거리 많은 바다: 속초해수욕장, 대포항", "서핑 바다: 양양 해변들", "산책하기 좋은 바다: 강릉 경포, 안목")),
  ("항구 먹거리", f"<p>바다 여행의 마무리는 항구 먹거리입니다. 속초 대포항에서는 {A('sokcho-gaori-jjim','가오리찜')}, {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 드실 수 있습니다.</p>"),
  ("더 보기", L(A("donghaean-trip","동해안 여행"), A("sokcho-beach-matjip","속초해수욕장 근처 맛집"), A("daepohang-walk","대포항 산책")))],
 [WHERE, PET])

add("gangwon-kids", "강원도 아이랑 가볼만한곳", "여행", "hall.jpg",
 "아이와 함께하는 강원도 바다 여행.",
 [("아이와 가기 좋은 곳", L("모래놀이하기 좋은 해수욕장", "항구에서 배 구경", "케이블카와 전망대", "날씨가 궂으면 실내 박물관과 아쿠아리움")),
  ("아이와 먹기 좋은 한 끼", f"<p>대포항생선찜본점에는 아기 의자가 있고, 맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}와 {A('sokcho-abai-sundae','아바이순대')}가 있어 아이와 함께 드시기 좋습니다.</p>"),
  ("더 보기", L(A("sokcho-kids-gabolmanhan","속초 아이랑 가볼만한곳"), A("sokcho-kids-matjip","속초 아이랑 맛집"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리")))],
 [KIDS])

add("gangwon-pet-trip", "강원도 애견동반 여행", "여행", "pet.jpg",
 "강아지와 함께 가는 강원도 바다 여행.",
 [("애견동반 여행 준비", L("숙소와 식당에 동반 가능한지 미리 확인", "배변 봉투, 물그릇, 목줄", "해변 출입 규정 확인")),
  ("함께 들어갈 수 있는 식당", f"<p>대포항생선찜본점은 반려동물과 함께 오실 수 있습니다. 다른 손님을 위해 목줄을 해 주세요.</p>"),
  ("더 보기", L(A("sokcho-pet-travel","속초 애견동반 여행"), A("sokcho-pet-friendly-restaurant","속초 애견동반 식당"), A("daepohang-pet-friendly","대포항 애견동반")))],
 [PET, TOGO])

add("gangwon-drive", "강원도 드라이브 코스", "여행", "storefront.jpg",
 "바다를 끼고 달리는 강원도 드라이브 코스.",
 [("추천 드라이브 길", L("강릉에서 속초까지 해안도로", "미시령이나 한계령을 넘어 속초로", "속초에서 고성까지 북쪽 해안길")),
  ("쉬어 가는 곳", f"<p>드라이브 중간에 대포항에 차를 세우고 항구를 걸어 보세요. 대포항생선찜본점에서 식사하시고, {A('daepohang-parking','대포항 공영주차장')}을 이용하시면 됩니다.</p>"),
  ("더 보기", L(A("sokcho-drive","속초 드라이브 코스"), A("daepohang-drive","대포항 드라이브"), A("misiryeong-matjip","미시령 넘어 속초 맛집")))],
 [PARK, TOGO])

# ---------- 계절 / 국내 여행 넓은 키워드 ----------
add("november-trip", "11월 국내 여행", "제철", "storefront.jpg",
 "늦가을 단풍 끝자락과 겨울 바다 사이, 11월 국내 여행.",
 [("11월 여행의 좋은 점", "<p>11월은 성수기가 지나 한적하고, 산에는 늦단풍이 남아 있고 바다에는 제철 생선이 올라오기 시작하는 때입니다.</p>"),
  ("11월 속초", f"<p>속초는 설악산 늦단풍과 바다를 함께 볼 수 있습니다. 찬바람이 불기 시작하면 따뜻한 {A('sokcho-kodari-jjim','코다리찜')}이나 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이 생각납니다.</p>"),
  ("더 보기", L(A("sokcho-november-matjip","11월 속초 맛집"), A("sokcho-november-trip","속초 11월 여행"), A("november-seasonal-food","11월 제철 음식")))],
 [WHERE])

add("december-trip", "12월 국내 여행", "제철", "storefront.jpg",
 "한 해의 끝, 겨울 바다 보러 가는 12월 국내 여행.",
 [("12월에 가기 좋은 곳", "<p>12월에는 겨울 바다, 해돋이 명소, 온천이 인기입니다. 동해안은 연말 해돋이를 미리 보러 가는 분도 많습니다.</p>"),
  ("12월 속초", f"<p>속초는 겨울 바다와 온천, 항구 먹거리를 함께 즐길 수 있습니다. 연말 모임이라면 큰 냄비 생선찜을 나눠 드셔 보세요.</p>"),
  ("더 보기", L(A("sokcho-december-matjip","12월 속초 맛집"), A("sokcho-year-end","속초 연말 여행"), A("december-seasonal-food","12월 제철 음식")))],
 [SIZE])

add("winter-sea-trip", "겨울 바다 여행지", "제철", "storefront.jpg",
 "겨울에 더 맑은 동해 바다, 겨울 바다 여행지.",
 [("겨울 동해 바다", "<p>겨울 동해 바다는 물빛이 맑고 파도가 시원합니다. 사람이 적어 조용히 걷기 좋고, 해돋이를 보기에도 좋은 계절입니다.</p>"),
  ("속초 겨울 바다", L("속초해수욕장 산책", "영금정에서 파도 보기", "대포항 항구 산책")),
  ("몸 녹이는 한 끼", f"<p>바닷바람에 언 몸은 뜨끈한 찜 한 냄비로 녹이세요. 대포항생선찜본점의 {A('sokcho-gaori-jjim','가오리찜')}을 추천합니다.</p>"),
  ("더 보기", L(A("sokcho-winter-sea","속초 겨울바다 여행"), A("gangwon-winter-trip","강원도 겨울 여행"), A("sokcho-winter-matjip","속초 겨울 맛집")))],
 [WHERE])

add("family-trip-korea", "국내 가족여행지 추천", "여행", "hall.jpg",
 "아이도 부모님도 좋아하는 국내 가족여행지.",
 [("가족여행지 고르는 법", L("이동 시간이 너무 길지 않은 곳", "아이가 놀 곳과 어른이 쉴 곳이 함께 있는 곳", "다 같이 먹을 메뉴가 있는 곳")),
  ("속초가 좋은 이유", "<p>속초는 바다, 산, 시장이 가까이 있어 이동이 짧고, 아이와 부모님 모두 즐길 거리가 있습니다.</p>"),
  ("가족 한 끼", f"<p>대포항생선찜본점은 아기 의자가 있고, 찜은 소·중·대로 인원에 맞춰 고를 수 있습니다. 맵지 않은 생선구이도 있습니다.</p>"),
  ("더 보기", L(A("sokcho-family-trip","속초 가족여행 코스"), A("family-dining-menu","가족 외식 메뉴 추천"), A("sokcho-three-generations","3대 가족 속초 식사")))],
 [KIDS, SIZE])

add("parents-trip-korea", "부모님 모시고 국내 여행", "여행", "jjim-table.jpg",
 "부모님과 함께 가기 좋은 바다 여행지와 식사.",
 [("부모님 여행 고르는 법", L("많이 걷지 않아도 되는 일정", "자리에 앉아 편하게 먹는 식사", "바다나 산 풍경을 가까이에서 보는 곳")),
  ("속초에서", "<p>속초는 차로 바다와 설악산을 쉽게 오갈 수 있어 부모님 여행지로 많이 찾습니다. 케이블카를 타면 산 풍경도 편하게 볼 수 있습니다.</p>"),
  ("부모님이 좋아하시는 메뉴", f"<p>밥반찬이 되는 생선찜은 부모님들이 특히 좋아하십니다. {A('sokcho-gaori-jjim','가오리찜')}이나 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}을 추천합니다.</p>"),
  ("더 보기", L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-mom-trip","엄마랑 속초 여행"), A("sokcho-hwangap","속초 환갑 식사")))],
 [SIZE, PARK])

add("couple-trip-korea", "국내 커플 여행지", "여행", "storefront.jpg",
 "둘이 떠나기 좋은 바다 도시, 속초 커플 여행.",
 [("커플 여행지로 속초", "<p>속초는 바다 산책로, 전망 좋은 카페, 야경이 예쁜 항구가 모여 있어 둘이 걷기 좋은 도시입니다.</p>"),
  ("코스 예시", L("오후: 바다 산책과 카페", "해질녘: 대포항 산책", "저녁: 2인 생선찜")),
  ("둘이 먹기 좋은 메뉴", f"<p>찜 소(2인)에 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 곁들이면 둘이 먹기 알맞습니다.</p>"),
  ("더 보기", L(A("sokcho-couple-trip","속초 커플 여행"), A("sokcho-date-course","속초 데이트 코스"), A("sokcho-jjim-2in","속초 2인 생선찜")))],
 [SIZE, TOGO])

def seasonal(slug, kw, month, foods, why, ours, more):
    add(slug, kw, "제철", "jjim-closeup.jpg",
     f"{month}에 맛있는 제철 음식, 바다 음식 위주로 정리했어요.",
     [(f"{month} 제철 음식", L(*foods)),
      ("제철이 맛있는 이유", f"<p>{why}</p>"),
      ("속초에서 맛보기", f"<p>{ours}</p>"),
      ("더 보기", more)],
     [TOGO, WHERE])

seasonal("november-seasonal-food", "11월 제철 음식", "11월",
 ["도루묵: 알이 꽉 차는 때", "양미리: 구이와 조림", "방어: 기름이 오르기 시작", "대구: 찬바람과 함께 살이 오름", "굴, 꼬막 같은 조개류"],
 "찬바람이 불면 생선은 추위를 견디려 살과 기름을 채웁니다. 그래서 늦가을부터 겨울까지 동해안 생선이 가장 맛있습니다.",
 f"대포항생선찜본점에서는 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}과 {A('sokcho-saengseon-gui','모듬생선구이')}로 이 계절 생선을 드실 수 있습니다.",
 L(A("dorumuk-season","도루묵 제철"), A("sokcho-yangmiri","속초 양미리"), A("sokcho-november-matjip","11월 속초 맛집")))

seasonal("december-seasonal-food", "12월 제철 음식", "12월",
 ["대구: 탕과 찜", "방어: 겨울 대표 회", "도루묵: 구이와 찌개", "곰치: 곰치국", "굴, 과메기"],
 "12월은 바닷물이 차가워지며 생선 살이 단단해지고 맛이 깊어지는 때입니다. 따뜻한 찜과 국물 요리가 잘 어울립니다.",
 f"추운 날에는 뜨끈한 {A('sokcho-daegu-ppol-jjim','대구뽈찜')}이나 {A('sokcho-kodari-jjim','코다리찜')}을 드셔 보세요.",
 L(A("donghae-winter-fish","동해 겨울 생선"), A("sokcho-december-matjip","12월 속초 맛집"), A("sokcho-gomchiguk","속초 곰치국")))

seasonal("winter-seasonal-food", "겨울 제철 음식", "겨울",
 ["대구, 명태: 찜과 탕", "도루묵, 양미리: 구이", "방어, 과메기", "굴, 꼬막, 가리비", "시금치, 무, 배추"],
 "겨울 무는 달고 단단해서 생선찜에 깔면 양념을 머금어 가장 맛있습니다. 겨울 생선과 겨울 무가 만나는 계절입니다.",
 f"대포항생선찜본점의 찜은 무를 넉넉히 깔아 냅니다. 겨울에는 {A('saengseon-jjim-mu','양념 밴 무')}까지 꼭 드셔 보세요.",
 L(A("sokcho-winter-matjip","속초 겨울 맛집"), A("donghae-winter-fish","동해 겨울 생선"), A("december-seasonal-food","12월 제철 음식")))

# 2026-10-19: owner asked to take these off the site; drop them and unlink them from the pages that stay.
REMOVED = {"sokcho-mulhoe","sokcho-daege","sokcho-makguksu","sokcho-gomchiguk","haemul-jjim-matjip","jjim-kinds",
 "myeongtae-dishes","gaori-benefits","kodari-benefits","gajami-gui","imyeonsu-gui","godeungeo-gui","sokcho-yangmiri",
 "sokcho-ojingeo","sundae-matjip","sundae-kinds","sokcho-things-to-do","sokcho-jungang-market","sokcho-abai-village",
 "daepohang-hoe-center","gangneung-matjip"}
import re as _re
def _unlink(html):
    for s in REMOVED:
        html = _re.sub(r'<li><a href="/%s/">[^<]*</a></li>' % s, '', html)
        html = _re.sub(r'<a href="/%s/">([^<]*)</a>' % s, r'\1', html)
    return html
P = [p for p in P if p["slug"] not in REMOVED]
for p in P:
    p["sections"] = [(h, _unlink(b)) for h, b in p["sections"]]
    p["faq"] = [(q, _unlink(a)) for q, a in p["faq"]]
