# 50 more keyword pages (added 2026-10-14). Same shape as pages2-5.
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
HOURS = ("몇 시에 여나요?",f"영업시간은 전화({TEL})로 확인해 주세요.")

# ---------- 메뉴 ----------
add("gaori-jjim-taste", "가오리찜 맛", "메뉴", "gaori-jjim.jpg",
 "쫄깃한 살, 오독오독한 연골, 매콤달콤한 양념. 가오리찜은 이런 맛이에요.",
 [("한 입에 세 가지 맛",
   "<p>가오리찜은 쫄깃한 살과 오독오독 씹히는 연골, 그리고 살 사이사이 스며든 매콤달콤한 양념이 한 번에 느껴지는 음식입니다. 홍어처럼 삭힌 냄새가 없어 처음 드시는 분도 편하게 드실 수 있습니다.</p>"),
  ("이런 분께 잘 맞아요",
   L("쫄깃한 식감을 좋아하는 분","밥반찬으로 매콤한 찜을 찾는 분","생선 가시 바르기가 번거로운 분")),
  ("더 보기", L(A("sokcho-gaori-jjim","속초 가오리찜 메뉴"), A("gaori-jjim-how-to-eat","가오리찜 맛있게 먹는 법"), A("gaori-vs-hongeo","가오리 홍어 차이")))],
 [("삭힌 냄새가 나나요?","아니요, 삭히지 않은 가오리라 냄새가 거의 없습니다."), SIZE])

add("gaori-yeongol", "가오리 연골 식감", "메뉴", "jjim-closeup.jpg",
 "가오리찜의 진짜 매력, 오독오독 씹히는 연골 이야기.",
 [("뼈 대신 연골",
   "<p>가오리는 단단한 뼈 대신 부드러운 연골로 이루어진 생선이라 살과 함께 연골까지 씹어 먹을 수 있습니다. 찜으로 익히면 연골이 적당히 부드러워져 오독오독한 식감이 살아납니다.</p>"),
  ("연골 맛있게 먹기",
   L("살과 연골을 한 번에 집어 양념에 굴려 드세요","날개 끝 쪽이 연골이 얇아 먹기 편해요","식감이 낯설면 살 위주로 드셔도 충분히 맛있어요")),
  ("더 보기", L(A("gaori-jjim-taste","가오리찜 맛"), A("sokcho-gaori-jjim","속초 가오리찜")))],
 [("아이도 먹을 수 있나요?","매콤한 양념이라 아이에게는 맵지 않은 메뉴를 함께 권해 드립니다."), SIZE])

add("modeum-jjim-guide", "생선모듬찜 고르는 이유", "메뉴", "jjim-table.jpg",
 "뭘 먹을지 못 정했다면 모듬찜. 여러 생선을 한 냄비에 맛보세요.",
 [("고민될 땐 모듬",
   "<p>생선모듬찜은 여러 생선을 한 냄비에 담아 쪄낸 메뉴라, 한 가지만 고르기 어려울 때 가장 무난한 선택입니다. 일행마다 좋아하는 생선이 달라도 함께 즐길 수 있습니다.</p>"),
  ("모듬찜이 좋은 자리",
   L("처음 오신 가족 여행","입맛이 다양한 단체 모임","여러 생선을 조금씩 맛보고 싶은 분")),
  ("더 보기", L(A("sokcho-saengseon-modeum-jjim","속초 생선모듬찜 메뉴"), A("daepohang-modeum-jjim","대포항 생선모듬찜")))],
 [("어떤 생선이 들어가나요?",f"그날 들어온 생선에 따라 달라집니다. 전화({TEL})로 물어보세요."), SIZE])

add("daegu-ppol-takeout", "대구뽈찜 포장", "메뉴", "jjim-closeup.jpg",
 "숙소에서 즐기는 대구뽈찜. 포장해서 가져가세요.",
 [("포장도 됩니다",
   f"<p>대포항생선찜본점은 전 메뉴 포장이 됩니다. {A('sokcho-daegu-ppol-jjim','대구뽈찜')}을 포장해 숙소에서 편하게 드셔 보세요. 미리 전화({TEL})로 주문하면 기다리는 시간을 줄일 수 있습니다.</p>"),
  ("숙소에서 맛있게",
   L("냄비나 팬에 옮겨 약불로 데우세요","양념이 졸면 물을 조금 넣어 주세요","볼살은 데운 뒤 바로 드시는 게 가장 쫀득해요")),
  ("더 보기", L(A("saengseon-jjim-reheat","생선찜 포장 데우는 법"), A("daegu-ppol-how-to-eat","대구뽈찜 먹는 법")))],
 [TOGO, SIZE])

