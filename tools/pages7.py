# 50 more keyword pages (added 2026-10-15). Same shape as pages2-6.
# Store facts only from the listing / photos; area facts kept general (no distances or minutes).
# Opening hours are unconfirmed, so pages point to the phone instead of stating times.
from pages2 import add as _add, L, A

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

TEL = "0507-1364-4060"
MENU_LINKS = L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-saengseon-gui","모듬생선구이"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"))
WHERE = ("가게 위치는?","속초시 대포항길 10입니다.")
OFF = ("휴무일은?","매주 수요일입니다.")
TOGO = ("포장되나요?","네, 전 메뉴 포장됩니다.")
SIZE = ("사이즈는 어떻게 되나요?","찜은 소(2인), 중(3인), 대(4인)입니다.")
PARK = ("주차는?",A("daepohang-parking","주차 안내")+"를 참고하세요.")
HOURS = ("몇 시까지 하나요?",f"영업시간은 전화({TEL})로 확인해 주세요.")
BABY = ("아기의자 있나요?","네, 있습니다.")
GROUP = ("단체 예약 되나요?",f"전화({TEL})로 문의해 주세요.")

# ---------- 메뉴 ----------
add("gaori-jjim-spicy-level", "가오리찜 맵기", "메뉴", "gaori-jjim.jpg",
 "가오리찜 얼마나 매울까? 맵기가 걱정되는 분을 위한 안내.",
 [("칼칼하지만 달큰해요",
   "<p>가오리찜 양념은 고춧가루로 칼칼하게 맛을 내지만, 무와 양파에서 나온 단맛이 함께 있어 맵기만 한 맛은 아닙니다. 매운 음식을 아주 못 드시는 분이 아니라면 대부분 잘 드십니다.</p>"),
  ("매운 게 걱정이라면",
   L("밥 위에 올려 양념을 조금만 끼얹어 드세요","양념 밴 무를 함께 드시면 덜 맵게 느껴져요","맵지 않은 "+A("sokcho-saengseon-gui","생선구이")+"나 "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+"를 곁들이세요")),
  ("더 보기", L(A("gaori-jjim-taste","가오리찜 맛"), A("sokcho-mild-menu","속초 안 매운 메뉴")))],
 [("아이도 먹을 수 있나요?","아이에게는 맵지 않은 구이와 순대를 권해 드립니다."), SIZE])

add("modeum-jjim-takeout", "생선모듬찜 포장", "메뉴", "jjim-table.jpg",
 "여러 생선이 한 냄비에, 생선모듬찜 포장해 숙소에서.",
 [("숙소에서 한 상",
   f"<p>{A('sokcho-saengseon-modeum-jjim','생선모듬찜')}은 포장해 가도 여러 생선을 한 번에 즐길 수 있어 숙소 저녁으로 좋습니다. 미리 전화({TEL})로 주문하면 바로 받아 가실 수 있습니다.</p>"),
  ("데울 때는", L("냄비에 옮겨 약불로","양념이 졸면 물을 조금","무를 바닥에 깔고 데우면 눌어붙지 않아요")),
  ("더 보기", L(A("saengseon-jjim-reheat","생선찜 포장 데우는 법"), A("sokcho-stay-in-dinner","숙소에서 먹는 저녁")))],
 [TOGO, SIZE])

add("daegu-ppol-taste", "대구뽈찜 맛", "메뉴", "jjim-closeup.jpg",
 "쫀득한 볼살과 젤라틴 가득한 껍질. 대구뽈찜은 이런 맛이에요.",
 [("고르는 재미가 있는 맛",
   "<p>대구뽈찜은 대구 머리 쪽의 볼살과 껍질을 쪄낸 음식입니다. 쫀득하게 씹히는 볼살과 말랑한 껍질이 매콤한 양념과 어우러져, 발라 먹는 재미가 있습니다.</p>"),
  ("이런 분께 추천", L("쫀득한 식감을 좋아하는 분","술안주로 찜을 찾는 분","가오리찜과 다른 맛을 찾는 분")),
  ("더 보기", L(A("sokcho-daegu-ppol-jjim","속초 대구뽈찜 메뉴"), A("daegu-ppol-how-to-eat","대구뽈찜 먹는 법"), A("daegu-ppol-meaning","대구뽈 뜻")))],
 [SIZE, ("맵나요?","칼칼한 편입니다.")])

