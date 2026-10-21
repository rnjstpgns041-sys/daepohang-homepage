# 50 keyword pages (added 2026-10-21), batch 501-550.
# Same goal as pages12: searches from people about to pick a restaurant. Shop-name + dish searches,
# open days, trip types and life events, taste worries (비린내, 가시, 회 못 먹음), 양양/고성 + dish, a few landmarks.
# No pages about dishes the shop doesn't sell. Store facts only from the listing / photos. Hours unconfirmed.
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
def j(w, a, b):
    return a if (ord(w[-1]) - 0xAC00) % 28 else b

# ---------- 가게 이름 + 메뉴 ----------
def brand_dish(slug, kw, dish, dish_slug, img, about, more):
    add(slug, kw, "대포항", img, f"대포항생선찜본점의 {dish}{j(dish,'을','를')} 소개해요.",
     [(dish, f"<p>{about}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", L(A(dish_slug, f"속초 {dish}"), *more))],
     [SIZE, TOGO])

brand_dish("brand-kodari-jjim", "대포항생선찜본점 코다리찜", "코다리찜", "sokcho-kodari-jjim", "jjim-closeup.jpg",
 "반쯤 말린 명태를 매콤달콤한 양념에 쪄 냅니다. 살이 쫄깃하고 양념이 속까지 배어 밥반찬으로 좋습니다. 소(2인), 중(3인), 대(4인).",
 [A("kodari-jjim-good","코다리찜 잘하는 집"), A("kodari-jjim-taste","코다리찜 맛")])
brand_dish("brand-daegu-ppol", "대포항생선찜본점 대구뽈찜", "대구뽈찜", "sokcho-daegu-ppol-jjim", "jjim-closeup.jpg",
 "대구 머리의 쫀득한 볼살과 말랑한 껍질을 콩나물과 함께 매콤하게 쪄 냅니다. 소(2인), 중(3인), 대(4인).",
 [A("daegu-ppol-good","대구뽈찜 잘하는 집"), A("daegu-ppol-taste","대구뽈찜 맛")])
brand_dish("brand-modeum-jjim", "대포항생선찜본점 생선모듬찜", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "여러 생선을 한 냄비에 담아 쪄 냅니다. 한 가지를 고르기 어려울 때 좋습니다. 소(2인), 중(3인), 대(4인).",
 [A("modeum-jjim-matjip","생선모듬찜 맛집"), A("modeum-jjim-guide","생선모듬찜 고르는 이유")])
brand_dish("brand-saengseon-gui", "대포항생선찜본점 생선구이", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 "그날 들어온 여러 생선을 노릇하게 구워 뜨거운 판에 냅니다. 맵지 않아 아이와 부모님도 잘 드십니다.",
 [A("fish-gui-good","생선구이 잘하는 집"), A("modeum-gui-taste","모듬생선구이 맛")])
brand_dish("brand-squid-sundae", "대포항생선찜본점 오징어순대", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg",
 "오징어 속을 꽉 채우고 겉을 누룽지처럼 바삭하게 지져 냅니다. 17,000원입니다.",
 [A("squid-sundae-good","오징어순대 잘하는 집"), A("daepohang-nurungji-sundae","대포항 누룽지 오징어순대")])
brand_dish("brand-abai-sundae", "대포항생선찜본점 아바이순대", "아바이순대", "sokcho-abai-sundae", "abai-sundae.jpg",
 "굵은 창자에 찹쌀과 채소, 선지를 꽉 채운 함경도식 순대입니다. 고추 장아찌를 곁들여 냅니다. 맵지 않습니다.",
 [A("abai-sundae-matjip","아바이순대 맛집"), A("abai-sundae-how-to-eat","아바이순대 먹는 법")])

add("brand-phone", "대포항생선찜본점 전화번호", "대포항", "storefront.jpg",
 "대포항생선찜본점 전화번호는 0507-1364-4060이에요.",
 [("전화번호", f'<p><a href="tel:050713644060">{TEL}</a> 를 누르면 바로 전화가 걸립니다.</p>'),
  ("전화로 할 수 있는 것", L("자리 문의, 여럿이 오실 때 미리 알리기", "포장 주문, 받아 갈 시간 정하기", "그날 생선구이 구성이나 영업시간 묻기")),
  ("가게 정보", SHOP)],
 [OFF, TOGO])