add("kodari-jjim-takeout", "코다리찜 포장", "메뉴", "jjim-table.jpg",
 "쫄깃한 코다리찜, 포장해서 집이나 숙소에서.",
 [("식어도 쫄깃해요",
   f"<p>반건조 명태로 만든 {A('sokcho-kodari-jjim','코다리찜')}은 살이 쫄깃해 포장해 가도 식감이 잘 유지됩니다. 전 메뉴 포장되니 전화({TEL})로 미리 주문해 주세요.</p>"),
  ("포장 팁", L("미리 전화 주문하면 바로 받아 가실 수 있어요","데울 땐 약불에서 뚜껑을 덮고","밥만 준비하면 한 끼 완성")),
  ("더 보기", L(A("kodari-jjim-how-to-eat","코다리찜 먹는 법"), A("daepohang-takeout","대포항 포장")))],
 [TOGO, SIZE])

add("abai-sundae-takeout", "아바이순대 포장", "메뉴", "abai-sundae.jpg",
 "속초 왔다면 아바이순대 하나는 챙겨 가세요.",
 [("든든한 굵은 순대",
   f"<p>{A('sokcho-abai-sundae','속초아바이순대')}는 찹쌀과 선지로 속을 꽉 채운 굵은 순대입니다. 포장해 숙소 저녁이나 술안주로 드시기 좋습니다.</p>"),
  ("포장해 간다면", L("찜기나 전자레인지로 촉촉하게 데우세요","팬에 살짝 부치면 겉이 고소해져요","찜 포장과 함께 하면 한 상이 됩니다")),
  ("더 보기", L(A("abai-sundae-story","아바이순대 이야기"), A("ojingeo-sundae-takeout","오징어순대 포장")))],
 [TOGO, WHERE])

