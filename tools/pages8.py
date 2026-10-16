# 50 more keyword pages (added 2026-10-16). Same shape as pages2-7.
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
PET = ("반려동물 동반 되나요?","네, 반려동물과 함께 오실 수 있습니다.")

# ---------- 메뉴 ----------
add("gaori-vs-kodari", "가오리찜 코다리찜 차이", "메뉴", "gaori-jjim.jpg",
 "둘 다 매콤한 찜인데 뭐가 다를까? 가오리찜과 코다리찜 비교.",
 [("식감이 달라요",
   L(A("sokcho-gaori-jjim","가오리찜")+": 쫄깃한 살과 오독오독한 연골, 가시 걱정이 적어요", A("sokcho-kodari-jjim","코다리찜")+": 반건조 명태라 꾸덕하고 쫄깃, 밥반찬으로 좋아요")),
  ("이렇게 고르세요", L("연골 씹는 맛을 좋아하면 가오리찜","밥이랑 든든하게 먹고 싶으면 코다리찜","둘 다 궁금하면 일행과 하나씩")),
  ("더 보기", L(A("gaori-jjim-taste","가오리찜 맛"), A("kodari-jjim-taste","코다리찜 맛")))],
 [SIZE, ("둘 다 맵나요?","둘 다 칼칼한 양념입니다.")])

add("daegu-ppol-vs-gaori", "대구뽈찜 가오리찜 비교", "메뉴", "jjim-closeup.jpg",
 "대구뽈찜이냐 가오리찜이냐, 고민될 때 보는 비교.",
 [("두 찜의 차이",
   L(A("sokcho-daegu-ppol-jjim","대구뽈찜")+": 쫀득한 볼살과 말랑한 껍질, 발라 먹는 재미", A("sokcho-gaori-jjim","가오리찜")+": 쫄깃한 살과 연골, 한 번에 집어 먹기 편해요")),
  ("상황별 추천", L("술안주라면 대구뽈찜","처음 오셨다면 가오리찜","여럿이라면 둘 다 시켜 나눠 드세요")),
  ("더 보기", L(A("daegu-ppol-taste","대구뽈찜 맛"), A("gaori-vs-kodari","가오리찜 코다리찜 차이")))],
 [SIZE, TOGO])

add("jjim-or-gui", "생선찜 생선구이 고르기", "메뉴", "gui.jpg",
 "매콤한 찜, 담백한 구이. 오늘은 뭘 먹을까?",
 [("찜이 좋은 날",
   L("밥과 함께 든든하게 먹고 싶을 때","매콤한 게 당길 때","여럿이 냄비 하나를 나눠 먹을 때")),
  ("구이가 좋은 날", L("맵지 않은 음식이 필요할 때","아이와 함께일 때","가볍게 먹고 싶을 때")),
  ("둘 다 먹고 싶다면", f"<p>찜 하나에 구이 하나를 곁들이면 맵고 담백한 맛을 번갈아 즐길 수 있습니다. {A('jjim-gui-together','생선찜 생선구이 같이')}도 참고하세요.</p>")],
 [("구이는 맵나요?","아니요, 맵지 않습니다."), SIZE])

add("modeum-or-gaori", "생선모듬찜 가오리찜 고르기", "메뉴", "jjim-table.jpg",
 "여러 생선을 맛볼까, 대표 메뉴 하나에 집중할까?",
 [("모듬찜이 맞는 분",
   L("여러 생선을 조금씩 맛보고 싶은 분","일행마다 입맛이 다른 경우","처음 와서 고르기 어려운 분")),
  ("가오리찜이 맞는 분", L("쫄깃한 식감을 좋아하는 분","가시 바르기가 번거로운 분","대표 메뉴를 먹어 보고 싶은 분")),
  ("더 보기", L(A("modeum-jjim-guide","생선모듬찜 고르는 이유"), A("gaori-jjim-taste","가오리찜 맛")))],
 [SIZE, OFF])