add("kodari-jjim-taste", "코다리찜 맛", "메뉴", "jjim-table.jpg",
 "꾸덕하고 쫄깃한 반건조 명태, 코다리찜의 맛.",
 [("반건조라 쫄깃해요",
   "<p>코다리는 명태를 반쯤 말린 것이라 살이 꾸덕하고 쫄깃합니다. 양념이 살 속까지 배어 밥반찬으로 특히 잘 어울립니다.</p>"),
  ("이런 분께 추천", L("쫄깃한 식감을 좋아하는 분","밥과 함께 든든하게 드실 분","부드러운 생선보다 씹는 맛을 좋아하는 분")),
  ("더 보기", L(A("sokcho-kodari-jjim","속초 코다리찜 메뉴"), A("kodari-jjim-how-to-eat","코다리찜 먹는 법"), A("myeongtae-names","명태 이름 정리")))],
 [SIZE, TOGO])

add("modeum-gui-taste", "모듬생선구이 맛", "메뉴", "gui.jpg",
 "껍질은 바삭, 살은 촉촉. 맵지 않은 모듬생선구이.",
 [("담백하고 고소해요",
   "<p>모듬생선구이는 여러 생선을 노릇하게 구워 한 접시에 담은 메뉴입니다. 껍질은 바삭하고 살은 촉촉해 맵지 않은 메뉴를 찾는 분과 아이에게 잘 맞습니다.</p>"),
  ("찜과 함께라면", "<p>매콤한 찜 사이에 담백한 구이를 곁들이면 입맛이 계속 살아납니다.</p>"),
  ("더 보기", L(A("sokcho-saengseon-gui","속초 생선구이 메뉴"), A("saengseon-gui-kinds","생선구이 종류"), A("jjim-gui-together","생선찜 생선구이 같이")))],
 [("맵나요?","아니요, 맵지 않습니다."), TOGO])

add("abai-sundae-how-to-eat", "아바이순대 먹는 법", "메뉴", "abai-sundae.jpg",
 "굵직한 아바이순대, 더 맛있게 먹는 방법.",
 [("따뜻할 때 한 점",
   "<p>아바이순대는 찹쌀과 선지로 속을 채운 굵은 순대라, 따뜻할 때 드셔야 속이 촉촉하고 고소합니다.</p>"),
  ("이렇게 드셔 보세요", L("함께 나오는 양념에 살짝 찍어서","매콤한 찜 사이사이 입가심으로","포장했다면 팬에 살짝 부쳐 고소하게")),
  ("더 보기", L(A("sokcho-abai-sundae","속초 아바이순대 메뉴"), A("abai-sundae-story","아바이순대 이야기"), A("abai-sundae-takeout","아바이순대 포장")))],
 [("맵나요?","아니요, 맵지 않습니다."), TOGO])

add("squid-sundae-taste", "오징어순대 맛", "메뉴", "squid-sundae2.jpg",
 "쫄깃한 오징어에 고소한 속. 오징어순대는 이런 맛이에요.",
 [("쫄깃함과 고소함",
   "<p>오징어순대는 쫄깃한 오징어 몸통 안에 고소한 속을 채워 만든 속초의 별미입니다. 대포항생선찜본점의 누룽지 오징어순대는 겉을 바삭하게 부쳐 식감이 하나 더 더해집니다.</p>"),
  ("가격", f"<p>{A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}는 17,000원입니다.</p>"),
  ("더 보기", L(A("nurungji-ojingeo-sundae-how-to-eat","누룽지 오징어순대 먹는 법"), A("ojingeo-sundae-story","오징어순대 이야기")))],
 [("맵나요?","맵지 않아 아이도 잘 먹습니다."), TOGO])