add("jjim-size-guide", "생선찜 사이즈 고르기", "메뉴", "jjim-table.jpg",
 "몇 명이면 무슨 사이즈? 생선찜 주문 전 확인하세요.",
 [("인원별 사이즈",
   L("소: 2인","중: 3인","대: 4인")),
  ("이렇게 고르면 좋아요",
   L("양이 많은 일행이면 한 사이즈 크게","곁들이 메뉴를 시킨다면 인원에 맞게","아이가 있다면 찜은 어른 인원 기준 + 맵지 않은 메뉴 추가")),
  ("곁들이 메뉴", L(A("sokcho-saengseon-gui","모듬생선구이"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대 (17,000원)"), A("sokcho-abai-sundae","아바이순대")))],
 [("5명 이상이면요?","대 사이즈에 다른 찜이나 곁들이를 더하시면 됩니다."),
  ("가격은?","메뉴판 가격은 매장이나 전화로 확인해 주세요.")])

add("saengseon-jjim-first-time", "생선찜 처음 먹어보기", "메뉴", "gaori-jjim.jpg",
 "생선찜이 처음이라면? 무엇을 어떻게 시키면 좋을지 알려 드려요.",
 [("처음이라면 이렇게",
   L("가시 걱정이 적은 "+A("sokcho-gaori-jjim","가오리찜")+"부터","여러 생선이 궁금하면 "+A("sokcho-saengseon-modeum-jjim","생선모듬찜"),"매운 게 걱정이면 "+A("sokcho-saengseon-gui","생선구이")+"를 함께")),
  ("먹는 순서",
   "<p>밥 위에 생선살과 양념 밴 무를 올리고 양념을 한 숟가락 끼얹어 드세요. 마지막엔 남은 양념에 밥을 비벼 마무리하면 됩니다.</p>"),
  ("더 보기", L(A("sokcho-saengseon-jjim","속초 생선찜이란"), A("saengseon-gasi-tip","생선 가시 바르는 법")))],
 [("많이 맵나요?","칼칼한 편이지만 단맛이 함께 있어 대부분 잘 드십니다."), SIZE])

add("sokcho-haejang", "속초 해장 식사", "메뉴", "jjim-closeup.jpg",
 "전날 한잔했다면, 칼칼한 생선찜으로 속을 달래 보세요.",
 [("칼칼한 게 당길 때",
   "<p>여행지에서 전날 한잔한 다음 날엔 칼칼하고 뜨끈한 음식이 생각납니다. 매콤한 양념에 무가 푹 익은 생선찜은 밥과 함께 든든한 한 끼가 됩니다.</p>"),
  ("추천", L(A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-kodari-jjim","코다리찜"), A("sokcho-saengseon-modeum-jjim","생선모듬찜"))),
  ("더 보기", L(A("sokcho-friends-trip","속초 친구여행 맛집"), A("daepohang-anju","대포항 술안주")))],
 [HOURS, OFF])

add("sokcho-jipbap", "속초 집밥 같은 식당", "메뉴", "jjim-table.jpg",
 "여행 중에도 밥이 먹고 싶을 때. 밥이 술술 넘어가는 생선찜 한 상.",
 [("여행 중 집밥 생각날 때",
   "<p>여행 중 군것질만 하다 보면 따뜻한 밥 한 공기가 생각납니다. 생선찜은 밥 위에 올려 먹는 반찬 같은 음식이라 집밥처럼 든든합니다.</p>"),
  ("밥과 잘 맞는 메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-bapjip","속초 밥집"), A("sokcho-bapdoduk","속초 밥도둑 메뉴"), A("sokcho-hansik","속초 한식 맛집")))],
 [WHERE, OFF])

# ---------- 대포항 ----------
add("daepohang-local-matjip", "대포항 현지인 맛집", "대포항", "storefront.jpg",
 "관광객만 가는 곳 말고, 동네 사람도 찾는 대포항 생선찜.",
 [("항구 앞 생선찜집",
   "<p>대포항생선찜본점은 대포항길에 있는 생선찜 전문점입니다. 찜, 구이, 순대처럼 속초 사람들이 평소에 먹는 음식을 냅니다.</p>"),
  ("자주 찾는 메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-local-food","속초 현지 음식"), A("daepohang-restaurant","대포항 식당 추천")))],
 [WHERE, OFF])

add("daepohang-breakfast", "대포항 아침 식사", "대포항", "jjim-closeup.jpg",
 "일출 보고 출출할 때, 대포항에서 든든한 아침 겸 점심.",
 [("해돋이 뒤 한 끼",
   f"<p>대포항 일출을 보고 나면 따뜻한 밥 한 끼가 생각납니다. 여는 시간은 날에 따라 다를 수 있으니 전화({TEL})로 먼저 확인해 주세요.</p>"),
  ("아침에 좋은 메뉴", L(A("sokcho-saengseon-gui","생선구이")+": 맵지 않고 담백하게", A("sokcho-kodari-jjim","코다리찜")+": 든든하게")),
  ("더 보기", L(A("daepohang-sunrise","대포항 일출"), A("sokcho-sunrise","속초 해돋이")))],
 [HOURS, OFF])

add("daepohang-honbap", "대포항 혼밥", "대포항", "gui.jpg",
 "혼자 대포항 여행, 혼자서도 편하게 먹을 수 있는 메뉴.",
 [("혼자라도 괜찮아요",
   f"<p>찜 메뉴는 2인 소 사이즈부터라 혼자라면 양이 넉넉합니다. 혼자 오셨다면 {A('sokcho-saengseon-gui','생선구이')}나 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 드시거나, 찜을 남겨 포장해 가셔도 좋습니다.</p>"),
  ("혼밥 팁", L("붐비는 식사 시간을 피하면 더 여유로워요","남은 음식은 포장 가능","전화로 미리 물어보면 편해요")),
  ("더 보기", L(A("sokcho-honbap","속초 혼밥"), A("sokcho-solo-trip","속초 혼자 여행")))],
 [TOGO, OFF])

add("daepohang-parents", "대포항 부모님 식사", "대포항", "hall.jpg",
 "부모님 모시고 대포항, 편하게 앉아 드실 수 있는 생선찜.",
 [("부모님이 좋아하시는 메뉴",
   L(A("sokcho-saengseon-modeum-jjim","생선모듬찜")+": 여러 생선을 한 번에", A("sokcho-saengseon-gui","생선구이")+": 맵지 않고 담백하게", A("sokcho-abai-sundae","아바이순대")+": 속초 옛 맛")),
  ("식사 뒤 산책", f"<p>식사 후엔 {A('daepohang-walk','대포항 산책')}으로 천천히 항구를 둘러보세요.</p>"),
  ("더 보기", L(A("sokcho-parents-matjip","속초 부모님 모시고 갈 맛집"), A("sokcho-parents-day","어버이날 속초 식사")))],
 [PARK, OFF])

add("daepohang-friends", "대포항 친구랑", "대포항", "jjim-table.jpg",
 "친구들과 대포항, 큰 냄비 생선찜 하나 가운데 놓고.",
 [("친구랑 오면 이렇게",
   L("인원에 맞춰 찜 사이즈 고르기","누룽지 오징어순대 하나 추가","식사 뒤 튀김골목 구경")),
  ("함께 먹기 좋은 메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-friends-trip","속초 친구여행 맛집"), A("daepohang-twigim","대포항 튀김 먹고 식사")))],
 [SIZE, OFF])

add("daepohang-hoesik", "대포항 회식", "대포항", "hall3.jpg",
 "대포항에서 회식한다면, 회 말고 생선찜 한 상은 어떠세요?",
 [("여럿이 나눠 먹기 좋아요",
   "<p>큰 냄비 찜을 가운데 두고 나눠 먹는 생선찜은 회식 자리에 잘 어울립니다. 인원이 많다면 미리 전화로 자리를 문의해 주세요.</p>"),
  ("회식 메뉴 구성", L("찜 2~3가지를 섞어 주문", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+"는 안주로", A("sokcho-saengseon-gui","생선구이")+"는 맵지 않은 메뉴로")),
  ("더 보기", L(A("sokcho-hoesik","속초 회식 장소"), A("daepohang-group-dining","대포항 단체 식사")))],
 [("단체 예약 되나요?",f"전화({TEL})로 문의해 주세요."), PARK])