add("brand-kids", "대포항생선찜본점 아기의자", "대포항", "hall.jpg",
 "아기와 함께 와도 편한 대포항 생선찜집.",
 [("아이와 함께", f"<p>아기 의자가 있습니다. 아이 메뉴로는 맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}와 {A('sokcho-abai-sundae','아바이순대')}를 많이 시킵니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-baby-matjip","아기랑 속초 맛집"), A("daepohang-with-kids","대포항 아이랑"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리")))],
 [KIDS, PARK])
add("brand-group", "대포항생선찜본점 단체", "대포항", "hall2.jpg",
 "여럿이 오실 때, 미리 전화 주세요.",
 [("단체 식사", f"<p>모임, 가족 행사, 동호회처럼 여럿이 오신다면 미리 전화({TEL})로 인원과 시간을 알려 주세요. 찜은 대(4인)를 여러 개 시키거나 종류를 섞어 주문하시면 됩니다.</p>"),
  ("주문 예시", L("8명: 찜 대 2개 + 모듬생선구이", "10명: 찜 대 2개 + 찜 소 1개 + 모듬생선구이 + 누룽지 오징어순대")),
  ("가게 정보", SHOP)],
 [SIZE, PARK])

# ---------- 요일 · 날씨 · 때 ----------
def when(slug, kw, lede, about, tip, faq):
    add(slug, kw, "상황별", "jjim-table.jpg", lede,
     [("이럴 때", f"<p>{about}</p>"),
      ("대포항생선찜본점은", f"<p>{tip}</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP)],
     faq)

when("sokcho-thursday-matjip", "속초 목요일 맛집", "수요일 쉬고 목요일 다시 여는 생선찜집.",
 "목요일은 주말 여행을 하루 일찍 시작하는 분이 많은 날입니다.", "매주 수요일만 쉬고 목요일엔 문을 엽니다. 영업시간은 전화로 확인해 주세요.", [OFF, HOURS])
when("sokcho-saturday-lunch", "속초 토요일 점심", "토요일 점심, 붐비기 전에 대포항으로.",
 "토요일 점심에는 속초 시내와 항구가 가장 붐빕니다. 조금 일찍 오시거나 미리 전화해 두면 편합니다.", f"토요일에도 문을 엽니다. 포장 주문은 전화({TEL})로 미리 해 두세요.", [OFF, PARK])
when("sokcho-windy-day", "속초 바람 부는 날", "바닷바람 센 날, 실내에서 뜨끈한 찜.",
 "속초는 바닷바람이 센 날이 많습니다. 항구 산책은 짧게 하고 따뜻한 실내에서 쉬어 가세요.", "김이 오르는 생선찜 한 냄비면 몸이 금방 풀립니다.", [WHERE, TOGO])
when("sokcho-new-year-sunrise-meal", "속초 해돋이 후 식사", "해돋이 보고 언 몸 녹이는 한 끼.",
 "해돋이를 보려면 새벽부터 바닷가에서 기다리게 됩니다. 해가 뜨고 나면 따뜻한 밥이 간절해집니다.", f"아침 일찍 문을 여는지는 날마다 다를 수 있으니 전화({TEL})로 확인해 주세요. 점심 무렵이라면 든든한 찜이 좋습니다.", [HOURS, WHERE])
when("sokcho-winter-break", "속초 겨울방학 여행", "아이 겨울방학, 속초 바다 여행과 생선 한 끼.",
 "겨울방학에는 아이와 함께 바다와 눈을 보러 속초를 찾는 가족이 많습니다.", f"아기 의자가 있고 맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}가 있어 아이와 함께 드시기 좋습니다.", [KIDS, SIZE])
when("sokcho-day-off-trip", "속초 연차 여행", "연차 내고 평일 속초, 한적하게 먹고 쉬기.",
 "평일 속초는 주말보다 한적해서 식당도 여유롭습니다.", "수요일만 피하면 됩니다. 매주 수요일은 쉽니다.", [OFF, PARK])

# ---------- 누구와 · 무슨 일로 ----------
def who(slug, kw, img, lede, about, pick, more, faq):
    add(slug, kw, "상황별", img, lede,
     [("이런 여행", f"<p>{about}</p>"),
      ("이렇게 시켜 보세요", f"<p>{pick}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

who("sokcho-student-trip", "속초 대학생 여행", "jjim-table.jpg", "친구들과 속초, 나눠 먹는 생선찜 한 냄비.",
 "대학생 여행은 여럿이 함께 다니며 비용을 나누는 경우가 많습니다. 큰 냄비 하나를 나눠 먹는 메뉴가 잘 맞습니다.",
 "넷이면 찜 대(4인)에 공깃밥, 더 먹고 싶다면 누룽지 오징어순대를 더하세요.",
 L(A("sokcho-friends-trip","속초 친구여행 맛집"), A("sokcho-budget-trip","속초 여행 경비 아끼기"), A("sokcho-mt","속초 MT 식사")), [SIZE, TOGO])
who("sokcho-office-worker-trip", "속초 직장인 여행", "jjim-closeup.jpg", "주말 짧게 다녀오는 속초, 맛있게 먹고 쉬기.",
 "금요일 저녁에 출발해 일요일에 돌아오는 짧은 여행이라면 먹는 일정이 여행의 절반입니다.",
 "도착한 날 저녁엔 찜, 돌아가는 날엔 포장. 짧은 여행도 알차게 채울 수 있습니다.",
 L(A("sokcho-friday-dinner","속초 금요일 저녁"), A("sokcho-weekend-matjip","속초 주말 맛집"), A("sokcho-last-meal","속초 마지막 식사")), [TOGO, PARK])
who("sokcho-50s-couple", "속초 50대 부부 여행", "jjim-table.jpg", "둘이 떠나는 속초, 밥반찬 생선찜 한 상.",
 "아이들이 크고 둘이 떠나는 여행이 늘어나는 나이입니다. 많이 걷기보다 바다를 보며 쉬고, 잘 차린 밥을 먹는 일정이 좋습니다.",
 "찜 소(2인)에 모듬생선구이나 오징어순대를 곁들이면 둘이 먹기에 넉넉합니다.",
 L(A("sokcho-couple-trip","속초 커플 여행"), A("sokcho-healing-trip","속초 힐링 여행"), A("couple-trip-korea","국내 커플 여행지")), [SIZE, PARK])
who("sokcho-hyodo-trip", "속초 효도 여행", "jjim-table.jpg", "부모님 모시고 속초, 편하게 앉아 드시는 생선찜.",
 "효도 여행은 이동을 줄이고, 부모님 입맛에 맞는 식사를 고르는 것이 가장 중요합니다.",
 "밥반찬이 되는 가오리찜이나 생선모듬찜, 그리고 맵지 않은 생선구이를 함께 시키면 부모님들이 좋아하십니다.",
 L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("parents-trip-korea","부모님 모시고 국내 여행"), A("sokcho-three-generations","3대 가족 속초 식사")), [SIZE, PARK])
who("sokcho-palsun", "속초 팔순 가족 식사", "hall2.jpg", "팔순 맞은 부모님과 온 가족이 함께하는 식사.",
 "팔순 같은 큰 생신에는 온 가족이 모여 여행을 겸하기도 합니다. 어르신이 드시기 편한 부드러운 메뉴가 좋습니다.",
 f"부드러운 생선살의 찜과 맵지 않은 생선구이를 함께 시키세요. 인원이 많으면 미리 전화({TEL}) 주세요.",
 L(A("sokcho-chilsun","속초 칠순 가족 식사"), A("sokcho-hwangap","속초 환갑 식사"), A("brand-group","대포항생선찜본점 단체")), [SIZE, KIDS])
who("sokcho-retirement-trip", "속초 퇴직 기념 여행", "jjim-table.jpg", "긴 직장 생활을 마치고 떠나는 속초 여행.",
 "퇴직 기념 여행은 서두르지 않는 일정이 어울립니다. 평일에 떠나면 어디든 한적합니다.",
 "바다 산책 뒤 항구 앞에서 생선찜 한 상, 술 한잔 곁들이기 좋습니다.",
 L(A("sokcho-50s-couple","속초 50대 부부 여행"), A("sokcho-day-off-trip","속초 연차 여행"), A("sokcho-healing-trip","속초 힐링 여행")), [OFF, PARK])
who("sokcho-elementary-trip", "속초 초등학생 아이 여행", "hall.jpg", "초등학생 아이와 속초, 바다 구경하고 생선 한 끼.",
 "초등학생 아이들은 항구의 고깃배와 수조 구경을 좋아합니다. 걷는 거리가 짧은 대포항이 아이와 다니기 좋습니다.",
 "아이는 맵지 않은 모듬생선구이, 어른은 가오리찜으로 나눠 시키면 다 같이 즐길 수 있습니다.",
 L(A("sokcho-kids-gabolmanhan","속초 아이랑 가볼만한곳"), A("daepohang-with-kids","대포항 아이랑"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리")), [KIDS, SIZE])
who("sokcho-10-people", "속초 10명 식사", "hall2.jpg", "열 명이 함께 먹는 속초 생선찜 한 상.",
 "열 명 안팎의 모임은 자리를 미리 확인하는 것이 가장 중요합니다.",
 f"찜 대 2개와 소 1개, 모듬생선구이, 누룽지 오징어순대를 함께 시키면 알맞습니다. 미리 전화({TEL})로 인원을 알려 주세요.",
 L(A("sokcho-jjim-6in","속초 6인 이상 식사"), A("brand-group","대포항생선찜본점 단체"), A("sokcho-group-restaurant","속초 단체 식당")), [SIZE, PARK])
who("sokcho-winter-date", "속초 겨울 데이트", "storefront.jpg", "겨울 바다 보고, 항구 앞에서 둘이 먹는 찜.",
 "겨울 속초는 바다가 맑고 사람이 적어 둘이 걷기 좋습니다. 네온 간판이 켜진 저녁 항구도 분위기가 있습니다.",
 "찜 소(2인)에 누룽지 오징어순대를 곁들이면 둘이 먹기 알맞습니다.",
 L(A("sokcho-date-course","속초 데이트 코스"), A("sokcho-date-matjip","속초 데이트 맛집"), A("winter-sea-trip","겨울 바다 여행지")), [SIZE, TOGO])

# ---------- 입맛 걱정 ----------
def worry(slug, kw, img, lede, about, pick, more, faq):
    add(slug, kw, "메뉴", img, lede,
     [("걱정되신다면", f"<p>{about}</p>"),
      ("이 메뉴를 추천해요", f"<p>{pick}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

worry("sokcho-no-raw-fish", "속초 회 못 먹는 사람 맛집", "gui.jpg", "회를 못 먹어도 속초 바다 음식을 즐기는 법.",
 "속초 여행에서 일행 중 회를 못 드시는 분이 있으면 식당 고르기가 어려워집니다.",
 f"익힌 생선 요리라면 걱정 없습니다. {A('sokcho-saengseon-gui','모듬생선구이')}, {A('sokcho-gaori-jjim','가오리찜')}, {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')} 모두 익힌 음식입니다.",
 L(A("daepohang-not-hoe","대포항 회 말고 먹을거"), A("sokcho-what-to-eat","속초 뭐 먹지"), A("sokcho-fish-restaurant","속초 생선요리 전문점")), [("회도 파나요?","아니요. 생선찜, 생선구이, 순대 전문점입니다."), TOGO])
worry("sokcho-not-fishy", "비린내 안 나는 생선 요리", "jjim-closeup.jpg", "생선 비린내가 걱정이라면, 양념 찜부터.",
 "생선 비린내 때문에 생선 요리를 피하는 분이 많습니다. 양념에 쪄 내거나 바삭하게 구운 생선은 비린내 걱정이 덜합니다.",
 f"고춧가루와 마늘 양념에 쪄 낸 {A('sokcho-gaori-jjim','가오리찜')}은 생선을 잘 안 드시는 분도 편하게 드십니다. 삭히지 않아 홍어 같은 냄새도 없습니다.",
 L(A("gaori-vs-hongeo","가오리 홍어 차이"), A("saengseon-jjim-first-time","생선찜 처음 먹는다면"), A("sokcho-light-food","속초 담백한 음식")), [SIZE, TOGO])
worry("sokcho-boneless-fish", "가시 없는 생선 요리", "gaori-jjim.jpg", "생선 가시가 싫다면, 연골이 있는 가오리찜.",
 "생선 가시를 바르기 번거롭거나 아이가 걱정된다면 가시가 적은 메뉴를 고르세요.",
 f"가오리는 뼈 대신 부드러운 연골이 있어 통째로 씹어 먹습니다. {A('sokcho-gaori-jjim','가오리찜')}은 가시 걱정이 적은 메뉴입니다. 생선구이는 {A('saengseon-gasi-tip','가시 바르는 법')}을 참고하세요.",
 L(A("gaori-yeongol","가오리 연골"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리"), A("soft-fish-dish","부드러운 생선 요리")), [KIDS, SIZE])

# ---------- 술 ----------
worry("sokcho-makgeolli-anju", "속초 막걸리 안주", "squid-sundae.jpg", "막걸리 한 잔에 바삭한 오징어순대.",
 "막걸리에는 기름에 부친 전 같은 안주가 잘 어울립니다.",
 f"겉을 바삭하게 지진 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}가 막걸리와 잘 맞습니다. 매콤한 {A('sokcho-gaori-jjim','가오리찜')}도 좋습니다. 막걸리, 소주, 맥주, 청하, 백세주가 있습니다.",
 L(A("sokcho-suljip","속초 술집"), A("daepohang-anju","대포항 술안주"), A("jjim-sulanju","생선찜 술안주")), [HOURS, TOGO])
worry("sokcho-honsul", "속초 혼술", "jjim-closeup.jpg", "혼자 속초, 생선 안주에 한 잔.",
 "혼자 여행하다 보면 저녁에 한 잔 생각날 때가 있습니다. 혼자서도 시킬 수 있는 메뉴가 있는지가 중요합니다.",
 f"혼자라면 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}나 {A('sokcho-saengseon-gui','모듬생선구이')}에 술 한 병이 알맞습니다. 찜은 소(2인)부터라 남으면 포장해 가세요.",
 L(A("sokcho-honbap","속초 혼밥"), A("sokcho-solo-trip","속초 혼자 여행"), A("sokcho-suljip","속초 술집")), [HOURS, TOGO])
worry("yangyang-suljip", "양양 술집", "jjim-closeup.jpg", "양양 놀고 한잔은 속초 대포항에서.",
 "양양 해변 근처는 카페와 펍이 많지만, 밥과 함께 먹는 안주를 찾는다면 선택지가 줄어듭니다.",
 f"속초 대포항으로 올라와 매콤한 {A('sokcho-gaori-jjim','가오리찜')}에 소주 한 잔 하세요. 숙소가 가까우면 포장도 됩니다.",
 L(A("sokcho-suljip","속초 술집"), A("yangyang-dinner-matjip","양양 저녁 맛집"), A("yangyang-matjip","양양 맛집")), [WHERE, TOGO])

# ---------- 메뉴 정보 ----------
def info(slug, kw, img, lede, body, more, faq):
    add(slug, kw, "메뉴", img, lede, body + [("더 보기", more)], faq)

info("gaori-kongnamul", "가오리찜 콩나물", "gaori-jjim.jpg", "가오리찜에 콩나물이 빠지지 않는 이유.",
 [("콩나물의 역할", "<p>콩나물은 매콤한 양념을 부드럽게 해 주고, 아삭한 식감으로 쫀득한 가오리와 대비를 이룹니다. 양념이 밴 콩나물만 따로 찾는 분도 많습니다.</p>"),
  ("이렇게 드세요", "<p>가오리 살 한 점에 콩나물을 함께 집어 드세요. 마지막엔 남은 콩나물과 양념에 밥을 비벼도 좋습니다.</p>")],
 L(A("gaori-jjim-how-to-eat","가오리찜 맛있게 먹는 법"), A("saengseon-jjim-bibim","생선찜 양념 밥 비벼먹기"), A("brand-gaori-jjim","대포항생선찜본점 가오리찜")), [SIZE, TOGO])
info("kodari-jjim-spicy", "코다리찜 맵기", "jjim-closeup.jpg", "코다리찜, 얼마나 매울까요?",
 [("맵기", "<p>코다리찜 양념은 고춧가루로 칼칼하게 내지만 단맛이 함께 있어 맵기만 하지 않습니다. 매운 음식을 아주 못 드시는 분이 아니라면 대부분 잘 드십니다.</p>"),
  ("매운 게 걱정이라면", f"<p>맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}를 함께 시키세요.</p>")],
 L(A("kodari-jjim-taste","코다리찜 맛"), A("sokcho-mild-menu","속초 안 매운 메뉴"), A("gaori-jjim-spicy-level","가오리찜 맵기")), [KIDS, SIZE])
info("daegu-ppol-spicy", "대구뽈찜 맵기", "jjim-closeup.jpg", "대구뽈찜, 얼마나 매울까요?",
 [("맵기", "<p>대구뽈찜은 매콤한 양념에 콩나물과 함께 쪄 냅니다. 칼칼하지만 대구 살이 담백해서 맵기가 부드럽게 느껴집니다.</p>"),
  ("매운 게 걱정이라면", f"<p>밥과 함께 드시고, 맵지 않은 {A('sokcho-abai-sundae','아바이순대')}를 곁들이세요.</p>")],
 L(A("daegu-ppol-taste","대구뽈찜 맛"), A("daegu-ppol-how-to-eat","대구뽈찜 먹는 법"), A("kodari-jjim-spicy","코다리찜 맵기")), [KIDS, SIZE])
info("abai-sundae-taste", "아바이순대 맛", "abai-sundae.jpg", "굵고 고소한 아바이순대, 어떤 맛일까요?",
 [("맛", "<p>아바이순대는 찹쌀과 채소, 선지를 굵은 창자에 꽉 채워 쪄 낸 순대입니다. 찰지고 고소하며, 흔한 당면 순대보다 씹는 맛이 풍성합니다.</p>"),
  ("곁들이기", "<p>고추 장아찌나 새우젓을 곁들이면 느끼함 없이 드실 수 있습니다. 맵지 않아 아이도 잘 먹습니다.</p>")],
 L(A("abai-sundae-how-to-eat","아바이순대 먹는 법"), A("brand-abai-sundae","대포항생선찜본점 아바이순대"), A("ojingeo-vs-abai-sundae","오징어순대 아바이순대 차이")), [KIDS, TOGO])
info("jjim-storage", "생선찜 남은 거 보관", "jjim-table.jpg", "먹고 남은 생선찜, 이렇게 보관하세요.",
 [("보관", L("식힌 뒤 뚜껑 있는 그릇에 담아 냉장 보관합니다.", "되도록 다음 날 안에 드세요.", "다시 먹을 때는 냄비에 물을 조금 넣고 약불로 데웁니다.")),
  ("포장해 갈 때", "<p>먼 길을 가신다면 아이스박스에 담아 가세요.</p>")],
 L(A("saengseon-jjim-reheat","생선찜 포장 데우는 법"), A("brand-takeout","대포항생선찜본점 포장"), A("gaori-jjim-takeout","가오리찜 포장")), [TOGO])
info("squid-sundae-storage", "오징어순대 보관", "squid-sundae.jpg", "남은 오징어순대, 이렇게 보관하세요.",
 [("보관", L("한 김 식혀 랩이나 밀폐 용기에 담아 냉장 보관합니다.", "되도록 빨리 드세요.", "다시 먹을 때는 프라이팬에 약불로 앞뒤를 데워 겉을 바삭하게 살립니다.")),
  ("포장해 갈 때", "<p>먼 길을 가신다면 아이스박스에 담아 가세요.</p>")],
 L(A("squid-sundae-reheat","오징어순대 데우는 법"), A("ojingeo-sundae-takeout","오징어순대 포장"), A("brand-squid-sundae","대포항생선찜본점 오징어순대")), [TOGO])

# ---------- 양양 · 고성 + 메뉴 ----------
def town_dish(slug, kw, dish, dish_slug, img, about, more):
    town = kw.split()[0]
    add(slug, kw, "근처", img, f"{town} 여행 중 {dish}{j(dish,'이','가')} 생각나면, 속초 대포항으로.",
     [(f"{town}에서 {dish}", f"<p>{about}</p>"),
      ("대포항생선찜본점", f"<p>대포항은 속초 남쪽 끝이라 {town}에서 오가기 편합니다. {A(dish_slug, dish)}{j(dish,'을','를')} 비롯해 생선찜, 생선구이, 순대를 한 곳에서 드실 수 있습니다.</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, TOGO])

town_dish("yangyang-gaori-jjim", "양양 가오리찜", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg",
 "쫀득한 가오리찜은 강원도 바닷가에서 사랑받는 찜 요리입니다.", L(A("yangyang-saengseon-jjim","양양 생선찜"), A("gaori-jjim-matjip","가오리찜 맛집")))
town_dish("yangyang-kodari-jjim", "양양 코다리찜", "코다리찜", "sokcho-kodari-jjim", "jjim-closeup.jpg",
 "반쯤 말린 명태로 만든 코다리찜은 동해안 밥반찬의 대표입니다.", L(A("yangyang-saengseon-jjim","양양 생선찜"), A("kodari-jjim-matjip","코다리찜 맛집")))
town_dish("goseong-gaori-jjim", "고성 가오리찜", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg",
 "고성 여행 길에 매콤한 찜이 생각나면 속초로 내려오는 길에 들르세요.", L(A("goseong-saengseon-jjim","고성 생선찜"), A("gaori-jjim-matjip","가오리찜 맛집")))
town_dish("goseong-squid-sundae", "고성 오징어순대", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg",
 "오징어순대는 속초를 대표하는 별미라 고성 여행객도 속초에 들러 많이 맛봅니다.", L(A("squid-sundae-matjip","오징어순대 맛집"), A("goseong-matjip","고성 맛집")))
town_dish("yangyang-honbap", "양양 혼밥", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 "혼자 양양 여행 중이라면 혼자서도 편하게 시킬 수 있는 메뉴가 필요합니다.", L(A("sokcho-honbap","속초 혼밥"), A("yangyang-bapjip","양양 밥집")))
town_dish("goseong-bapjip", "고성 밥집", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "고성 여행 중 제대로 된 밥 한 끼가 필요하다면 속초로 내려오는 길을 이용하세요.", L(A("goseong-matjip","고성 맛집"), A("goseong-dinner-matjip","고성 저녁 맛집")))

# ---------- 여행 종류 ----------
def trip(slug, kw, lede, plan, more, faq):
    add(slug, kw, "여행", "storefront.jpg", lede,
     [("이렇게 다녀 보세요", L(*plan)),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

trip("sokcho-2bak3il-matjip", "속초 2박3일 맛집", "2박3일 속초, 끼니마다 무엇을 먹을까.",
 ["첫날 저녁: 대포항에서 생선찜", "둘째 날 점심: 시장 구경하며 간식", "둘째 날 저녁: 숙소에서 포장 음식", "셋째 날 점심: 출발 전 든든하게"],
 L(A("sokcho-2bak3il","속초 2박3일 코스"), A("sokcho-1bak2il-matjip","속초 1박2일 맛집"), A("sokcho-last-meal","속초 마지막 식사")), [TOGO, PARK])
trip("sokcho-day-trip-matjip", "속초 당일치기 맛집", "하루만 머무는 속초, 한 끼는 제대로.",
 ["아침 일찍 출발", "오전: 바다와 항구 구경", "점심: 대포항에서 생선찜", "오후: 시장 들렀다 출발, 남은 건 포장"],
 L(A("sokcho-day-trip","속초 당일치기"), A("gangwon-day-trip","강원도 당일치기"), A("sokcho-ic-matjip","속초IC 근처 맛집")), [TOGO, PARK])
trip("sokcho-winter-1bak2il", "속초 겨울 1박2일", "겨울 속초 1박2일, 바다와 온천과 생선찜.",
 ["첫날: 겨울 바다 산책, 대포항 생선찜 저녁", "둘째 날: 온천이나 실내 명소, 점심 먹고 출발"],
 L(A("sokcho-winter-course","속초 겨울 여행 코스"), A("sokcho-winter-matjip","속초 겨울 맛집"), A("gangwon-winter-trip","강원도 겨울 여행")), [OFF, PARK])
trip("sokcho-sikdorak", "속초 식도락 여행", "먹으러 가는 속초, 이것만은 꼭.",
 ["생선찜: 가오리찜, 코다리찜, 대구뽈찜", "순대: 오징어순대, 아바이순대", "간식: 닭강정, 튀김", "마무리: 포장해서 숙소로"],
 L(A("sokcho-must-eat","속초 꼭 먹어야 할 음식"), A("sokcho-food-course","속초 먹방 코스"), A("sokcho-food","속초 먹거리")), [TOGO, SIZE])
trip("sokcho-hotplace", "속초 핫플", "요즘 속초에서 사람들이 많이 가는 곳.",
 ["바다 앞 대관람차와 해수욕장", "청초호 주변 카페 거리", "아바이마을과 갯배", "대포항 산책과 항구 먹거리"],
 L(A("sokcho-attractions","속초 가볼만한곳"), A("sokcho-photo-spots","속초 사진 명소"), A("daepohang-attractions","대포항 가볼만한곳")), [WHERE])

# ---------- 명소 ----------
def spot(slug, kw, lede, about, more):
    add(slug, kw, "근처", "storefront.jpg", lede,
     [("둘러보기", f"<p>{about}</p>"),
      ("배고프면 대포항으로", "<p>속초 시내 구경을 마치고 남쪽 대포항으로 내려와 생선찜으로 한 끼를 채우세요.</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, PARK])

spot("chilseong-shipyard-matjip", "칠성조선소 근처 맛집", "칠성조선소 구경하고 생선 한 끼.",
 "칠성조선소는 청초호 옆의 오래된 조선소를 고쳐 만든 공간으로, 카페와 전시를 함께 둘러볼 수 있습니다.",
 L(A("cheongchoho-matjip","청초호 근처 맛집"), A("sokcho-cafe-tour","속초 카페 투어"), A("sokcho-hotplace","속초 핫플")))
spot("munudang-matjip", "문우당서림 근처 맛집", "속초 서점 구경하고 생선 한 끼.",
 "문우당서림은 속초 시내의 오래된 동네 서점으로, 여행객들이 일부러 찾아가는 곳입니다.",
 L(A("sokcho-indoor","속초 실내 가볼만한곳"), A("sokcho-rainy-gabolmanhan","속초 비오는날 가볼만한곳"), A("sokcho-hotplace","속초 핫플")))
spot("sokcho-museum-matjip", "속초시립박물관 근처 맛집", "실향민 이야기 보고, 아바이순대 맛보기.",
 "속초시립박물관에는 실향민 마을을 재현한 공간이 있어 속초의 역사를 둘러보기 좋습니다. 박물관을 보고 나면 실향민 음식인 아바이순대가 궁금해집니다.",
 L(A("sokcho-silhyangmin-food","속초 실향민 음식"), A("abai-sundae-story","아바이순대 이야기"), A("brand-abai-sundae","대포항생선찜본점 아바이순대")))