add("jjim-sulanju", "생선찜 술안주", "메뉴", "jjim-closeup.jpg",
 "소주 한잔에 매콤한 생선찜. 여행지 저녁 술안주로.",
 [("한잔 곁들이기 좋은 메뉴",
   L(A("sokcho-daegu-ppol-jjim","대구뽈찜")+": 쫀득한 볼살이 안주로 딱", A("sokcho-gaori-jjim","가오리찜")+": 오독오독 연골 씹는 맛", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 바삭한 한 점")),
  ("숙소에서 한잔이라면", "<p>전 메뉴 포장되니 숙소에서 편하게 드셔도 좋습니다.</p>"),
  ("더 보기", L(A("daepohang-anju","대포항 술안주"), A("sokcho-haejang","속초 해장 식사")))],
 [TOGO, HOURS])

add("kids-fish-dish", "아이가 먹기 좋은 생선 요리", "메뉴", "gui.jpg",
 "생선 잘 안 먹는 아이도 잘 먹는 메뉴가 있어요.",
 [("맵지 않은 메뉴",
   L(A("sokcho-saengseon-gui","모듬생선구이")+": 살이 촉촉하고 고소해요", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 바삭해서 아이들이 좋아해요", A("sokcho-abai-sundae","아바이순대")+": 맵지 않고 든든해요")),
  ("가시는 이렇게", f"<p>구이는 등뼈를 따라 살을 발라 주시면 됩니다. {A('saengseon-gasi-tip','생선 가시 바르는 법')}도 참고하세요.</p>"),
  ("더 보기", L(A("sokcho-kids-matjip","속초 아이랑 맛집"), A("sokcho-baby-matjip","아기랑 속초 맛집")))],
 [BABY, TOGO])

add("soft-fish-dish", "부드러운 생선 요리", "메뉴", "jjim-table.jpg",
 "치아가 약한 어르신도 편하게. 부드럽게 익은 생선찜과 무.",
 [("푹 익어 부드러워요",
   "<p>생선찜은 생선과 무를 양념에 푹 쪄내 살과 무가 부드럽습니다. 어르신과 함께라면 무와 생선살을 밥에 얹어 편하게 드실 수 있습니다.</p>"),
  ("어르신께 추천", L(A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-saengseon-gui","생선구이")+" (맵지 않아요)", A("sokcho-abai-sundae","아바이순대"))),
  ("더 보기", L(A("saengseon-jjim-mu","생선찜 무"), A("daepohang-parents","대포항 부모님 식사")))],
 [SIZE, PARK])

# ---------- 대포항 ----------
add("daepohang-afternoon", "대포항 오후", "대포항", "storefront.jpg",
 "느지막한 오후 대포항, 항구 구경과 늦은 식사.",
 [("오후의 대포항",
   "<p>오후에는 항구를 천천히 둘러보고 튀김골목에서 간식을 즐기기 좋습니다. 점심을 놓쳤다면 늦은 식사로 생선찜을 드셔 보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-late-lunch","속초 늦은 점심"), A("daepohang-walk","대포항 산책")))],
 [HOURS, OFF])

add("daepohang-spring", "봄 대포항", "대포항", "gaori-jjim.jpg",
 "바닷바람이 부드러워지는 봄, 대포항 산책과 생선찜.",
 [("봄의 대포항",
   "<p>봄이 오면 바닷바람이 한결 부드러워져 항구를 걷기 좋습니다. 산책 뒤 따뜻한 찜으로 식사하세요.</p>"),
  ("봄 한 상", MENU_LINKS),
  ("더 보기", L(A("sokcho-spring-matjip","속초 봄 맛집"), A("sokcho-april-matjip","4월 속초 맛집")))],
 [OFF, TOGO])

add("daepohang-summer", "여름 대포항", "대포항", "storefront.jpg",
 "해수욕 마치고 대포항으로. 여름 저녁 생선찜 한 상.",
 [("여름의 대포항",
   "<p>여름엔 근처 해변에서 물놀이를 마치고 대포항으로 저녁 먹으러 오는 분이 많습니다. 해가 길어 식사 후 항구 산책도 즐기기 좋습니다.</p>"),
  ("여름 추천", L(A("sokcho-saengseon-gui","생선구이")+": 가볍게", A("sokcho-gaori-jjim","가오리찜")+": 든든하게", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 간식처럼")),
  ("더 보기", L(A("sokcho-summer-matjip","속초 여름 맛집"), A("sokcho-beach-matjip","속초해수욕장 근처 맛집")))],
 [PARK, OFF])

add("daepohang-couple", "대포항 커플 식사", "대포항", "jjim-closeup.jpg",
 "둘이 걷는 대포항, 소 사이즈 생선찜으로 딱 맞는 한 끼.",
 [("둘이라면 소 사이즈",
   f"<p>찜은 소 사이즈가 2인이라 커플에게 딱 맞습니다. {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 하나 곁들이면 더 풍성해집니다.</p>"),
  ("커플 코스", L("항구 산책","생선찜 식사","튀김골목 간식","야경 구경")),
  ("더 보기", L(A("daepohang-date","대포항 데이트"), A("sokcho-couple-trip","속초 커플 여행 맛집")))],
 [SIZE, OFF])

add("daepohang-first-visit", "대포항 처음 가는 분", "대포항", "storefront.jpg",
 "대포항이 처음이라면, 이것만 알고 오세요.",
 [("처음 오신다면",
   L("주차는 "+A("daepohang-parking","공영주차장")+" 이용","항구 한 바퀴는 걸어서 충분해요","식사는 생선찜, 간식은 튀김골목","수요일은 저희 가게 휴무예요")),
  ("뭘 먹을지 모르겠다면", f"<p>처음이라면 {A('sokcho-gaori-jjim','가오리찜')}이나 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}을 추천합니다.</p>"),
  ("더 보기", L(A("daepohang-directions","대포항 가는 법"), A("daepohang-course","대포항 구경 코스")))],
 [WHERE, OFF])

add("daepohang-meokgeori", "대포항 먹거리", "대포항", "squid-sundae.jpg",
 "대포항에 오면 뭘 먹을까? 대포항 먹거리 정리.",
 [("대포항에서 먹을 것",
   L("생선찜: "+A("sokcho-gaori-jjim","가오리찜")+", "+A("sokcho-saengseon-modeum-jjim","생선모듬찜"),"생선구이: "+A("sokcho-saengseon-gui","모듬생선구이"),"순대: "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+", "+A("sokcho-abai-sundae","아바이순대"),"간식: "+A("daepohang-twigim","튀김골목"))),
  ("한 곳에서 여러 가지", "<p>대포항생선찜본점에서는 찜, 구이, 순대를 한 상에서 맛볼 수 있습니다.</p>"),
  ("더 보기", L(A("sokcho-food","속초 먹거리"), A("daepohang-not-hoe","대포항 회 말고 먹을거")))],
 [WHERE, TOGO])

add("daepohang-lodging-dinner", "대포항 숙소 근처 식당", "대포항", "hall2.jpg",
 "대포항 근처 숙소에 묵는다면, 걸어서 저녁 먹으러.",
 [("숙소에서 가까운 저녁",
   "<p>대포항 주변 숙소에 묵는다면 저녁 먹으러 항구 쪽으로 걸어 나와 보세요. 식사 후 항구 야경까지 즐길 수 있습니다.</p>"),
  ("숙소로 포장도", f"<p>전 메뉴 포장되니 전화({TEL})로 주문하고 숙소에서 드셔도 됩니다.</p>"),
  ("더 보기", L(A("sokcho-stay-in-dinner","숙소에서 먹는 저녁"), A("daepohang-night","대포항 야경")))],
 [TOGO, OFF])

add("daepohang-weekday", "대포항 평일", "대포항", "hall.jpg",
 "붐비지 않는 평일 대포항, 여유롭게 생선찜.",
 [("평일이 좋은 이유",
   L("주차가 한결 수월해요","식당이 덜 붐벼 여유로워요","항구를 조용히 둘러볼 수 있어요")),
  ("평일 휴무 확인", "<p>대포항생선찜본점은 매주 수요일 휴무입니다. 수요일을 피해 오세요.</p>"),
  ("더 보기", L(A("sokcho-weekday-trip","속초 평일 여행"), A("daepohang-weekend","대포항 주말")))],
 [OFF, PARK])

add("daepohang-holiday", "대포항 연휴", "대포항", "hall3.jpg",
 "연휴에 붐비는 대포항, 미리 알아 두면 좋은 것.",
 [("연휴엔 이렇게",
   L("식사 시간을 조금 앞당기거나 늦추면 덜 기다려요","주차는 공영주차장, 일찍 오시면 수월해요","포장 주문으로 숙소에서 드셔도 좋아요")),
  ("연휴 영업", f"<p>명절이나 연휴 영업 여부는 전화({TEL})로 미리 확인해 주세요.</p>"),
  ("더 보기", L(A("sokcho-holiday","속초 명절 여행"), A("sokcho-chuseok","추석 속초 맛집")))],
 [TOGO, PARK])

add("daepohang-jjim-matjip", "대포항 찜 맛집", "대포항", "gaori-jjim.jpg",
 "대포항에서 찜 먹을 곳, 생선찜 전문 대포항생선찜본점.",
 [("찜 메뉴",
   L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-kodari-jjim","코다리찜"))),
  ("사이즈", L("소: 2인","중: 3인","대: 4인")),
  ("더 보기", L(A("sokcho-jjim-matjip","속초 찜 맛집"), A("daepohang-saengseon-jjim","대포항 생선찜")))],
 [WHERE, OFF])

# ---------- 근처 ----------
add("sokcho-cityhall-matjip", "속초시청 근처 맛집", "근처", "jjim-table.jpg",
 "시청 쪽에서 볼일 보고, 대포항 생선찜으로 한 끼.",
 [("시내에서 대포항으로",
   "<p>시청이 있는 시내에서 남쪽으로 내려오면 대포항에 닿습니다. 볼일을 마치고 점심이나 저녁으로 들르기 좋습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("joyangdong-matjip","조양동 맛집"), A("sokcho-office-lunch","속초 직장인 점심")))],
 [WHERE, PARK])

add("sokcho-emart-matjip", "속초 이마트 근처 맛집", "근처", "hall2.jpg",
 "장 보러 나온 김에, 대포항까지 생선찜 먹으러.",
 [("장보기 전후 한 끼",
   "<p>속초 시내에서 장을 보고 대포항 쪽으로 내려와 식사하는 코스입니다. 숙소 장보기 전에 든든하게 드셔도 좋습니다.</p>"),
  ("포장도 돼요", "<p>전 메뉴 포장되니 장 본 짐과 함께 숙소로 가져가셔도 됩니다.</p>"),
  ("더 보기", L(A("sokcho-takeout-matjip","속초 포장 맛집"), A("sokcho-stay-in-dinner","숙소에서 먹는 저녁")))],
 [TOGO, PARK])

add("seorak-beach-matjip", "설악해변 근처 맛집", "근처", "storefront.jpg",
 "설악해변에서 바다 보고, 속초 대포항으로 생선찜.",
 [("해변에서 항구로",
   "<p>설악해변은 속초 남쪽 바닷가입니다. 바닷가 길을 따라 북쪽으로 올라오면 대포항에 닿습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("mulchihang-matjip","물치항 근처 맛집"), A("oeongchi-matjip","외옹치 맛집")))],
 [WHERE, PARK])

add("naksan-beach-matjip", "낙산해수욕장 근처 맛집", "근처", "jjim-closeup.jpg",
 "낙산해수욕장 물놀이 뒤, 속초 대포항에서 저녁.",
 [("양양에서 속초로",
   "<p>낙산해수욕장은 양양의 대표 해변입니다. 물놀이를 마치고 바닷가 길을 따라 속초로 올라와 저녁을 드셔 보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("naksansa-matjip","낙산사 가는 길 맛집"), A("sokcho-yangyang-course","속초 양양 여행 코스")))],
 [PARK, OFF])

add("ramada-sokcho-matjip", "라마다 속초 근처 맛집", "근처", "hall.jpg",
 "라마다 속초에 묵는다면, 대포항 생선찜으로 저녁.",
 [("숙소에서 나와 한 끼",
   "<p>속초 바닷가 호텔에 묵으면서 저녁은 항구 쪽 식당에서 드시는 분이 많습니다. 대포항은 속초 남쪽 바닷가에 있습니다.</p>"),
  ("숙소로 포장", "<p>전 메뉴 포장되니 객실에서 드셔도 좋습니다.</p>"),
  ("더 보기", L(A("sokcho-stay-in-dinner","숙소에서 먹는 저녁"), A("sokcho-beach-matjip","속초해수욕장 근처 맛집")))],
 [TOGO, WHERE])

add("deungdae-beach-matjip", "속초 등대해수욕장 맛집", "근처", "storefront.jpg",
 "등대해변 바다 보고, 대포항까지 내려와 생선찜.",
 [("북쪽 바다에서 남쪽 항구로",
   "<p>등대해수욕장은 속초 북쪽 영금정 근처의 작은 해변입니다. 시내를 지나 남쪽 대포항으로 내려오면 됩니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-lighthouse-matjip","속초등대 맛집"), A("yeonggeumjeong-matjip","영금정 근처 맛집")))],
 [WHERE, PARK])

add("misiryeong-matjip", "미시령 넘어 속초 맛집", "근처", "jjim-table.jpg",
 "미시령 넘어 속초 도착, 첫 끼는 대포항 생선찜.",
 [("고개 넘어 바다로",
   "<p>미시령을 넘어오면 속초 시내와 바다가 펼쳐집니다. 긴 길을 달려왔다면 첫 끼는 든든한 생선찜으로 하세요.</p>"),
  ("도착하면 이것", MENU_LINKS),
  ("더 보기", L(A("seoul-to-sokcho","서울에서 속초"), A("sokcho-drive","속초 드라이브 코스")))],
 [PARK, OFF])

add("hangyeryeong-matjip", "한계령 넘어 속초 맛집", "근처", "jjim-closeup.jpg",
 "한계령 굽잇길 드라이브 끝, 속초 바다와 생선찜.",
 [("산길 드라이브 뒤 한 끼",
   "<p>한계령은 설악산을 넘는 고갯길로 풍경이 아름다운 드라이브 코스입니다. 고개를 넘어 바다 쪽으로 내려오면 대포항에서 식사하기 좋습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("sokcho-drive","속초 드라이브 코스"), A("seorak-danpung-matjip","설악산 단풍 맛집")))],
 [PARK, OFF])

add("jumunjin-matjip", "주문진 여행 속초 맛집", "근처", "storefront.jpg",
 "주문진 구경하고 속초로, 동해안 항구 여행.",
 [("항구에서 항구로",
   "<p>주문진과 속초는 동해안 항구를 따라 함께 여행하기 좋은 곳입니다. 주문진에서 북쪽으로 올라와 속초 대포항에서 생선찜으로 마무리하세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("gangneung-sokcho-trip","강릉 속초 여행"), A("sokcho-yangyang-course","속초 양양 여행 코스")))],
 [WHERE, PARK])

add("sokcho-intercity-terminal-matjip", "속초 시외버스터미널 근처 맛집", "근처", "hall2.jpg",
 "버스로 속초 도착, 대포항 생선찜으로 여행 시작.",
 [("버스 여행이라면",
   "<p>시외버스터미널에 도착하면 시내버스나 택시로 대포항까지 이동할 수 있습니다. 짐이 많다면 식사 후 포장도 가능합니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-terminal-matjip","속초 고속버스터미널 근처 맛집"), A("sokcho-bus-trip","버스로 속초 여행")))],
 [WHERE, TOGO])

# ---------- 상황 ----------
add("sokcho-office-lunch", "속초 직장인 점심", "상황", "jjim-table.jpg",
 "동료들과 점심 한 끼, 매콤한 생선찜으로 든든하게.",
 [("동료와 나눠 먹기",
   "<p>여럿이 함께하는 점심이라면 인원에 맞춰 찜 사이즈를 고르고 나눠 드시면 됩니다. 미리 전화로 주문하면 시간을 아낄 수 있습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("sokcho-lunch-matjip","속초 점심 맛집"), A("daepohang-lunch","대포항 점심")))],
 [SIZE, OFF])

add("sokcho-sanggyeonrye", "속초 상견례 식사", "상황", "hall3.jpg",
 "양가 어른들과 함께하는 자리, 정갈한 생선찜 한 상.",
 [("어른들이 좋아하시는 메뉴",
   L(A("sokcho-saengseon-modeum-jjim","생선모듬찜")+": 여러 생선을 한 번에", A("sokcho-saengseon-gui","생선구이")+": 맵지 않고 담백하게", A("sokcho-abai-sundae","아바이순대")+": 속초 옛 맛")),
  ("미리 문의하세요", f"<p>인원과 자리를 미리 전화({TEL})로 문의해 주세요.</p>"),
  ("더 보기", L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-jeopdae","속초 손님 접대 식당")))],
 [GROUP, PARK])

add("sokcho-templestay-meal", "속초 템플스테이 후 식사", "상황", "jjim-closeup.jpg",
 "조용한 산사에서 하루, 내려와서 바다 앞 생선찜.",
 [("산사에서 바다로",
   "<p>설악산 자락 절에서 템플스테이를 마치고 바다 쪽으로 내려오면 대포항에서 식사하기 좋습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("sinheungsa-matjip","신흥사 맛집"), A("sokcho-healing-trip","속초 힐링 여행")))],
 [PARK, OFF])

add("sokcho-graduation-trip", "속초 졸업 여행", "상황", "jjim-table.jpg",
 "친구들과 졸업 기념 속초 여행, 다 같이 나눠 먹는 생선찜.",
 [("여럿이 나눠 먹기",
   L("인원에 맞춰 찜 사이즈 고르기","곁들이로 "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"),"식사 뒤 항구 산책과 사진")),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-friends-trip","속초 친구여행 맛집"), A("sokcho-photo-spots","속초 사진 명소")))],
 [SIZE, OFF])

add("sokcho-after-suneung", "수능 끝나고 속초 여행", "상황", "squid-sundae.jpg",
 "수능 끝, 친구나 가족과 떠나는 속초 겨울 여행.",
 [("고생한 만큼 맛있게",
   "<p>수능을 마치고 바다를 보러 속초를 찾는 분이 많습니다. 겨울 바다 구경 뒤엔 뜨끈한 생선찜이 잘 어울립니다.</p>"),
  ("추천", L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"), A("sokcho-saengseon-gui","생선구이"))),
  ("더 보기", L(A("sokcho-winter-sea","속초 겨울바다 여행"), A("sokcho-november-matjip","11월 속초 맛집")))],
 [OFF, TOGO])

add("sokcho-hiking-club", "속초 산악회 식사", "상황", "hall3.jpg",
 "설악산 산행 마친 산악회, 다 같이 생선찜 한 상.",
 [("산행 뒤 단체 식사",
   "<p>산행을 마친 단체 손님은 큰 냄비 찜을 여러 개 놓고 나눠 드시면 좋습니다. 인원이 많다면 미리 전화로 알려 주세요.</p>"),
  ("추천", L(A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-gaori-jjim","가오리찜"), A("sokcho-abai-sundae","아바이순대"))),
  ("더 보기", L(A("ulsanbawi-matjip","울산바위 등산 후 맛집"), A("sokcho-club-trip","동호회 속초 여행 식당")))],
 [GROUP, PARK])

add("sokcho-mom-trip", "엄마랑 속초 여행", "상황", "gaori-jjim.jpg",
 "엄마와 단둘이 속초, 바다 보고 생선찜 한 상.",
 [("엄마와 둘이라면",
   f"<p>찜 소 사이즈가 2인이라 둘이 드시기 좋습니다. 맵지 않은 {A('sokcho-saengseon-gui','생선구이')}를 곁들여도 좋습니다.</p>"),
  ("모녀 코스", L("바다향기로 산책","대포항 생선찜","바다 보이는 카페")),
  ("더 보기", L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-walking-course","속초 걷기 좋은 길")))],
 [SIZE, OFF])

add("sokcho-dad-trip", "아빠랑 속초 여행", "상황", "jjim-closeup.jpg",
 "아빠와 함께하는 속초, 소주 한잔 곁들일 생선찜.",
 [("아빠가 좋아하실 메뉴",
   L(A("sokcho-daegu-ppol-jjim","대구뽈찜")+": 쫀득한 볼살", A("sokcho-kodari-jjim","코다리찜")+": 밥도둑", A("sokcho-abai-sundae","아바이순대")+": 속초 옛 맛")),
  ("함께 걷기", f"<p>식사 뒤 {A('daepohang-walk','대포항 산책')}으로 이야기 나누며 걸어 보세요.</p>"),
  ("더 보기", L(A("jjim-sulanju","생선찜 술안주"), A("sokcho-parents-day","어버이날 속초 식사")))],
 [SIZE, OFF])

add("sokcho-marathon-meal", "속초 마라톤 후 식사", "상황", "jjim-table.jpg",
 "속초에서 달리고 난 뒤, 든든하게 생선찜으로 회복.",
 [("달린 뒤엔 든든하게",
   "<p>바닷가를 달리는 대회나 러닝을 마친 뒤엔 든든한 식사가 필요합니다. 밥과 함께 드시는 생선찜이면 배부르게 드실 수 있습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("sokcho-cycling-trip","동해안 자전거 여행 식사"), A("sokcho-group-restaurant","속초 단체 식당")))],
 [GROUP, PARK])

add("sokcho-after-work-dinner", "속초 퇴근 후 저녁", "상황", "hall2.jpg",
 "하루 일 마치고 동료나 가족과, 대포항 생선찜 한 끼.",
 [("퇴근길 한 끼",
   "<p>퇴근 후 가족이나 동료와 함께 든든한 저녁을 드시기 좋습니다. 바쁘다면 전화로 미리 주문하고 포장해 가셔도 됩니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("sokcho-dinner-matjip","속초 저녁 맛집"), A("daepohang-dinner","대포항 저녁")))],
 [HOURS, TOGO])

# ---------- 여행 ----------
add("gwangju-to-sokcho", "광주에서 속초 여행", "여행", "storefront.jpg",
 "광주에서 동해까지, 먼 길 끝 속초 생선찜 한 상.",
 [("먼 길 오시는 분께",
   "<p>광주에서 속초는 먼 여정이라 1박 이상 머무는 분이 많습니다. 도착한 날이나 떠나는 날, 대포항에서 생선찜을 드셔 보세요.</p>"),
  ("꼭 먹을 것", MENU_LINKS),
  ("더 보기", L(A("sokcho-2bak3il","속초 2박3일 코스"), A("sokcho-food-course","속초 먹방 코스")))],
 [WHERE, OFF])

add("incheon-to-sokcho", "인천에서 속초 여행", "여행", "jjim-table.jpg",
 "서해에서 동해로, 인천에서 떠나는 속초 여행.",
 [("서해와 다른 동해",
   "<p>인천에서 속초로 오면 서해와 다른 맑고 깊은 동해 바다를 만날 수 있습니다. 동해 생선으로 만든 찜도 꼭 맛보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("donghae-fish","동해안 생선 종류"), A("sokcho-1bak2il","속초 1박2일 코스")))],
 [WHERE, PARK])

add("wonju-to-sokcho", "원주에서 속초 여행", "여행", "gaori-jjim.jpg",
 "같은 강원도, 원주에서 속초 바다 보러.",
 [("가까운 강원도 바다",
   "<p>원주에서 속초는 당일치기로도 많이 오는 바다 여행지입니다. 바다 구경하고 대포항에서 점심이나 저녁을 드셔 보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-day-trip","속초 당일치기"), A("chuncheon-to-sokcho","춘천에서 속초 여행")))],
 [PARK, OFF])

add("cheongju-to-sokcho", "청주에서 속초 여행", "여행", "storefront.jpg",
 "청주에서 속초로, 바다 없는 동네에서 떠나는 바다 여행.",
 [("바다 보러 속초로",
   "<p>청주에서 속초까지 바다를 보러 오는 분이 많습니다. 바다 구경과 함께 동해 생선으로 만든 찜을 드셔 보세요.</p>"),
  ("꼭 먹을 것", MENU_LINKS),
  ("더 보기", L(A("daejeon-to-sokcho","대전에서 속초 여행"), A("sokcho-first-trip","속초 처음 여행")))],
 [WHERE, OFF])

add("sokcho-course-recommend", "속초 여행 코스 추천", "여행", "storefront.jpg",
 "산, 호수, 항구. 속초 여행 코스 한 번에 짜기.",
 [("하루 코스 예시",
   L("오전: 설악산 소공원이나 케이블카","점심: 대포항 "+A("sokcho-gaori-jjim","가오리찜"),"오후: 영랑호·청초호 산책","저녁: 대포항 튀김과 야경")),
  ("식사는 여기서", MENU_LINKS),
  ("더 보기", L(A("sokcho-1bak2il","속초 1박2일 코스"), A("sokcho-attractions","속초 가볼만한곳")))],
 [PARK, OFF])

add("sokcho-winter-course", "속초 겨울 여행 코스", "여행", "jjim-closeup.jpg",
 "겨울 속초, 해돋이부터 따뜻한 생선찜까지.",
 [("겨울 하루 코스",
   L("아침: 해돋이 보기","점심: 따뜻한 "+A("sokcho-daegu-ppol-jjim","대구뽈찜"),"오후: 바다 보이는 카페","저녁: 항구 야경 산책")),
  ("따뜻하게 챙길 것", L("두꺼운 겉옷과 장갑","바닷바람 막을 모자","따뜻한 국물 있는 찜 한 상")),
  ("더 보기", L(A("sokcho-winter-sea","속초 겨울바다 여행"), A("sokcho-winter-matjip","속초 겨울 맛집")))],
 [OFF, TOGO])

add("sokcho-1bak2il-matjip", "속초 1박2일 맛집", "여행", "gaori-jjim.jpg",
 "1박2일 속초 여행, 한 끼는 꼭 생선찜으로.",
 [("1박2일 식사 계획",
   L("첫날 저녁: 대포항 생선찜","둘째 날 아침: 숙소에서 간단히","둘째 날 점심: 아바이마을 순대나 시장 구경")),
  ("생선찜 추천", MENU_LINKS),
  ("더 보기", L(A("sokcho-1bak2il","속초 1박2일 코스"), A("sokcho-food-course","속초 먹방 코스")))],
 [WHERE, OFF])

# ---------- 제철 ----------
add("sokcho-july-matjip", "7월 속초 맛집", "제철", "storefront.jpg",
 "해수욕장 문 여는 7월 속초, 물놀이 뒤 생선찜.",
 [("7월의 속초",
   "<p>7월이면 해수욕장이 문을 열고 여름 여행객이 늘어납니다. 물놀이를 마친 저녁엔 든든한 찜으로 식사하세요.</p>"),
  ("여름 한 상", MENU_LINKS),
  ("더 보기", L(A("sokcho-summer-matjip","속초 여름 맛집"), A("daepohang-summer","여름 대포항")))],
 [PARK, OFF])

add("sokcho-august-matjip", "8월 속초 맛집", "제철", "hall.jpg",
 "한여름 휴가철 속초, 붐빌 때 알아 두면 좋은 식사 팁.",
 [("휴가철엔 이렇게",
   L("식사 시간을 조금 앞당기거나 늦추면 덜 기다려요","포장해서 숙소에서 드셔도 좋아요","주차는 공영주차장, 일찍 오시면 수월해요")),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-july-matjip","7월 속초 맛집"), A("sokcho-takeout-matjip","속초 포장 맛집")))],
 [TOGO, PARK])

add("sokcho-september-matjip", "9월 속초 맛집", "제철", "gaori-jjim.jpg",
 "선선해진 9월 속초, 여유로운 바다와 생선찜.",
 [("9월의 속초",
   "<p>9월은 여름 성수기가 지나 바다가 한결 여유롭고, 선선한 바람에 걷기 좋은 때입니다.</p>"),
  ("가을 문턱 한 상", MENU_LINKS),
  ("더 보기", L(A("sokcho-autumn-matjip","속초 가을 맛집"), A("sokcho-october-matjip","10월 속초 맛집")))],
 [OFF, TOGO])

assert len(P) == 50, len(P)
