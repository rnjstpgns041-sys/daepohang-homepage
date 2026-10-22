# 50 keyword pages (added 2026-10-22), batch 551-600.
# Owner asked for keywords from people actually choosing where to sit down and eat.
# So: meal (점심/저녁) x who, meal x when, meal x nearby place, dish x nearby place, dish x meal.
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
KIDS = ("아이와 가도 되나요?","네, 아기 의자가 있고 맵지 않은 생선구이와 순대가 있습니다.")
HOURS = ("몇 시까지 하나요?",f"영업시간은 전화({TEL})로 확인해 주세요.")
SHOP = f"<p>대포항생선찜본점은 속초시 대포항길 10, 대포항 안쪽 상가 1층에 있습니다. 노란색과 분홍색 네온 간판을 찾으세요. 매주 수요일은 쉬고, 전 메뉴 포장됩니다. 전화 {TEL}.</p>"
def j(w, a, b):
    return a if (ord(w[-1]) - 0xAC00) % 28 else b

# ---------- 점심·저녁 x 누구와 ----------
def meal_who(slug, kw, img, lede, scene, order, more, faq):
    add(slug, kw, "상황별", img, lede,
     [("이런 한 끼", f"<p>{scene}</p>"),
      ("이렇게 시켜 보세요", f"<p>{order}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

meal_who("sokcho-family-lunch", "속초 가족 점심", "jjim-table.jpg", "가족 여행 중 점심, 다 같이 둘러앉는 생선찜.",
 "오전 일정을 마친 가족 여행의 점심은 아이도 어른도 배가 고픈 때입니다. 기다리지 않고 바로 먹을 수 있는 메뉴가 좋습니다.",
 "넷이라면 가오리찜 대(4인)에 맵지 않은 모듬생선구이를 더하세요. 아이 몫은 구이로 해결됩니다.",
 L(A("sokcho-family-dining","속초 가족 외식"), A("family-dining-menu","가족 외식 메뉴 추천"), A("sokcho-lunch-matjip","속초 점심 맛집")), [KIDS, SIZE])
meal_who("sokcho-family-dinner", "속초 가족 저녁", "jjim-table.jpg", "하루를 마친 가족, 저녁은 항구 앞 생선찜.",
 "바다와 산을 돌고 온 가족에게 저녁은 하루의 마무리입니다. 큰 냄비 찜을 가운데 두고 오늘 있었던 이야기를 나눠 보세요.",
 "찜 대(4인)와 누룽지 오징어순대, 아이가 있다면 모듬생선구이까지. 남으면 포장해 숙소에서 드셔도 됩니다.",
 L(A("sokcho-dinner-matjip","속초 저녁 맛집"), A("daepohang-family-dining","대포항 가족 식사"), A("sokcho-family-trip","속초 가족여행 코스")), [KIDS, TOGO])
meal_who("sokcho-couple-lunch", "속초 커플 점심", "gaori-jjim.jpg", "둘이 떠난 속초, 점심은 가오리찜 소 하나.",
 "커플 여행의 점심은 오후 일정을 위해 너무 무겁지 않게, 그래도 속초다운 걸로 고르고 싶어집니다.",
 "가오리찜 소(2인) 하나면 둘이 알맞습니다. 매운 걸 잘 못 먹는다면 모듬생선구이로 바꾸세요.",
 L(A("sokcho-date-matjip","속초 데이트 맛집"), A("gaori-jjim-2in","가오리찜 2인"), A("sokcho-couple-trip","속초 커플 여행")), [SIZE, TOGO])
meal_who("sokcho-couple-dinner", "속초 커플 저녁", "storefront.jpg", "네온 불 켜진 항구, 둘이 먹는 저녁.",
 "해가 지면 대포항에 불이 켜집니다. 항구를 한 바퀴 걷고 따뜻한 찜에 술 한잔 곁들이기 좋은 시간입니다.",
 "찜 소(2인)에 누룽지 오징어순대, 소주나 막걸리 한 병이면 둘이 먹기 넉넉합니다.",
 L(A("daepohang-night","대포항 야경"), A("sokcho-winter-date","속초 겨울 데이트"), A("daepohang-date","대포항 데이트")), [SIZE, HOURS])
meal_who("sokcho-parents-lunch", "속초 부모님 점심", "jjim-closeup.jpg", "부모님 모시고 속초, 편하게 앉아 드시는 점심.",
 "부모님과의 여행에서 점심은 오래 걷지 않고 바로 앉을 수 있는 곳이 좋습니다. 밥반찬이 되는 메뉴를 부모님들이 좋아하십니다.",
 "가오리찜이나 생선모듬찜에 공깃밥. 매운 걸 못 드시면 모듬생선구이를 함께 시키세요.",
 L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-hyodo-trip","속초 효도 여행"), A("parents-trip-korea","부모님 모시고 국내 여행")), [SIZE, PARK])
meal_who("sokcho-parents-dinner", "속초 부모님 저녁", "jjim-table.jpg", "부모님과 하루를 마치는 저녁, 생선찜 한 상.",
 "하루 종일 함께 다닌 부모님께 저녁은 든든하게 차려 드리고 싶어집니다.",
 "찜 중·대에 모듬생선구이와 아바이순대를 곁들이면 한 상이 풍성해집니다. 반주 한잔도 좋습니다.",
 L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-three-generations","3대 가족 속초 식사"), A("sokcho-palsun","속초 팔순 가족 식사")), [SIZE, PARK])
meal_who("sokcho-kids-lunch", "속초 아이랑 점심", "gui.jpg", "아이와 속초, 맵지 않은 점심 한 끼.",
 "아이와 다니면 점심 메뉴 고르기가 가장 어렵습니다. 맵지 않고, 가시 바르기 쉬운 메뉴가 있어야 합니다.",
 "아이는 모듬생선구이와 아바이순대, 어른은 가오리찜. 아기 의자도 있습니다.",
 L(A("sokcho-kids-matjip","속초 아이랑 맛집"), A("kids-fish-dish","아이가 먹기 좋은 생선 요리"), A("brand-kids","대포항생선찜본점 아기의자")), [KIDS, SIZE])
meal_who("sokcho-kids-dinner", "속초 아이랑 저녁", "gui.jpg", "놀다 지친 아이와 저녁, 빨리 나오는 생선구이.",
 "하루 종일 논 아이는 저녁 무렵 배가 고프고 지쳐 있습니다. 숙소 가기 전 가까운 곳에서 든든히 먹이는 것이 좋습니다.",
 "모듬생선구이에 공깃밥이면 아이 저녁으로 충분합니다. 피곤하면 포장해서 숙소에서 드셔도 됩니다.",
 L(A("sokcho-kids-matjip","속초 아이랑 맛집"), A("sokcho-elementary-trip","속초 초등학생 아이 여행"), A("brand-takeout","대포항생선찜본점 포장")), [KIDS, TOGO])
meal_who("sokcho-friends-dinner", "속초 친구 저녁", "jjim-closeup.jpg", "친구들과 속초, 저녁은 찜에 한잔.",
 "친구 여행의 저녁은 길어집니다. 나눠 먹을 큰 찜과 안주 하나, 술 몇 병이면 충분합니다.",
 "넷이면 찜 대(4인)에 누룽지 오징어순대. 소주, 맥주, 막걸리가 있습니다.",
 L(A("sokcho-friends-trip","속초 친구여행 맛집"), A("sokcho-suljip","속초 술집"), A("sokcho-student-trip","속초 대학생 여행")), [SIZE, HOURS])
meal_who("sokcho-solo-lunch", "속초 혼자 점심", "gui.jpg", "혼자 속초, 점심은 생선구이 한 판.",
 "혼자 여행할 때는 1인분으로 시킬 수 있는 메뉴가 있는지가 중요합니다.",
 "모듬생선구이나 누룽지 오징어순대에 공깃밥이 혼자 먹기 알맞습니다. 찜은 소(2인)부터라 남으면 포장해 가세요.",
 L(A("sokcho-honbap","속초 혼밥"), A("sokcho-solo-trip","속초 혼자 여행"), A("sokcho-honsul","속초 혼술")), [TOGO, WHERE])
meal_who("sokcho-group-lunch", "속초 단체 점심", "hall2.jpg", "여럿이 함께하는 속초 점심, 미리 전화 주세요.",
 "단체 여행의 점심은 시간이 정해져 있어서 빨리 앉고 빨리 나오는 것이 중요합니다.",
 f"인원과 도착 시간을 미리 전화({TEL})로 알려 주세요. 찜 대 여러 개에 모듬생선구이를 섞어 시키면 됩니다.",
 L(A("brand-group","대포항생선찜본점 단체"), A("sokcho-group-restaurant","속초 단체 식당"), A("sokcho-10-people","속초 10명 식사")), [SIZE, PARK])
meal_who("sokcho-group-dinner", "속초 단체 저녁", "hall2.jpg", "모임 저녁, 큰 냄비 생선찜으로.",
 "동호회, 모임, 회식처럼 여럿이 저녁을 먹는다면 나눠 먹는 찜이 편합니다.",
 f"찜 대 여러 개에 누룽지 오징어순대, 모듬생선구이를 곁들이세요. 미리 전화({TEL}) 주시면 좋습니다.",
 L(A("brand-group","대포항생선찜본점 단체"), A("sokcho-hoesik","속초 회식 장소"), A("sokcho-moim","속초 모임 식당")), [SIZE, PARK])

# ---------- 점심·저녁 x 언제 ----------
def meal_when(slug, kw, lede, scene, tip, more, faq):
    add(slug, kw, "상황별", "jjim-table.jpg", lede,
     [("이때 속초는", f"<p>{scene}</p>"),
      ("대포항생선찜본점에서", f"<p>{tip}</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

meal_when("sokcho-weekend-lunch", "속초 주말 점심", "주말 점심, 붐비기 전에 대포항으로.",
 "주말 점심에는 속초 시내와 항구가 가장 붐빕니다. 조금 일찍 움직이면 훨씬 여유롭습니다.",
 f"포장이라면 전화({TEL})로 미리 주문해 두세요. 받는 시간만 맞춰 오시면 됩니다.",
 L(A("sokcho-weekend-matjip","속초 주말 맛집"), A("sokcho-saturday-lunch","속초 토요일 점심"), A("daepohang-weekend","대포항 주말")), [PARK, TOGO])
meal_when("sokcho-weekend-dinner", "속초 주말 저녁", "주말 저녁, 항구 불빛 아래 생선찜.",
 "주말 저녁 대포항은 산책하는 사람들로 활기가 넘칩니다.",
 "여럿이라면 자리를 위해 미리 전화 주세요. 찜은 소·중·대로 인원에 맞춰 고르시면 됩니다.",
 L(A("sokcho-weekend-matjip","속초 주말 맛집"), A("daepohang-night","대포항 야경"), A("sokcho-dinner-matjip","속초 저녁 맛집")), [SIZE, PARK])
meal_when("sokcho-weekday-lunch", "속초 평일 점심", "평일 속초, 한적하게 먹는 점심.",
 "평일 속초는 주말보다 훨씬 조용합니다. 줄 서지 않고 여유 있게 식사하기 좋습니다.",
 "수요일만 쉬니 그날만 피하세요.",
 L(A("sokcho-weekday-trip","속초 평일 여행"), A("sokcho-day-off-trip","속초 연차 여행"), A("sokcho-lunch-matjip","속초 점심 맛집")), [OFF, PARK])
meal_when("sokcho-weekday-dinner", "속초 평일 저녁", "평일 저녁, 조용한 항구에서 생선찜.",
 "평일 저녁 항구는 한적해서 천천히 먹고 걷기 좋습니다.",
 "수요일은 쉽니다. 늦게 오신다면 영업시간을 전화로 확인해 주세요.",
 L(A("sokcho-weekday-trip","속초 평일 여행"), A("sokcho-after-work-dinner","속초 퇴근 후 저녁"), A("daepohang-weekday","대포항 평일")), [OFF, HOURS])
meal_when("sokcho-saturday-dinner", "속초 토요일 저녁", "토요일 저녁, 가장 붐비는 날 미리 챙기기.",
 "토요일 저녁은 한 주 중 속초가 가장 붐비는 때입니다.",
 f"자리 문의나 포장은 미리 전화({TEL})로 해 두세요.",
 L(A("sokcho-saturday-lunch","속초 토요일 점심"), A("sokcho-weekend-dinner","속초 주말 저녁"), A("brand-reservation","대포항생선찜본점 예약")), [PARK, TOGO])
meal_when("sokcho-holiday-dinner", "속초 연휴 저녁", "연휴 속초 저녁, 붐빌 땐 포장도 방법.",
 "연휴에는 속초 어디든 사람이 많습니다. 식당 앞에서 오래 기다리기보다 포장해서 숙소에서 먹는 분도 많습니다.",
 f"전화({TEL})로 미리 포장을 주문하고, 받는 시간에 맞춰 오세요.",
 L(A("sokcho-holiday","속초 명절 여행"), A("daepohang-holiday","대포항 연휴"), A("sokcho-stay-in-dinner","숙소에서 먹는 저녁")), [TOGO, HOURS])

# ---------- 점심·저녁 x 근처 명소 ----------
def meal_place(slug, kw, place, meal, lede, about, more):
    add(slug, kw, "근처", "storefront.jpg", lede,
     [(f"{place} 다녀와서", f"<p>{about}</p>"),
      (f"{meal}은 대포항에서", f"<p>속초 남쪽 대포항의 대포항생선찜본점에서 생선찜, 생선구이, 순대를 드실 수 있습니다. 주차는 대포항 공영주차장을 이용하세요.</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, PARK])

meal_place("seoraksan-lunch", "설악산 점심 맛집", "설악산", "점심", "설악산 다녀온 점심, 바다 쪽으로 내려와 생선찜.",
 "설악산 소공원이나 케이블카를 보고 나오면 점심때가 됩니다. 산에서 내려와 바다 쪽으로 가면 식사와 바다 구경을 함께 할 수 있습니다.",
 L(A("seoraksan-matjip","설악산 근처 맛집"), A("seorak-sogongwon-matjip","설악산 소공원 근처 맛집"), A("seorak-cablecar-matjip","설악산 케이블카 맛집")))
meal_place("seoraksan-dinner", "설악산 저녁 맛집", "설악산", "저녁", "설악산 하루 일정 끝, 저녁은 항구에서.",
 "산행을 마치면 다리는 무겁고 배는 고픕니다. 따뜻한 찜에 밥 한 공기로 하루를 마무리하세요.",
 L(A("seoraksan-matjip","설악산 근처 맛집"), A("ulsanbawi-matjip","울산바위 등산 후 맛집"), A("seorak-danpung-matjip","설악산 단풍 맛집")))
meal_place("sokcho-beach-lunch", "속초해수욕장 점심", "속초해수욕장", "점심", "해수욕장 산책하고 점심은 생선 한 상.",
 "속초해수욕장 주변은 대관람차와 산책로가 있어 오전 시간을 보내기 좋습니다. 점심때가 되면 남쪽 대포항으로 내려와 보세요.",
 L(A("sokcho-beach-matjip","속초해수욕장 근처 맛집"), A("sokcho-eye-matjip","속초아이 대관람차 근처 맛집"), A("sokcho-lunch-matjip","속초 점심 맛집")))
meal_place("sokcho-beach-dinner", "속초해수욕장 저녁", "속초해수욕장", "저녁", "해 질 무렵 해수욕장, 저녁은 대포항 생선찜.",
 "속초해수욕장에서 해 질 무렵을 보내고 나면 저녁 먹을 곳을 찾게 됩니다.",
 L(A("sokcho-beach-matjip","속초해수욕장 근처 맛집"), A("sokcho-night-view","속초 야경"), A("sokcho-dinner-matjip","속초 저녁 맛집")))
meal_place("oeongchi-lunch", "외옹치 점심", "외옹치", "점심", "외옹치 바다향기로 걷고 점심.",
 "외옹치 바다향기로는 바다를 끼고 걷는 산책로입니다. 걷고 나면 가까운 대포항에서 점심을 드세요.",
 L(A("oeongchi-matjip","외옹치 맛집"), A("sokcho-badahyanggiro-matjip","바다향기로 맛집"), A("daepohang-lunch","대포항 점심")))
meal_place("oeongchi-dinner", "외옹치 저녁", "외옹치", "저녁", "외옹치 근처 숙소라면, 저녁은 대포항.",
 "외옹치 주변 숙소에 묵는다면 대포항이 가장 가까운 저녁 장소 중 하나입니다.",
 L(A("oeongchi-matjip","외옹치 맛집"), A("daepohang-dinner","대포항 저녁"), A("daepohang-lodging-dinner","대포항 숙소 근처 식당")))
meal_place("lotte-resort-dinner", "속초 롯데리조트 저녁", "롯데리조트", "저녁", "롯데리조트 묵는 날, 저녁은 밖에서 생선찜.",
 "리조트 안에서만 먹기 아쉽다면 가까운 항구로 나가 속초다운 저녁을 드셔 보세요.",
 L(A("sokcho-lotte-resort-matjip","속초 롯데리조트 근처 맛집"), A("sokcho-hotel-matjip","속초 호텔 근처 맛집"), A("sokcho-stay-in-dinner","숙소에서 먹는 저녁")))
meal_place("solbeach-dinner", "쏠비치 양양 저녁", "쏠비치 양양", "저녁", "쏠비치 양양에서 북쪽으로, 저녁은 속초 대포항.",
 "쏠비치 양양에 묵는다면 속초 대포항까지 바닷길로 이어집니다. 하루쯤은 속초로 저녁을 먹으러 나와 보세요.",
 L(A("solbeach-yangyang-matjip","쏠비치 양양 근처 맛집"), A("yangyang-dinner-matjip","양양 저녁 맛집"), A("yangyang-saengseon-jjim","양양 생선찜")))
meal_place("naksan-dinner", "낙산 저녁 맛집", "낙산", "저녁", "낙산 해변과 낙산사 다녀와서 저녁.",
 "낙산해수욕장과 낙산사를 둘러본 날, 저녁은 북쪽 속초 대포항에서 드셔 보세요.",
 L(A("naksan-beach-matjip","낙산해수욕장 근처 맛집"), A("naksansa-matjip","낙산사 가는 길 맛집"), A("yangyang-dinner-matjip","양양 저녁 맛집")))
meal_place("abai-village-lunch", "아바이마을 점심", "아바이마을", "점심", "아바이마을 구경하고 점심.",
 "갯배를 타고 아바이마을을 둘러보면 오전이 금방 갑니다. 아바이순대를 더 맛보고 싶다면 대포항에서도 드실 수 있습니다.",
 L(A("abai-village-matjip","아바이마을 근처 맛집"), A("brand-abai-sundae","대포항생선찜본점 아바이순대"), A("abai-sundae-taste","아바이순대 맛")))
meal_place("tourist-market-lunch", "속초관광수산시장 점심", "속초관광수산시장", "점심", "시장 구경하고, 앉아서 먹는 점심.",
 "시장 먹거리는 서서 먹거나 포장이 많습니다. 제대로 앉아서 밥을 먹고 싶다면 대포항으로 내려오세요.",
 L(A("sokcho-tourist-market-matjip","속초관광수산시장 근처 맛집"), A("sokcho-dakgangjeong","속초 닭강정"), A("sokcho-food","속초 먹거리")))
meal_place("sokcho-eye-dinner", "속초아이 대관람차 저녁", "속초아이 대관람차", "저녁", "대관람차 타고 나서, 저녁은 생선찜.",
 "대관람차에서 속초 바다를 내려다본 뒤 저녁을 먹을 곳을 찾는다면 남쪽 대포항으로 가 보세요.",
 L(A("sokcho-eye-matjip","속초아이 대관람차 근처 맛집"), A("sokcho-beach-dinner","속초해수욕장 저녁"), A("sokcho-night-view","속초 야경")))

# ---------- 메뉴 x 근처 동네 ----------
def dish_place(slug, kw, place, dish, dish_slug, img, about, more):
    add(slug, kw, "근처", img, f"{place} 근처에서 {dish}{j(dish,'을','를')} 찾는다면, 대포항으로.",
     [(f"{place}에서", f"<p>{about}</p>"),
      (dish, f"<p>대포항생선찜본점의 {A(dish_slug, dish)}{j(dish,'은','는')} 이 집 손님들이 많이 찾는 메뉴입니다. 찜은 소(2인), 중(3인), 대(4인)로, 전 메뉴 포장됩니다.</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, TOGO])

G = ("모듬생선구이","sokcho-saengseon-gui","gui.jpg")
J = ("생선모듬찜","sokcho-saengseon-modeum-jjim","jjim-table.jpg")
for slug, kw, place, d, about, more in [
  ("oeongchi-saengseon-jjim","외옹치 생선찜","외옹치",J,"외옹치는 대포항 바로 북쪽의 작은 항구 마을입니다.",L(A("oeongchi-matjip","외옹치 맛집"),A("fish-jjim-matjip","생선찜 맛집"))),
  ("oeongchi-saengseon-gui","외옹치 생선구이","외옹치",G,"외옹치 산책 뒤 맵지 않은 생선구이가 당길 때 가까운 대포항으로 오세요.",L(A("oeongchi-matjip","외옹치 맛집"),A("fish-gui-matjip","생선구이 맛집"))),
  ("mulchi-saengseon-jjim","물치 생선찜","물치",J,"물치는 속초와 맞닿은 양양 북쪽 항구 마을입니다. 대포항이 가깝습니다.",L(A("mulchihang-matjip","물치항 근처 맛집"),A("yangyang-saengseon-jjim","양양 생선찜"))),
  ("mulchi-saengseon-gui","물치 생선구이","물치",G,"물치 해변에서 놀고 나면 북쪽 대포항에서 생선구이 한 판이 좋습니다.",L(A("mulchihang-matjip","물치항 근처 맛집"),A("yangyang-saengseon-gui","양양 생선구이"))),
  ("seoraksan-saengseon-gui","설악산 생선구이","설악산",G,"설악산 산행 뒤 담백한 생선구이가 생각난다면 바다 쪽으로 내려오세요.",L(A("seoraksan-matjip","설악산 근처 맛집"),A("seoraksan-lunch","설악산 점심 맛집"))),
  ("seoraksan-saengseon-jjim","설악산 생선찜","설악산",J,"설악산을 다녀온 날, 매콤한 생선찜으로 언 몸을 녹이세요.",L(A("seoraksan-matjip","설악산 근처 맛집"),A("seoraksan-dinner","설악산 저녁 맛집"))),
  ("sokcho-beach-saengseon-jjim","속초해수욕장 생선찜","속초해수욕장",J,"속초해수욕장 근처 숙소에 묵는다면 남쪽 대포항까지 내려와 생선찜을 드셔 보세요.",L(A("sokcho-beach-matjip","속초해수욕장 근처 맛집"),A("sokcho-beach-dinner","속초해수욕장 저녁"))),
  ("naksan-saengseon-gui","낙산 생선구이","낙산",G,"낙산 해변과 낙산사를 둘러본 날, 북쪽으로 올라와 생선구이로 한 끼를 채우세요.",L(A("naksan-beach-matjip","낙산해수욕장 근처 맛집"),A("naksan-dinner","낙산 저녁 맛집"))),
  ("daepodong-saengseon-jjim","대포동 생선찜","대포동",J,"대포동은 대포항이 있는 동네입니다. 동네 안에서 생선찜을 찾는다면 바로 여기입니다.",L(A("daepodong-matjip","대포동 맛집"),A("daepohang-saengseon-jjim","대포항 생선찜"))),
  ("daepodong-saengseon-gui","대포동 생선구이","대포동",G,"대포동 숙소에 묵는다면 걸어서 대포항까지 나와 생선구이를 드셔 보세요.",L(A("daepodong-matjip","대포동 맛집"),A("daepohang-saengseon-gui","대포항 생선구이"))),
]:
    dish_place(slug, kw, place, d[0], d[1], d[2], about, more)

# ---------- 메뉴 x 점심·저녁 ----------
def dish_meal(slug, kw, dish, dish_slug, img, meal, scene, order, more, faq):
    add(slug, kw, "메뉴", img, f"{meal}으로 먹는 {dish}, 속초 대포항에서." if meal == "점심" else f"{meal}에 먹는 {dish}, 속초 대포항에서.",
     [(f"{meal}에 {dish}", f"<p>{scene}</p>"),
      ("이렇게 드세요", f"<p>{order}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     faq)

dish_meal("sokcho-gui-lunch", "속초 생선구이 점심", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg", "점심",
 "점심에는 맵지 않고 담백한 생선구이가 부담 없습니다. 오후 일정이 있어도 속이 편합니다.",
 "모듬생선구이에 공깃밥. 둘 이상이면 누룽지 오징어순대를 곁들이세요.",
 L(A("sokcho-saengseon-gui","속초 생선구이"), A("fish-gui-good","생선구이 잘하는 집")), [KIDS, TOGO])
dish_meal("sokcho-jjim-dinner", "속초 생선찜 저녁", "생선찜", "sokcho-saengseon-jjim", "jjim-table.jpg", "저녁",
 "저녁에는 보글보글 끓는 찜 냄비가 제격입니다. 양념에 밥을 비벼 먹으며 하루를 마무리하세요.",
 "찜은 인원에 맞춰 소·중·대로. 술 한잔 곁들이면 오징어순대가 안주로 좋습니다.",
 L(A("sokcho-saengseon-jjim","속초 생선찜"), A("fish-jjim-good","생선찜 잘하는 집")), [SIZE, HOURS])
dish_meal("sokcho-jjim-lunch", "속초 생선찜 점심", "생선찜", "sokcho-saengseon-jjim", "jjim-closeup.jpg", "점심",
 "든든하게 먹고 오후를 버티고 싶다면 점심에도 생선찜이 좋습니다.",
 "둘이면 소(2인), 셋이면 중(3인). 남으면 포장해 저녁에 데워 드셔도 됩니다.",
 L(A("sokcho-saengseon-jjim","속초 생선찜"), A("sokcho-lunch-matjip","속초 점심 맛집")), [SIZE, TOGO])
dish_meal("sokcho-gaori-dinner", "속초 가오리찜 저녁", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg", "저녁",
 "쫀득한 가오리와 오독한 연골은 저녁 반주 안주로도 인기입니다.",
 "가오리찜에 소주나 막걸리 한 병. 마지막엔 남은 양념에 밥을 비벼 드세요.",
 L(A("sokcho-gaori-jjim","속초 가오리찜"), A("gaori-jjim-good","가오리찜 잘하는 집")), [SIZE, HOURS])
dish_meal("daepohang-gui-lunch", "대포항 생선구이 점심", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg", "점심",
 "대포항 구경을 하다 점심때가 되면 항구 안쪽 상가에서 생선구이 한 판을 드셔 보세요.",
 "맵지 않아 아이와 부모님도 잘 드십니다.",
 L(A("daepohang-saengseon-gui","대포항 생선구이"), A("daepohang-lunch","대포항 점심")), [KIDS, PARK])
dish_meal("daepohang-gaori-dinner", "대포항 가오리찜 저녁", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg", "저녁",
 "네온 불 켜진 대포항에서 먹는 가오리찜 저녁은 속초 여행의 한 장면이 됩니다.",
 "가오리찜에 누룽지 오징어순대를 곁들이면 한 상이 완성됩니다.",
 L(A("daepohang-gaori-jjim","대포항 가오리찜"), A("daepohang-dinner","대포항 저녁")), [SIZE, PARK])
dish_meal("sokcho-sundae-dinner", "속초 오징어순대 저녁", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg", "저녁",
 "저녁에 가볍게 한잔하고 싶을 때 바삭한 오징어순대가 안주로 좋습니다.",
 "누룽지 오징어순대(17,000원)에 막걸리 한 병. 더 드시려면 찜 소를 더하세요.",
 L(A("sokcho-nurungji-squid-sundae","속초 누룽지 오징어순대"), A("sokcho-makgeolli-anju","속초 막걸리 안주")), [HOURS, TOGO])
dish_meal("sokcho-kodari-lunch", "속초 코다리찜 점심", "코다리찜", "sokcho-kodari-jjim", "jjim-closeup.jpg", "점심",
 "양념 진한 코다리찜은 밥반찬으로 최고라 점심 메뉴로 많이 찾습니다.",
 "코다리찜에 공깃밥, 마지막엔 양념에 밥을 비벼 드세요.",
 L(A("sokcho-kodari-jjim","속초 코다리찜"), A("kodari-jjim-good","코다리찜 잘하는 집")), [SIZE, TOGO])

# ---------- 메뉴 x 누구와 ----------
dish_meal("sokcho-parents-jjim", "부모님과 속초 생선찜", "생선찜", "sokcho-saengseon-jjim", "jjim-table.jpg", "식사",
 "부모님들은 밥반찬이 되는 생선찜을 특히 좋아하십니다. 부드러운 생선살과 양념 밴 무가 입에 잘 맞습니다.",
 "가오리찜이나 생선모듬찜, 매운 걸 못 드시면 모듬생선구이를 함께.",
 L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-parents-lunch","속초 부모님 점심")), [SIZE, PARK])
dish_meal("sokcho-family-jjim", "가족과 속초 생선찜", "생선찜", "sokcho-saengseon-jjim", "jjim-table.jpg", "식사",
 "가족이 둘러앉아 큰 냄비 하나를 나눠 먹는 생선찜은 가족 외식으로 잘 맞습니다.",
 "넷이면 대(4인), 아이가 있으면 모듬생선구이를 더하세요.",
 L(A("sokcho-family-dining","속초 가족 외식"), A("gaori-jjim-4in","가오리찜 4인 가족")), [KIDS, SIZE])