add("daepohang-nearby-restaurant", "대포항 근처 식당", "대포항", "storefront.jpg",
 "대포항 근처에서 밥 먹을 곳 찾는다면, 대포항길 생선찜집.",
 [("어디에 있나요?",
   f"<p>대포항생선찜본점은 강원특별자치도 속초시 {A('daepohang-directions','대포항길 10')}에 있습니다. 항구 구경하다 걸어서 오기 좋습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("daepohang-matjip","대포항 맛집"), A("daepodong-matjip","대포동 맛집")))],
 [PARK, OFF])

add("daepohang-sundae", "대포항 순대", "대포항", "squid-sundae.jpg",
 "대포항에서 맛보는 속초 순대 두 가지, 오징어순대와 아바이순대.",
 [("두 가지 순대",
   L(A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 겉은 바삭, 속은 촉촉 (17,000원)", A("sokcho-abai-sundae","속초아바이순대")+": 찹쌀과 선지로 속을 채운 굵은 순대")),
  ("찜과 함께", "<p>매콤한 찜 사이사이 맵지 않은 순대를 곁들이면 입맛이 계속 살아납니다.</p>"),
  ("더 보기", L(A("ojingeo-vs-abai-sundae","오징어순대 아바이순대 차이"), A("daepohang-ojingeo-sundae","대포항 오징어순대")))],
 [("순대는 맵나요?","아니요, 맵지 않습니다."), TOGO])

add("daepohang-winter", "겨울 대포항", "대포항", "jjim-closeup.jpg",
 "찬바람 부는 겨울 대포항, 뜨끈한 생선찜으로 몸 녹이기.",
 [("겨울 대포항",
   "<p>겨울 대포항은 바닷바람이 차갑지만 맑은 하늘과 겨울 바다가 아름답습니다. 항구를 한 바퀴 돌고 나면 뜨끈한 찜이 반갑습니다.</p>"),
  ("겨울에 좋은 메뉴", L(A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-kodari-jjim","코다리찜"), A("sokcho-gaori-jjim","가오리찜"))),
  ("더 보기", L(A("sokcho-winter-matjip","속초 겨울 맛집"), A("sokcho-winter-sea","속초 겨울바다 여행")))],
 [OFF, TOGO])

add("daepohang-autumn", "가을 대포항", "대포항", "gaori-jjim.jpg",
 "단풍 여행길에 들르는 가을 대포항, 생선찜 한 상.",
 [("가을 여행 코스",
   L("설악산 단풍 구경","대포항으로 내려와 늦은 점심","항구 산책과 튀김 간식")),
  ("가을 한 상", MENU_LINKS),
  ("더 보기", L(A("seorak-danpung-matjip","설악산 단풍 맛집"), A("sokcho-autumn-matjip","속초 가을 맛집")))],
 [PARK, OFF])

# ---------- 근처 ----------
add("yeongnangdong-matjip", "속초 영랑동 맛집", "근처", "storefront.jpg",
 "영랑동에서 차로 대포항까지, 생선찜 먹으러 가요.",
 [("영랑동에서 출발",
   "<p>영랑동은 속초 북쪽 바닷가 동네입니다. 대포항은 속초 남쪽에 있어 시내를 지나 바닷가 길로 내려오면 됩니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("yeongnangho-matjip","영랑호 근처 맛집"), A("yeonggeumjeong-matjip","영금정 근처 맛집")))],
 [WHERE, PARK])

add("geumhodong-matjip", "속초 금호동 맛집", "근처", "jjim-table.jpg",
 "금호동에서 생선찜 생각나면, 대포항까지 한 번에.",
 [("시내에서 대포항으로",
   "<p>금호동은 속초 시내 중심 동네입니다. 시내에서 남쪽 대포항 쪽으로 내려오면 대포항길에 가게가 있습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("jungangdong-matjip","속초 중앙동 맛집"), A("gyodong-matjip","속초 교동 맛집")))],
 [WHERE, OFF])

add("domundong-matjip", "속초 도문동 맛집", "근처", "hall2.jpg",
 "설악산 가는 길 도문동, 바다 쪽으로 내려와 생선찜.",
 [("산과 바다 사이",
   "<p>도문동은 설악산 쪽으로 가는 길목에 있는 동네입니다. 산 구경을 마치고 바다 쪽 대포항으로 내려와 식사하기 좋습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("seoraksan-matjip","설악산 근처 맛집"), A("seorak-cablecar-matjip","설악 케이블카 맛집")))],
 [WHERE, PARK])

add("seorakdong-matjip", "설악동 맛집", "근처", "jjim-closeup.jpg",
 "설악동에서 산행 마치고, 대포항 생선찜으로 마무리.",
 [("산행 뒤 든든하게",
   "<p>설악동은 설악산 소공원 쪽 동네로 산행을 시작하고 마치는 곳입니다. 땀 흘린 뒤엔 뜨끈하고 매콤한 찜이 잘 어울립니다.</p>"),
  ("산행 후 추천", L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-abai-sundae","아바이순대"))),
  ("더 보기", L(A("ulsanbawi-matjip","울산바위 등산 후 맛집"), A("biseondae-matjip","비선대 맛집")))],
 [PARK, OFF])

add("gwongeumseong-matjip", "권금성 맛집", "근처", "gaori-jjim.jpg",
 "케이블카 타고 권금성 다녀온 뒤, 바다 쪽 생선찜.",
 [("권금성 다녀와서",
   "<p>권금성은 설악산 케이블카를 타고 오르는 봉우리입니다. 내려와서 바다 쪽 대포항으로 이동하면 산과 바다를 하루에 즐길 수 있습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("seorak-cablecar-matjip","설악 케이블카 맛집"), A("sinheungsa-matjip","신흥사 맛집")))],
 [PARK, OFF])

add("solbeach-yangyang-matjip", "쏠비치 양양 근처 맛집", "근처", "jjim-table.jpg",
 "양양 쏠비치에 묵는다면, 속초 대포항까지 생선찜 먹으러.",
 [("양양에서 속초로",
   "<p>양양에서 바닷가 길을 따라 북쪽으로 올라오면 속초 대포항에 닿습니다. 숙소에서 쉬다가 저녁 먹으러 나오기 좋습니다.</p>"),
  ("숙소로 포장도", f"<p>전 메뉴 포장되니 숙소에서 드셔도 좋습니다. {A('sokcho-stay-in-dinner','숙소에서 먹는 저녁')}도 참고하세요.</p>"),
  ("더 보기", L(A("yangyang-surf-matjip","양양 서핑 후 맛집"), A("mulchihang-matjip","물치항 근처 맛집")))],
 [TOGO, PARK])

add("delpino-matjip", "델피노 근처 맛집", "근처", "hall3.jpg",
 "고성 델피노에 묵는다면, 속초 대포항 생선찜 한 끼.",
 [("고성에서 속초로",
   "<p>고성 쪽 리조트에 묵으면서 속초로 나와 식사하는 분이 많습니다. 대포항은 속초 남쪽에 있어 시내를 지나 내려오면 됩니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("goseong-trip-matjip","고성 여행 속초 맛집"), A("sokcho-family-dining","속초 가족 외식")))],
 [WHERE, TOGO])

add("kensington-seorak-matjip", "켄싱턴 설악 근처 맛집", "근처", "hall.jpg",
 "설악동 켄싱턴에 묵는다면, 바다 쪽 대포항에서 생선찜.",
 [("숙소에서 바다로",
   "<p>설악동 숙소에서 산 구경을 마친 뒤 바다 쪽으로 나오면 대포항에 닿습니다. 저녁 겸 항구 산책 코스로 좋습니다.</p>"),
  ("추천", MENU_LINKS),
  ("더 보기", L(A("seorakdong-matjip","설악동 맛집"), A("daepohang-dinner","대포항 저녁")))],
 [PARK, OFF])

add("hajodae-matjip", "하조대 여행 맛집", "근처", "storefront.jpg",
 "양양 하조대 구경하고 속초로 올라와 생선찜 한 상.",
 [("양양에서 속초까지",
   "<p>하조대는 양양의 바닷가 명소입니다. 바닷가 길을 따라 북쪽으로 올라오면 속초 대포항에 닿아 하루 코스로 묶기 좋습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-yangyang-course","속초 양양 여행 코스"), A("naksansa-matjip","낙산사 가는 길 맛집")))],
 [WHERE, PARK])

add("hwajinpo-matjip", "화진포 여행 맛집", "근처", "jjim-closeup.jpg",
 "고성 화진포 다녀오는 길, 속초 대포항에서 저녁.",
 [("고성 여행 마무리",
   "<p>화진포는 고성의 호수와 바다가 함께 있는 명소입니다. 고성 여행을 마치고 남쪽으로 내려오는 길에 속초에서 식사하기 좋습니다.</p>"),
  ("저녁 추천", MENU_LINKS),
  ("더 보기", L(A("goseong-trip-matjip","고성 여행 속초 맛집"), A("sokcho-drive","속초 드라이브 코스")))],
 [PARK, OFF])

# ---------- 상황 ----------
add("sokcho-couple-trip", "속초 커플 여행 맛집", "상황", "gaori-jjim.jpg",
 "둘이 떠난 속초, 생선찜 소 사이즈로 딱 좋은 한 끼.",
 [("둘이라면",
   f"<p>찜은 소 사이즈가 2인이라 둘이 드시기 딱 좋습니다. {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')} 하나를 곁들이면 더 풍성해집니다.</p>"),
  ("커플 코스", L("바닷가 카페","대포항 생선찜","항구 야경 산책")),
  ("더 보기", L(A("sokcho-date-matjip","속초 데이트 맛집"), A("daepohang-date","대포항 데이트")))],
 [SIZE, OFF])

add("sokcho-solo-trip", "속초 혼자 여행", "상황", "gui.jpg",
 "혼자 떠나는 속초, 걷고 보고 먹는 하루.",
 [("혼자 여행 코스",
   L("바다향기로나 호숫길 걷기","대포항 구경","혼자서도 편한 "+A("sokcho-saengseon-gui","생선구이")+" 한 끼")),
  ("혼자라면", "<p>찜은 2인 소 사이즈부터라 남으면 포장해 가셔도 됩니다.</p>"),
  ("더 보기", L(A("sokcho-honbap","속초 혼밥"), A("daepohang-honbap","대포항 혼밥"), A("sokcho-ttubeogi","속초 뚜벅이 여행")))],
 [TOGO, OFF])

add("sokcho-girls-trip", "속초 여자끼리 여행 맛집", "상황", "jjim-table.jpg",
 "친구들끼리 속초, 사진도 찍고 생선찜도 나눠 먹고.",
 [("여럿이 나눠 먹기",
   "<p>인원에 맞춰 찜 사이즈를 고르고 곁들이 메뉴를 하나 더하면 다 같이 다양하게 맛볼 수 있습니다.</p>"),
  ("추천 조합", L(A("sokcho-gaori-jjim","가오리찜")+" + "+A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"), A("sokcho-saengseon-modeum-jjim","생선모듬찜")+" + "+A("sokcho-saengseon-gui","생선구이"))),
  ("더 보기", L(A("sokcho-photo-spots","속초 사진 명소"), A("sokcho-cafe-tour","속초 카페 투어 후 식사")))],
 [SIZE, OFF])

add("sokcho-family-gathering", "속초 가족 모임 식당", "상황", "hall3.jpg",
 "온 가족이 모이는 날, 큰 상에 생선찜 둘러앉아.",
 [("가족 모임에 좋아요",
   L("어른용 매콤한 찜","아이용 맵지 않은 구이와 순대","아기의자 있어요")),
  ("인원이 많다면", f"<p>미리 전화({TEL})로 인원을 알려 주시면 편합니다.</p>"),
  ("더 보기", L(A("sokcho-three-generations","3대 가족 속초 식사"), A("sokcho-family-dining","속초 가족 외식")))],
 [("아기의자 있나요?","네, 있습니다."), PARK])

add("sokcho-company-outing", "속초 회사 야유회 식사", "상황", "hall2.jpg",
 "회사 야유회로 속초, 다 같이 먹을 생선찜 한 상.",
 [("단체 식사로 좋아요",
   "<p>여러 냄비의 찜을 나눠 먹는 식사는 단체 자리에 잘 어울립니다. 맵지 않은 메뉴도 있어 입맛이 다른 분들도 함께 드실 수 있습니다.</p>"),
  ("준비 팁", L("인원과 도착 시간을 미리 전화로 알려 주세요","찜 여러 가지 + 곁들이로 구성","주차는 공영주차장 이용")),
  ("더 보기", L(A("sokcho-workshop-restaurant","속초 워크숍 식당"), A("sokcho-group-restaurant","속초 단체 식당")))],
 [("단체 예약 되나요?",f"전화({TEL})로 문의해 주세요."), PARK])

add("sokcho-retreat-meal", "속초 수련회 식사", "상황", "hall.jpg",
 "수련회나 단체 여행 중 한 끼, 속초 생선찜으로.",
 [("단체가 함께 먹기",
   "<p>여럿이 둘러앉아 큰 냄비를 나눠 먹는 생선찜은 단체 식사에 잘 맞습니다. 맵지 않은 구이와 순대도 있어 함께 주문하기 좋습니다.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-senior-group","어르신 단체 속초 식사"), A("sokcho-club-trip","동호회 속초 여행 식당")))],
 [("단체 예약 되나요?",f"전화({TEL})로 문의해 주세요."), OFF])

add("sokcho-military-visit", "속초 면회 외식", "상황", "jjim-table.jpg",
 "면회 와서 함께하는 한 끼, 든든한 생선찜.",
 [("오랜만에 든든하게",
   "<p>면회 날 함께 먹는 한 끼는 든든하고 푸짐한 메뉴가 좋습니다. 큰 냄비 찜에 밥 한 공기면 배부르게 드실 수 있습니다.</p>"),
  ("추천", L(A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-gaori-jjim","가오리찜"), A("sokcho-abai-sundae","아바이순대"))),
  ("남으면 포장", "<p>남은 음식은 포장해 가실 수 있습니다.</p>")],
 [TOGO, OFF])

add("sokcho-chabak", "속초 차박 음식", "상황", "gui.jpg",
 "차박 캠핑 중 저녁, 포장한 생선찜과 구이로.",
 [("차박 저녁은 포장으로",
   f"<p>전 메뉴 포장되니 차박지에서 드실 저녁으로 챙겨 가세요. 미리 전화({TEL})로 주문하면 바로 받아 가실 수 있습니다.</p>"),
  ("차박에 좋은 메뉴", L(A("sokcho-saengseon-gui","생선구이")+": 국물이 없어 들고 다니기 편해요", A("sokcho-abai-sundae","아바이순대")+": 안주로 좋아요", A("sokcho-gaori-jjim","가오리찜")+": 버너에 데워 드세요")),
  ("더 보기", L(A("sokcho-camping-takeout","속초 캠핑 포장 음식"), A("sokcho-takeout-matjip","속초 포장 맛집")))],
 [TOGO, OFF])

add("sokcho-christmas", "속초 크리스마스 식사", "상황", "jjim-closeup.jpg",
 "크리스마스 속초 여행, 겨울 바다 보고 뜨끈한 생선찜.",
 [("겨울 바다와 함께",
   "<p>크리스마스 무렵 속초는 겨울 바다를 보러 오는 여행객이 많습니다. 차가운 바닷바람 뒤엔 뜨끈한 찜이 잘 어울립니다.</p>"),
  ("추천", L(A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-gaori-jjim","가오리찜"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"))),
  ("더 보기", L(A("sokcho-year-end","속초 연말 여행"), A("sokcho-december-matjip","12월 속초 맛집")))],
 [("크리스마스에도 여나요?",f"휴일 영업은 전화({TEL})로 확인해 주세요."), OFF])

add("sokcho-childrens-day", "어린이날 속초 식사", "상황", "hall.jpg",
 "어린이날 속초 가족여행, 아이와 함께 먹기 좋은 메뉴.",
 [("아이와 함께라면",
   L(A("sokcho-saengseon-gui","생선구이")+": 맵지 않아요", A("sokcho-nurungji-squid-sundae","누룽지 오징어순대")+": 바삭해서 아이들이 좋아해요","아기의자 있어요")),
  ("어른 메뉴", f"<p>어른들은 {A('sokcho-gaori-jjim','가오리찜')}이나 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}을 함께 드세요.</p>"),
  ("더 보기", L(A("sokcho-kids-matjip","속초 아이랑 맛집"), A("daepohang-with-kids","대포항 아이랑")))],
 [("아기의자 있나요?","네, 있습니다."), ("휴일에도 여나요?",f"전화({TEL})로 확인해 주세요.")])

# ---------- 여행 ----------
add("daejeon-to-sokcho", "대전에서 속초 여행", "여행", "storefront.jpg",
 "대전에서 속초까지, 긴 길 끝에 기다리는 생선찜 한 상.",
 [("멀리서 오는 여행",
   "<p>대전에서 속초는 꽤 먼 길이라 1박 이상 머무는 분이 많습니다. 도착한 날 저녁이나 떠나기 전 점심으로 생선찜을 드셔 보세요.</p>"),
  ("꼭 먹을 것", MENU_LINKS),
  ("더 보기", L(A("sokcho-1bak2il","속초 1박2일 코스"), A("sokcho-2bak3il","속초 2박3일 코스")))],
 [WHERE, OFF])

add("daegu-to-sokcho", "대구에서 속초 여행", "여행", "jjim-table.jpg",
 "대구에서 속초로 떠나는 여행, 동해 바다와 생선찜.",
 [("동해 바다 보러",
   "<p>대구에서 속초로 오는 분들은 동해안을 따라 올라오며 여러 바닷가를 들르기도 합니다. 속초에 도착하면 대포항에서 생선찜으로 한 끼 하세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("busan-to-sokcho","부산에서 속초 여행"), A("sokcho-drive","속초 드라이브 코스")))],
 [WHERE, PARK])

add("gyeonggi-to-sokcho", "경기도에서 속초 여행", "여행", "gaori-jjim.jpg",
 "경기도에서 주말 속초, 당일치기도 1박도 좋아요.",
 [("주말에 훌쩍",
   "<p>경기도에서는 속초까지 주말 여행으로 많이 옵니다. 당일치기라면 점심을, 1박이라면 저녁을 대포항에서 드셔 보세요.</p>"),
  ("메뉴", MENU_LINKS),
  ("더 보기", L(A("seoul-to-sokcho","서울에서 속초"), A("sokcho-day-trip","속초 당일치기")))],
 [PARK, OFF])

add("chuncheon-to-sokcho", "춘천에서 속초 여행", "여행", "jjim-closeup.jpg",
 "춘천 닭갈비 다음은 속초 생선찜. 강원도 먹방 여행.",
 [("강원도 한 바퀴",
   "<p>춘천과 속초를 묶어 강원도를 여행하는 분이 많습니다. 내륙에서 바다로 넘어오면 생선 요리로 분위기를 바꿔 보세요.</p>"),
  ("속초에선 이것", MENU_LINKS),
  ("더 보기", L(A("gangneung-sokcho-trip","강릉 속초 여행"), A("sokcho-food-course","속초 먹방 코스")))],
 [WHERE, OFF])

add("sokcho-rentcar", "속초 렌터카 여행", "여행", "storefront.jpg",
 "렌터카로 속초 한 바퀴, 대포항 주차하고 생선찜.",
 [("차가 있으면 편해요",
   "<p>렌터카가 있으면 설악산, 호수, 항구를 하루에 돌아볼 수 있습니다. 대포항에 오시면 공영주차장에 세우고 걸어서 오시면 됩니다.</p>"),
  ("코스 예시", L("설악산 구경","영랑호·청초호 드라이브","대포항에서 식사와 산책")),
  ("더 보기", L(A("daepohang-parking","대포항 주차"), A("sokcho-drive","속초 드라이브 코스")))],
 [PARK, OFF])

add("sokcho-half-day", "속초 반나절 코스", "여행", "gaori-jjim.jpg",
 "시간이 반나절뿐이라면, 대포항 하나로 알차게.",
 [("반나절 코스",
   L("대포항 도착 후 항구 구경","생선찜으로 식사","튀김골목에서 간식","바닷가 산책")),
  ("빠르게 먹고 싶다면", f"<p>미리 전화({TEL})로 메뉴를 물어보고 오시면 시간을 아낄 수 있습니다.</p>"),
  ("더 보기", L(A("daepohang-course","대포항 구경 코스"), A("sokcho-day-trip","속초 당일치기")))],
 [PARK, OFF])

add("sokcho-off-season", "속초 비수기 여행", "여행", "hall2.jpg",
 "붐비지 않을 때 가는 속초, 한적한 바다와 여유로운 식사.",
 [("비수기의 좋은 점",
   L("숙소와 길이 한결 여유로워요","식당도 덜 붐벼 천천히 식사할 수 있어요","바다를 조용히 즐길 수 있어요")),
  ("한적할 때 한 끼", MENU_LINKS),
  ("더 보기", L(A("sokcho-weekday-trip","속초 평일 여행"), A("sokcho-budget-trip","속초 알뜰 여행")))],
 [OFF, PARK])

# ---------- 제철 ----------
add("sokcho-april-matjip", "4월 속초 맛집", "제철", "gaori-jjim.jpg",
 "벚꽃 피는 4월 속초, 호숫길 산책하고 생선찜.",
 [("4월의 속초",
   "<p>4월이면 호숫가를 따라 봄꽃이 피어 산책하기 좋습니다. 산책 뒤엔 든든한 생선찜으로 식사하세요.</p>"),
  ("봄 한 상", MENU_LINKS),
  ("더 보기", L(A("yeongnangho-matjip","영랑호 근처 맛집"), A("sokcho-spring-matjip","속초 봄 맛집")))],
 [OFF, TOGO])

add("sokcho-may-matjip", "5월 속초 맛집", "제철", "hall.jpg",
 "가정의 달 5월, 가족과 함께 속초에서 생선찜.",
 [("가족 여행의 달",
   "<p>5월은 어린이날과 어버이날이 있어 가족 여행이 많은 달입니다. 아이와 어른 모두 드실 메뉴가 있습니다.</p>"),
  ("가족 메뉴", L(A("sokcho-saengseon-modeum-jjim","생선모듬찜"), A("sokcho-saengseon-gui","생선구이"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"))),
  ("더 보기", L(A("sokcho-childrens-day","어린이날 속초 식사"), A("sokcho-parents-day","어버이날 속초 식사")))],
 [("아기의자 있나요?","네, 있습니다."), OFF])

add("sokcho-june-matjip", "6월 속초 맛집", "제철", "storefront.jpg",
 "초여름 6월 속초, 성수기 전 여유로운 바다 여행.",
 [("6월의 속초",
   "<p>6월은 본격적인 여름 성수기 전이라 비교적 여유롭게 바다를 즐길 수 있습니다. 해가 길어 저녁 산책하기도 좋습니다.</p>"),
  ("초여름 한 끼", MENU_LINKS),
  ("더 보기", L(A("sokcho-summer-matjip","속초 여름 맛집"), A("sokcho-beach-matjip","속초해수욕장 근처 맛집")))],
 [OFF, PARK])

assert len(P) == 50, len(P)