add("sokcho-fish-recommend", "속초 생선 요리 추천", "메뉴", "jjim-table.jpg",
 "속초에서 생선 요리 먹는다면, 이것부터 드셔 보세요.",
 [("추천 순서",
   L("1. "+A("sokcho-gaori-jjim","가오리찜")+": 대표 메뉴","2. "+A("sokcho-saengseon-modeum-jjim","생선모듬찜")+": 여러 생선을 한 번에","3. "+A("sokcho-saengseon-gui","모듬생선구이")+": 맵지 않은 메뉴","4. "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 곁들이로")),
  ("회 말고 생선", f"<p>회 말고도 속초에는 찜과 구이처럼 익혀 먹는 생선 요리가 많습니다. {A('daepohang-not-hoe','대포항 회 말고 먹을거')}도 참고하세요.</p>"),
  ("더 보기", L(A("sokcho-fish-dishes","속초 생선요리"), A("donghae-fish","동해안 생선 종류")))],
 [WHERE, OFF])

add("sokcho-jjim-3in", "속초 3인 생선찜", "메뉴", "jjim-table.jpg",
 "셋이서 속초 여행, 생선찜은 중 사이즈로.",
 [("셋이라면 중 사이즈",
   "<p>찜은 중 사이즈가 3인 기준입니다. 양이 많은 일행이라면 곁들이 메뉴를 하나 더하세요.</p>"),
  ("3인 추천 조합", L(A("sokcho-gaori-jjim","가오리찜")+" 중 + "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"), A("sokcho-saengseon-modeum-jjim","생선모듬찜")+" 중 + "+A("sokcho-saengseon-gui","생선구이"))),
  ("더 보기", L(A("sokcho-jjim-2in","속초 2인 생선찜"), A("sokcho-jjim-4in","속초 4인 가족 생선찜")))],
 [SIZE, TOGO])

add("sokcho-jjim-5in", "속초 5인 가족 식사", "메뉴", "hall.jpg",
 "다섯 식구 속초 여행, 생선찜 주문은 이렇게.",
 [("5인이라면",
   L("대(4인) 사이즈 + 곁들이 메뉴 하나","아이가 있다면 대 사이즈 + 맵지 않은 구이","어른 다섯이면 찜 두 가지를 섞어서")),
  ("곁들이", L(A("sokcho-nurungji-squid-sundae","누룽지 오징어순대 (17,000원)"), A("sokcho-abai-sundae","아바이순대"), A("sokcho-saengseon-gui","모듬생선구이"))),
  ("더 보기", L(A("jjim-size-guide","생선찜 사이즈 고르기"), A("sokcho-family-dining","속초 가족 외식")))],
 [SIZE, BABY])

add("sokcho-jjim-6in", "속초 6인 이상 식사", "메뉴", "hall3.jpg",
 "여섯 명 넘는 일행이라면, 찜 여러 가지를 나눠 드세요.",
 [("여럿이라면",
   L("찜 2~3가지를 사이즈별로 섞어 주문","맵지 않은 구이와 순대를 곁들이로","인원이 많으면 미리 전화로 문의")),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-group-restaurant","속초 단체 식당"), A("daepohang-group-dining","대포항 단체 식사")))],
 [GROUP, PARK])

add("jjim-gukmul", "생선찜 국물", "메뉴", "jjim-closeup.jpg",
 "자작하게 졸아든 생선찜 국물, 왜 이렇게 맛있을까?",
 [("자작한 양념 국물",
   "<p>생선찜은 국물이 많은 탕과 달리 자작하게 졸아든 양념이 특징입니다. 생선과 무에서 우러난 맛이 양념에 섞여 진하고 깊은 맛이 납니다.</p>"),
  ("국물 맛있게 먹기", L("밥 위에 한 숟가락씩 끼얹어서","양념 밴 무와 함께","마지막엔 밥을 비벼서")),
  ("더 보기", L(A("saengseon-jjim-yangnyeom","생선찜 양념 맛"), A("saengseon-jjim-bibim","생선찜 양념 밥 비벼먹기")))],
 [SIZE, OFF])

add("nurungji-sundae-price", "누룽지 오징어순대 가격", "메뉴", "squid-sundae.jpg",
 "대포항생선찜본점 누룽지 오징어순대는 17,000원이에요.",
 [("가격",
   f"<p>{A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}는 17,000원입니다. 오징어순대를 노릇하게 부쳐 겉은 바삭하고 속은 쫄깃합니다.</p>"),
  ("이렇게 드세요", L("찜과 함께 곁들이로","아이 메뉴로 (맵지 않아요)","포장해서 숙소 간식으로")),
  ("더 보기", L(A("squid-sundae-taste","오징어순대 맛"), A("nurungji-ojingeo-sundae-how-to-eat","누룽지 오징어순대 먹는 법")))],
 [("다른 메뉴 가격은?","매장이나 전화로 확인해 주세요."), TOGO])

# ---------- 대포항 ----------
add("daepohang-sunset", "대포항 해질녘", "대포항", "storefront.jpg",
 "하루가 저무는 대포항, 노을빛 항구 산책과 저녁.",
 [("해 질 무렵 대포항",
   "<p>해가 질 무렵 항구에 불이 하나둘 켜지기 시작하면 대포항은 또 다른 분위기가 됩니다. 산책 뒤 따뜻한 저녁을 드셔 보세요.</p>"),
  ("저녁 추천", MENU_LINKS),
  ("더 보기", L(A("daepohang-night","대포항 야경"), A("daepohang-dinner","대포항 저녁")))],
 [HOURS, OFF])

add("daepohang-photo", "대포항 사진 명소", "대포항", "storefront.jpg",
 "대포항에서 사진 찍기 좋은 곳, 그리고 사진 찍고 싶은 한 상.",
 [("찍기 좋은 장면",
   L("항구에 정박한 고깃배","방파제와 등대","불 밝힌 밤 항구","보글보글 끓는 찜 냄비")),
  ("가게 안 볼거리", f"<p>가게 안에는 사인볼이 가득한 벽이 있어 사진 찍는 분이 많습니다. {A('sokcho-ball-wall','사인볼 벽 식당')}도 참고하세요.</p>"),
  ("더 보기", L(A("sokcho-photo-spots","속초 사진 명소"), A("daepohang-walk","대포항 산책")))],
 [WHERE, OFF])

add("daepohang-fishing-boats", "대포항 고깃배 구경", "대포항", "storefront.jpg",
 "고깃배가 드나드는 대포항, 구경하고 생선 요리 한 끼.",
 [("항구의 풍경",
   "<p>대포항은 크지 않은 항구지만 고깃배가 드나들고 항구 특유의 활기가 있습니다. 아이와 함께 배 구경하기도 좋습니다.</p>"),
  ("구경하고 한 끼", MENU_LINKS),
  ("더 보기", L(A("daepohang-story","대포항 이야기"), A("donghae-fish","동해안 생선 종류")))],
 [PARK, OFF])

add("daepohang-1bak", "대포항 1박 여행", "대포항", "hall2.jpg",
 "대포항 근처에서 하룻밤, 저녁과 아침까지 알차게.",
 [("1박 일정 예시",
   L("오후: 대포항 구경과 튀김 간식","저녁: 생선찜","밤: 항구 야경 산책","다음 날 아침: 해돋이")),
  ("저녁은 포장도", "<p>전 메뉴 포장되니 숙소에서 편하게 드셔도 좋습니다.</p>"),
  ("더 보기", L(A("daepohang-lodging-dinner","대포항 숙소 근처 식당"), A("daepohang-sunrise","대포항 일출")))],
 [TOGO, OFF])

add("daepohang-drive", "대포항 드라이브", "대포항", "storefront.jpg",
 "바닷가 길 따라 대포항까지, 드라이브 끝 생선찜.",
 [("바닷가 드라이브",
   "<p>속초와 양양 사이 바닷가 길을 따라 달리면 대포항에 닿습니다. 차는 공영주차장에 세우고 항구를 걸어 보세요.</p>"),
  ("도착하면", MENU_LINKS),
  ("더 보기", L(A("sokcho-drive","속초 드라이브 코스"), A("daepohang-parking","대포항 주차")))],
 [PARK, OFF])

add("daepohang-bapjip", "대포항 밥집", "대포항", "jjim-table.jpg",
 "대포항에서 밥 먹을 곳, 밥도둑 생선찜이 있는 곳.",
 [("밥이 술술 넘어가요",
   "<p>생선찜은 밥 위에 생선살과 무를 올리고 양념을 끼얹어 먹는 음식이라 밥 한 공기가 금방 비워집니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-bapjip","속초 밥집"), A("sokcho-bapdoduk","속초 밥도둑 메뉴")))],
 [WHERE, OFF])

add("daepohang-hansik", "대포항 한식", "대포항", "jjim-closeup.jpg",
 "회 대신 한식 한 상, 대포항 생선찜과 구이.",
 [("한식 한 상",
   "<p>생선찜과 생선구이는 밥과 함께 먹는 한식 상차림입니다. 회가 부담스러운 분이나 어르신과 함께라면 더 잘 맞습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-hansik","속초 한식 맛집"), A("daepohang-not-hoe","대포항 회 말고 먹을거")))],
 [WHERE, PARK])

add("daepohang-family-trip", "대포항 가족여행", "대포항", "hall.jpg",
 "아이부터 어르신까지, 온 가족 대포항 여행.",
 [("가족 모두 먹을 메뉴",
   L("어른: "+A("sokcho-gaori-jjim","가오리찜")+", "+A("sokcho-saengseon-modeum-jjim","생선모듬찜"),"아이: "+A("sokcho-saengseon-gui","생선구이")+", "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"),"어르신: 부드러운 찜과 "+A("sokcho-abai-sundae","아바이순대"))),
  ("편의", L("아기의자 있어요","반려동물 동반 가능","전 메뉴 포장")),
  ("더 보기", L(A("daepohang-family-dining","대포항 가족 식사"), A("sokcho-family-trip","속초 가족여행 코스")))],
 [BABY, PET])

add("daepohang-abai-sundae", "대포항 아바이순대", "대포항", "abai-sundae.jpg",
 "아바이마을까지 안 가도, 대포항에서 맛보는 아바이순대.",
 [("대포항에서도 아바이순대",
   f"<p>대포항생선찜본점에서는 {A('sokcho-abai-sundae','속초아바이순대')}를 함께 냅니다. 찹쌀과 선지로 속을 채운 굵은 순대를 찜과 함께 드셔 보세요.</p>"),
  ("함께 먹기 좋은 메뉴", MENU_LINKS),
  ("더 보기", L(A("abai-sundae-story","아바이순대 이야기"), A("abai-sundae-how-to-eat","아바이순대 먹는 법")))],
 [("맵나요?","아니요, 맵지 않습니다."), TOGO])

add("daepohang-trip", "대포항 여행", "대포항", "storefront.jpg",
 "속초 남쪽 작은 항구 대포항, 여행 전에 알아 둘 것.",
 [("대포항 여행 요약",
   L("볼거리: 항구, 고깃배, 방파제, 야경","먹거리: 생선찜, 생선구이, 순대, 튀김","주차: 대포항 공영주차장","저희 가게 휴무: 매주 수요일")),
  ("식사는 여기서", MENU_LINKS),
  ("더 보기", L(A("daepohang-first-visit","대포항 처음 가는 분"), A("daepohang-attractions","대포항 가볼만한곳")))],
 [WHERE, PARK])

# ---------- 근처 ----------
add("haksapyeong-matjip", "학사평 근처 맛집", "근처", "jjim-table.jpg",
 "학사평 지나 바다로, 대포항 생선찜으로 한 끼.",
 [("산 쪽에서 바다 쪽으로",
   "<p>학사평은 설악산으로 가는 길목의 마을입니다. 순두부 말고 생선 요리가 당긴다면 바다 쪽 대포항으로 내려와 보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("domundong-matjip","속초 도문동 맛집"), A("seoraksan-matjip","설악산 근처 맛집")))],
 [WHERE, PARK])

add("seorak-sogongwon-matjip", "설악산 소공원 근처 맛집", "근처", "jjim-closeup.jpg",
 "소공원에서 산책 마치고, 대포항 생선찜으로 마무리.",
 [("산책 뒤 한 끼",
   "<p>설악산 소공원은 가볍게 걷기 좋은 설악산 입구입니다. 걷고 내려와 바다 쪽 대포항에서 식사하면 산과 바다를 하루에 즐길 수 있습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("seorak-cablecar-matjip","설악 케이블카 맛집"), A("sinheungsa-matjip","신흥사 맛집")))],
 [PARK, OFF])

add("namaehang-matjip", "남애항 여행 맛집", "근처", "storefront.jpg",
 "양양 남애항 구경하고 속초로, 항구에서 항구로.",
 [("양양 항구에서 속초 항구로",
   "<p>남애항은 양양 남쪽의 아담한 항구입니다. 바닷가 길을 따라 북쪽으로 올라오면 속초 대포항에 닿습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("hajodae-matjip","하조대 여행 맛집"), A("sokcho-yangyang-course","속초 양양 여행 코스")))],
 [WHERE, PARK])

add("jukdo-beach-matjip", "죽도해변 근처 맛집", "근처", "gui.jpg",
 "양양 죽도해변 서핑 마치고, 속초에서 든든한 저녁.",
 [("서핑 뒤 한 끼",
   "<p>죽도해변은 서핑으로 유명한 양양의 해변입니다. 물에서 나온 뒤엔 든든한 식사가 필요하니 속초 대포항으로 올라와 보세요.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("yangyang-surf-matjip","양양 서핑 후 맛집"), A("solbeach-yangyang-matjip","쏠비치 양양 근처 맛집")))],
 [PARK, TOGO])

add("ayajin-matjip", "아야진 여행 맛집", "근처", "storefront.jpg",
 "고성 아야진 맑은 바다 보고, 속초 대포항에서 식사.",
 [("고성에서 속초로",
   "<p>아야진은 물이 맑기로 알려진 고성의 바닷가입니다. 고성 바다를 보고 남쪽으로 내려와 속초에서 식사하기 좋습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("goseong-trip-matjip","고성 여행 속초 맛집"), A("hwajinpo-matjip","화진포 여행 맛집")))],
 [WHERE, PARK])

add("songjiho-matjip", "송지호 여행 맛집", "근처", "hall2.jpg",
 "고성 송지호 둘러보고, 속초로 내려와 생선찜.",
 [("호수와 바다 여행",
   "<p>송지호는 고성의 호수로 산책하기 좋은 곳입니다. 고성 여행을 마치고 속초로 내려오는 길에 대포항에서 식사하세요.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("ayajin-matjip","아야진 여행 맛집"), A("delpino-matjip","델피노 근처 맛집")))],
 [PARK, OFF])

add("mountain-museum-matjip", "국립산악박물관 근처 맛집", "근처", "hall.jpg",
 "산악박물관 구경하고, 바다 쪽 대포항에서 한 끼.",
 [("실내 구경 뒤 식사",
   "<p>국립산악박물관은 아이와 함께 실내에서 둘러보기 좋은 곳입니다. 구경을 마치고 대포항으로 내려와 식사해 보세요.</p>"),
  ("아이와 함께라면", L(A("sokcho-saengseon-gui","생선구이")+": 맵지 않아요", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 바삭해요","아기의자 있어요")),
  ("더 보기", L(A("nohakdong-matjip","속초 노학동 맛집"), A("sokcho-rainy-day-matjip","속초 비오는날 맛집")))],
 [BABY, PARK])

add("inje-trip-matjip", "인제 여행 속초 맛집", "근처", "jjim-table.jpg",
 "인제 계곡과 숲 여행 뒤, 고개 넘어 속초 바다로.",
 [("산에서 바다로",
   "<p>인제는 계곡과 숲으로 유명한 강원도 내륙입니다. 고개를 넘어 속초로 오면 바다와 함께 생선 요리를 즐길 수 있습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("hangyeryeong-matjip","한계령 넘어 속초 맛집"), A("misiryeong-matjip","미시령 넘어 속초 맛집")))],
 [WHERE, PARK])

add("osaek-matjip", "오색 여행 맛집", "근처", "jjim-closeup.jpg",
 "양양 오색 산행이나 온천 뒤, 속초 대포항에서 저녁.",
 [("오색에서 바다로",
   "<p>오색은 설악산 남쪽 자락의 산행 들머리이자 온천으로 알려진 곳입니다. 산에서 내려와 바다 쪽으로 오면 대포항에서 식사하기 좋습니다.</p>"),
  ("산행 뒤 추천", L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-abai-sundae","아바이순대"))),
  ("더 보기", L(A("hangyeryeong-matjip","한계령 넘어 속초 맛집"), A("sokcho-hiking-club","속초 산악회 식사")))],
 [PARK, OFF])

add("tongil-observatory-matjip", "통일전망대 여행 맛집", "근처", "storefront.jpg",
 "고성 통일전망대 다녀오는 길, 속초에서 생선찜.",
 [("최북단 여행 뒤",
   "<p>고성 통일전망대는 동해안 최북단 여행지입니다. 다녀오는 길에 남쪽으로 내려와 속초 대포항에서 식사하세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("goseong-trip-matjip","고성 여행 속초 맛집"), A("hwajinpo-matjip","화진포 여행 맛집")))],
 [WHERE, OFF])

# ---------- 상황 ----------
add("sokcho-wedding-anniversary", "속초 결혼기념일 식사", "상황", "gaori-jjim.jpg",
 "결혼기념일 둘만의 속초 여행, 바다 앞 생선찜 한 상.",
 [("둘이라면 소 사이즈",
   f"<p>찜 소 사이즈가 2인 기준입니다. {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 곁들이면 더 풍성한 한 상이 됩니다.</p>"),
  ("기념일 코스", L("바닷가 산책","대포항 생선찜","항구 야경")),
  ("더 보기", L(A("sokcho-anniversary","속초 기념일 식사"), A("sokcho-couple-trip","속초 커플 여행 맛집")))],
 [SIZE, OFF])

add("sokcho-hwangap", "속초 환갑 식사", "상황", "hall3.jpg",
 "환갑 맞은 부모님과 속초 여행, 온 가족 생선찜 한 상.",
 [("어른들이 좋아하시는 메뉴",
   L(A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-saengseon-gui","생선구이")+" (맵지 않아요)", A("sokcho-abai-sundae","아바이순대"))),
  ("미리 문의하세요", f"<p>인원이 많다면 미리 전화({TEL})로 알려 주세요.</p>"),
  ("더 보기", L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-family-gathering","속초 가족 모임 식당")))],
 [GROUP, PARK])

add("sokcho-chilsun", "속초 칠순 가족 식사", "상황", "hall.jpg",
 "칠순 맞은 부모님과 함께, 부드러운 생선찜 한 상.",
 [("어르신이 드시기 편한 메뉴",
   L("푹 익어 부드러운 찜과 무", A("sokcho-saengseon-gui","생선구이")+": 맵지 않고 담백", A("sokcho-abai-sundae","아바이순대")+": 속초 옛 맛")),
  ("가족이 많다면", f"<p>인원과 도착 시간을 미리 전화({TEL})로 알려 주세요.</p>"),
  ("더 보기", L(A("soft-fish-dish","부드러운 생선 요리"), A("sokcho-three-generations","3대 가족 속초 식사")))],
 [GROUP, BABY])

add("sokcho-dol-trip", "속초 돌 기념 여행", "상황", "hall2.jpg",
 "아기 첫 생일 기념 가족여행, 아기의자 있는 식당.",
 [("아기와 함께라면",
   L("아기의자 있어요","어른은 매콤한 찜, 아이는 맵지 않은 구이","포장해서 숙소에서 편하게 드셔도 돼요")),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-baby-matjip","아기랑 속초 맛집"), A("daepohang-with-kids","대포항 아이랑")))],
 [BABY, TOGO])

add("sokcho-mt", "속초 MT 식사", "상황", "jjim-table.jpg",
 "동아리나 과 MT로 속초, 다 같이 나눠 먹는 생선찜.",
 [("여럿이 나눠 먹기",
   L("찜 여러 가지를 사이즈별로","누룽지 오징어순대는 모두가 좋아해요","숙소로 포장도 가능")),
  ("단체라면", f"<p>인원이 많다면 미리 전화({TEL})로 문의해 주세요.</p>"),
  ("더 보기", L(A("sokcho-club-trip","동호회 속초 여행 식당"), A("sokcho-graduation-trip","속초 졸업 여행")))],
 [GROUP, TOGO])

add("sokcho-discharge-trip", "전역 기념 속초 여행", "상황", "jjim-closeup.jpg",
 "전역하고 떠나는 속초 여행, 든든한 생선찜으로 축하.",
 [("든든하게 한 끼",
   "<p>전역 기념 여행이라면 친구나 가족과 큰 냄비 찜을 나눠 먹으며 축하해 보세요.</p>"),
  ("추천", L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"))),
  ("더 보기", L(A("sokcho-friends-trip","속초 친구여행 맛집"), A("sokcho-military-visit","속초 면회 외식")))],
 [SIZE, OFF])

add("sokcho-taegyo-trip", "속초 태교여행 식사", "상황", "gui.jpg",
 "태교여행으로 속초, 맵지 않고 편안한 메뉴도 있어요.",
 [("편하게 드실 메뉴",
   L(A("sokcho-saengseon-gui","모듬생선구이")+": 맵지 않고 담백해요", A("sokcho-abai-sundae","아바이순대")+": 맵지 않아요", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 바삭하고 고소해요")),
  ("천천히 여유롭게", "<p>붐비는 식사 시간을 피하면 더 편하게 드실 수 있습니다. 포장해서 숙소에서 드셔도 좋습니다.</p>"),
  ("더 보기", L(A("sokcho-mild-menu","속초 안 매운 메뉴"), A("sokcho-healing-trip","속초 힐링 여행")))],
 [TOGO, PARK])

add("sokcho-new-year-party", "속초 신년회 식당", "상황", "hall3.jpg",
 "새해 첫 모임, 큰 냄비 생선찜 둘러앉아.",
 [("신년회 메뉴",
   L("찜 2~3가지를 섞어서", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+"는 안주로","맵지 않은 구이도 함께")),
  ("미리 문의하세요", f"<p>인원이 많다면 전화({TEL})로 미리 알려 주세요.</p>"),
  ("더 보기", L(A("sokcho-moim","속초 모임 식당"), A("sokcho-january-matjip","1월 속초 맛집")))],
 [GROUP, PARK])

add("sokcho-year-end-party", "속초 송년회 식당", "상황", "hall2.jpg",
 "한 해를 마무리하는 송년 모임, 생선찜 한 상.",
 [("송년회 메뉴",
   L(A("sokcho-daegu-ppol-jjim","대구뽈찜")+": 술안주로", A("sokcho-saengseon-modeum-jjim","생선모듬찜")+": 여럿이 나눠", A("sokcho-saengseon-gui","생선구이")+": 맵지 않은 메뉴")),
  ("미리 문의하세요", f"<p>연말엔 붐빌 수 있으니 전화({TEL})로 미리 문의해 주세요.</p>"),
  ("더 보기", L(A("sokcho-hoesik","속초 회식 장소"), A("sokcho-december-matjip","12월 속초 맛집")))],
 [GROUP, HOURS])

add("sokcho-campingcar", "속초 캠핑카 여행 음식", "상황", "gui.jpg",
 "캠핑카로 동해안 여행, 저녁은 포장 생선찜으로.",
 [("캠핑카 저녁",
   f"<p>전 메뉴 포장되니 캠핑카에서 드실 저녁으로 챙겨 가세요. 미리 전화({TEL})로 주문하면 바로 받아 가실 수 있습니다.</p>"),
  ("포장 추천", L(A("sokcho-saengseon-gui","생선구이")+": 국물 없어 편해요", A("sokcho-abai-sundae","아바이순대")+": 데워 먹기 쉬워요", A("sokcho-gaori-jjim","가오리찜")+": 냄비에 데워서")),
  ("더 보기", L(A("sokcho-chabak","속초 차박 음식"), A("sokcho-camping-takeout","속초 캠핑 포장 음식")))],
 [TOGO, PARK])

# ---------- 여행 ----------
add("ulsan-to-sokcho", "울산에서 속초 여행", "여행", "storefront.jpg",
 "울산에서 동해안 따라 속초까지, 바닷길 여행.",
 [("동해안 따라 올라오기",
   "<p>울산에서 속초는 동해안을 따라 올라오는 긴 여정입니다. 중간에 여러 바닷가를 들르며 천천히 오는 분이 많습니다.</p>"),
  ("속초에선 이것", MENU_LINKS),
  ("더 보기", L(A("busan-to-sokcho","부산에서 속초 여행"), A("pohang-to-sokcho","포항에서 속초 여행")))],
 [WHERE, OFF])

add("jeonju-to-sokcho", "전주에서 속초 여행", "여행", "jjim-table.jpg",
 "전주 한옥마을 다음은 속초 바다, 맛있는 도시 여행.",
 [("맛의 도시에서 바다로",
   "<p>전주에서 속초는 먼 길이라 1박 이상 머무는 분이 많습니다. 전주와는 또 다른 바닷가 음식을 맛보세요.</p>"),
  ("꼭 먹을 것", MENU_LINKS),
  ("더 보기", L(A("sokcho-food-course","속초 먹방 코스"), A("sokcho-2bak3il","속초 2박3일 코스")))],
 [WHERE, OFF])

add("suwon-to-sokcho", "수원에서 속초 여행", "여행", "gaori-jjim.jpg",
 "수원에서 주말 속초, 바다 보고 생선찜 한 상.",
 [("주말 바다 여행",
   "<p>수원에서 속초는 주말 1박이나 당일치기로 많이 오는 바다 여행지입니다. 점심이나 저녁으로 대포항 생선찜을 드셔 보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("gyeonggi-to-sokcho","경기도에서 속초 여행"), A("sokcho-day-trip","속초 당일치기")))],
 [PARK, OFF])

add("pohang-to-sokcho", "포항에서 속초 여행", "여행", "storefront.jpg",
 "포항에서 속초까지, 동해 바다를 따라 북쪽으로.",
 [("동해 바다 끝에서 끝으로",
   "<p>포항과 속초는 모두 동해 바다를 낀 도시입니다. 같은 동해지만 속초에서는 또 다른 생선 요리를 맛볼 수 있습니다.</p>"),
  ("속초에선 이것", MENU_LINKS),
  ("더 보기", L(A("ulsan-to-sokcho","울산에서 속초 여행"), A("donghae-fish","동해안 생선 종류")))],
 [WHERE, PARK])

add("sokcho-3person-trip", "속초 셋이서 여행", "여행", "jjim-table.jpg",
 "셋이 떠나는 속초, 생선찜 중 사이즈가 딱 맞아요.",
 [("셋이라면",
   L("찜은 중 사이즈(3인)","곁들이로 누룽지 오징어순대","식사 뒤 항구 산책")),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-jjim-3in","속초 3인 생선찜"), A("sokcho-friends-trip","속초 친구여행 맛집")))],
 [SIZE, OFF])

add("sokcho-trip-cost", "속초 여행 경비 아끼기", "여행", "hall2.jpg",
 "속초 여행 식비, 나눠 먹고 포장해서 알뜰하게.",
 [("식비 아끼는 법",
   L("찜은 인원에 맞는 사이즈로 나눠 먹기","남은 음식은 포장해서 다음 끼니로","숙소 저녁은 포장 주문으로")),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-budget-trip","속초 알뜰 여행"), A("sokcho-off-season","속초 비수기 여행")))],
 [SIZE, ("가격은?","메뉴판 가격은 매장이나 전화로 확인해 주세요.")])

add("sokcho-autumn-course", "속초 가을 여행 코스", "여행", "gaori-jjim.jpg",
 "단풍과 바다, 가을 속초 하루 코스.",
 [("가을 하루 코스",
   L("오전: 설악산 단풍 구경","점심: 대포항 "+A("sokcho-gaori-jjim","가오리찜"),"오후: 영랑호 산책","저녁: 항구 야경")),
  ("가을 한 상", MENU_LINKS),
  ("더 보기", L(A("seorak-danpung-matjip","설악산 단풍 맛집"), A("daepohang-autumn","가을 대포항")))],
 [PARK, OFF])

# ---------- 제철 ----------
add("donghae-winter-fish", "동해 겨울 생선", "제철", "jjim-closeup.jpg",
 "겨울에 더 맛있어지는 동해 생선들.",
 [("겨울 동해 생선",
   L("명태: 동해 겨울을 대표하던 생선, 코다리와 황태로도 먹어요","대구: 겨울이 제철, 뽈찜과 탕으로","도루묵: 초겨울 알이 꽉 찬 별미")),
  ("겨울 메뉴", L(A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-kodari-jjim","코다리찜"), A("sokcho-saengseon-gui","모듬생선구이"))),
  ("더 보기", L(A("sokcho-jecheol-saengseon","속초 제철 생선"), A("myeongtae-names","명태 이름 정리")))],
 [("구이에 어떤 생선이 나오나요?",f"그날 들어온 생선에 따라 다릅니다. 전화({TEL})로 물어보세요."), OFF])

add("dorumuk-season", "도루묵 제철", "제철", "gui.jpg",
 "초겨울 동해안 별미 도루묵, 언제 먹으면 좋을까?",
 [("초겨울 별미",
   "<p>도루묵은 초겨울 동해안에서 많이 잡히는 생선으로, 알이 꽉 찬 때 구이나 찌개로 즐겨 먹습니다.</p>"),
  ("생선구이로", f"<p>대포항생선찜본점의 {A('sokcho-saengseon-gui','모듬생선구이')} 구성은 그날 들어온 생선에 따라 달라집니다. 도루묵이 궁금하다면 전화({TEL})로 물어보세요.</p>"),
  ("더 보기", L(A("saengseon-gui-kinds","생선구이 종류"), A("donghae-winter-fish","동해 겨울 생선")))],
 [("도루묵 메뉴가 있나요?","그날 들어온 생선에 따라 달라 전화로 확인해 주세요."), OFF])

add("sokcho-four-seasons", "속초 사계절 맛집", "제철", "storefront.jpg",
 "봄, 여름, 가을, 겨울. 언제 와도 좋은 속초 생선찜.",
 [("계절마다 속초",
   L("봄: 호숫가 꽃길 산책","여름: 해수욕과 바다 저녁","가을: 설악산 단풍","겨울: 해돋이와 겨울 바다")),
  ("언제 와도 생선찜", MENU_LINKS),
  ("더 보기", L(A("sokcho-spring-matjip","속초 봄 맛집"), A("sokcho-summer-matjip","속초 여름 맛집"), A("sokcho-autumn-matjip","속초 가을 맛집"), A("sokcho-winter-matjip","속초 겨울 맛집")))],
 [OFF, TOGO])

assert len(P) == 50, len(P)
