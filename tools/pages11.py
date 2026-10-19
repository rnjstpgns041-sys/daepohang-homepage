# 21 keyword pages (added 2026-10-19) replacing the 21 the owner removed from pages10.
# Aimed at people deciding where to eat in or near Sokcho (visit intent): nearby hotels in 대포동,
# neighbouring towns + dish, "what to eat" moments of a trip.
# Hotel addresses checked on their own sites: 마레몬스 동해대로 3705 (대포동), 카시아 속초 대포항희망길 120 (대포동).
# Area facts kept general (no distances, minutes or exit names). Opening hours are unconfirmed.
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
SHOP = f"<p>대포항생선찜본점은 속초시 대포항길 10, 대포항 안쪽 상가 1층에 있습니다. 노란색과 분홍색 네온 간판을 찾으세요. 매주 수요일은 쉬고, 전 메뉴 포장됩니다. 전화 {TEL}.</p>"

# ---------- 대포동 숙소 근처 ----------
def stay_near(slug, kw, name, about, more):
    add(slug, kw, "근처", "storefront.jpg",
     f"{name}에 묵는다면, 저녁은 대포항에서 생선찜으로.",
     [(f"{name} 근처에서 먹기", f"<p>{about}</p>"),
      ("대포항생선찜본점", f"<p>대포항 안쪽 상가에 있는 생선찜, 생선구이 전문점입니다. 대표 메뉴는 {A('sokcho-gaori-jjim','가오리찜')}이고, 맵지 않은 {A('sokcho-saengseon-gui','모듬생선구이')}와 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}도 있습니다.</p>"),
      ("방에서 먹고 싶다면", "<p>전 메뉴 포장됩니다. 미리 전화로 주문해 두면 기다리지 않고 받아 가실 수 있습니다.</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [TOGO, OFF])

stay_near("cassia-sokcho-matjip", "카시아 속초 근처 맛집", "카시아 속초",
 "카시아 속초는 대포동, 대포항 바로 뒤편에 있는 숙소입니다. 체크인하고 짐을 풀었다면 대포항까지 걸어 나와 항구 구경과 저녁을 함께 해결하기 좋습니다.",
 L(A("daepohang-lodging-dinner","대포항 숙소 근처 식당"), A("daepohang-night","대포항 야경"), A("sokcho-stay-in-dinner","숙소에서 먹는 저녁")))

stay_near("maremons-matjip", "마레몬스 근처 맛집", "호텔 마레몬스",
 "호텔 마레몬스는 대포동에 있는 호텔로, 대포항과 같은 동네입니다. 차를 다시 꺼내지 않고 가까운 대포항에서 저녁을 드시기 좋습니다.",
 L(A("daepohang-lodging-dinner","대포항 숙소 근처 식당"), A("daepohang-dinner","대포항 저녁"), A("oeongchi-matjip","외옹치 맛집")))

add("sokcho-hotel-matjip", "속초 호텔 근처 맛집", "근처", "storefront.jpg",
 "속초 호텔에 묵을 때, 저녁 먹으러 나가기 좋은 곳.",
 [("호텔 위치별로", L("대포동, 외옹치 쪽 호텔: 대포항이 가장 가깝습니다.", "속초해수욕장 쪽 호텔: 시내 식당이 많고, 차로 대포항까지 내려오기도 쉽습니다.", "설악산 쪽 리조트: 산에서 내려오는 길에 대포항으로 오시면 됩니다.")),
  ("대포항에서 한 끼", f"<p>대포항생선찜본점은 생선찜, 생선구이, 순대를 한 곳에서 드실 수 있습니다. 호텔 방에서 드시려면 포장도 됩니다.</p>"),
  ("추천 메뉴", MENU_LINKS),
  ("더 보기", L(A("cassia-sokcho-matjip","카시아 속초 근처 맛집"), A("maremons-matjip","마레몬스 근처 맛집"), A("sokcho-lotte-resort-matjip","속초 롯데리조트 근처 맛집")))],
 [TOGO, PARK])

add("sokcho-pension-matjip", "속초 펜션 근처 맛집", "근처", "storefront.jpg",
 "펜션에서 먹을 저녁, 사 가거나 먹고 들어가거나.",
 [("펜션 저녁 고민", "<p>펜션에서는 바비큐를 많이 하지만, 하루쯤은 차려진 밥을 먹고 싶을 때가 있습니다. 대포동, 도문동 쪽 펜션이라면 대포항이 가깝습니다.</p>"),
  ("포장해서 펜션으로", f"<p>대포항생선찜본점은 전 메뉴 포장됩니다. 찜은 냄비째 데워 드시면 되고, {A('saengseon-jjim-reheat','데우는 법')}도 정리해 두었습니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-stay-in-dinner","숙소에서 먹는 저녁"), A("sokcho-camping-takeout","속초 캠핑 포장 음식"), A("daepohang-takeout","대포항 포장")))],
 [TOGO, PET])

# ---------- 길 위에서 ----------
add("sokcho-ic-matjip", "속초IC 근처 맛집", "근처", "storefront.jpg",
 "속초IC로 들어오거나 나가기 전, 생선찜 한 끼.",
 [("속초IC로 오가는 분께", "<p>서울양양고속도로를 타고 속초로 들어오면 속초IC로 빠지는 분이 많습니다. 속초에 도착한 첫 끼나 돌아가기 전 마지막 끼니를 대포항에서 드셔 보세요.</p>"),
  ("대포항까지", f"<p>내비게이션에 ‘대포항’ 또는 ‘대포항길 10’을 찍으세요. 주차는 {A('daepohang-parking','대포항 공영주차장')}을 이용하시면 됩니다.</p>"),
  ("추천 메뉴", MENU_LINKS),
  ("더 보기", L(A("sokcho-first-meal","속초 도착 첫 끼"), A("sokcho-last-meal","속초 마지막 식사"), A("daepohang-directions","대포항 가는 법")))],
 [PARK, TOGO])

add("seoul-yangyang-expressway-matjip", "서울양양고속도로 맛집", "근처", "storefront.jpg",
 "서울양양고속도로 끝, 바다 앞에서 먹는 첫 끼.",
 [("고속도로 끝에서", "<p>서울양양고속도로를 달려 동해안에 닿으면 양양과 속초가 바로입니다. 휴게소에서 간단히 먹고 왔다면, 도착해서 제대로 된 한 끼를 드셔 보세요.</p>"),
  ("대포항이 편한 이유", "<p>대포항은 속초 남쪽 끝이라 양양 쪽에서 올라올 때 가장 먼저 닿는 항구입니다. 항구 구경과 식사를 한 번에 할 수 있습니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("seoul-to-sokcho","서울에서 속초"), A("sokcho-ic-matjip","속초IC 근처 맛집"), A("yangyang-matjip","양양 맛집")))],
 [PARK, WHERE])

add("sokcho-first-meal", "속초 도착 첫 끼", "상황별", "jjim-table.jpg",
 "속초에 도착하자마자 먹을 첫 끼, 바다 음식으로.",
 [("첫 끼로 좋은 이유", "<p>먼 길을 달려와 배가 고플 때는 기다림 없이 든든하게 먹을 수 있는 메뉴가 좋습니다. 생선찜은 밥과 함께 나와 한 끼로 충분합니다.</p>"),
  ("무엇을 시킬까", f"<p>둘이라면 찜 소(2인)에 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}, 가족이라면 찜 중·대에 {A('sokcho-saengseon-gui','모듬생선구이')}를 더하면 알맞습니다.</p>"),
  ("미리 전화하면", f"<p>도착 시간에 맞춰 자리나 포장을 전화({TEL})로 물어보세요.</p>"),
  ("더 보기", L(A("sokcho-last-meal","속초 마지막 식사"), A("sokcho-1bak2il-matjip","속초 1박2일 맛집"), A("sokcho-what-to-eat","속초 뭐 먹지")))],
 [SIZE, PARK])

add("sokcho-last-meal", "속초 마지막 식사", "상황별", "jjim-closeup.jpg",
 "집에 가기 전 속초에서 마지막 한 끼, 그리고 포장.",
 [("돌아가기 전 한 끼", "<p>여행 마지막 날에는 체크아웃 후 짐을 싣고 한 끼를 먹고 출발하는 분이 많습니다. 긴 운전 전에는 든든한 밥이 좋습니다.</p>"),
  ("집에 가져가기", f"<p>여행에서 먹은 맛을 집에서도 드시고 싶다면 포장하세요. {A('saengseon-jjim-reheat','생선찜 데우는 법')}과 {A('squid-sundae-reheat','오징어순대 데우는 법')}도 정리해 두었습니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-first-meal","속초 도착 첫 끼"), A("gaori-jjim-takeout","가오리찜 포장"), A("ojingeo-sundae-takeout","오징어순대 포장")))],
 [TOGO, OFF])

add("sokcho-what-to-eat", "속초 뭐 먹지", "상황별", "jjim-table.jpg",
 "속초에서 뭐 먹을지 고민될 때, 상황별로 골라 드려요.",
 [("상황별 추천", L(f"든든한 밥이 필요할 때: {A('sokcho-gaori-jjim','가오리찜')}", f"아이와 함께일 때: {A('sokcho-saengseon-gui','모듬생선구이')}", f"속초다운 별미가 먹고 싶을 때: {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}", f"여럿이 나눠 먹을 때: {A('sokcho-saengseon-modeum-jjim','생선모듬찜')} 대(4인)")),
  ("회가 망설여진다면", f"<p>회를 못 드시는 분이 있거나 따뜻한 음식이 당길 때는 익힌 생선 요리가 좋습니다. {A('daepohang-not-hoe','대포항 회 말고 먹을거')}도 참고하세요.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-must-eat","속초 꼭 먹어야 할 음식"), A("sokcho-matjip-best","속초 맛집 베스트"), A("sokcho-food","속초 먹거리")))],
 [KIDS, SIZE])

add("sokcho-trip-matjip", "속초 여행 맛집", "여행", "jjim-table.jpg",
 "속초 여행 중 한 끼, 대포항 생선찜으로 채우세요.",
 [("여행 중 들르기 좋은 곳", "<p>대포항은 속초 남쪽 끝 항구로, 양양이나 설악산 쪽에서 오가기 편합니다. 항구 산책, 튀김골목 구경과 함께 식사까지 한 번에 할 수 있습니다.</p>"),
  ("추천 메뉴", MENU_LINKS),
  ("이런 분께 맞아요", L("회 말고 따뜻한 밥이 먹고 싶은 분", "아이, 부모님과 함께 온 가족", "반려동물과 함께 여행하는 분")),
  ("더 보기", L(A("sokcho-trip","속초 여행"), A("sokcho-1bak2il-matjip","속초 1박2일 맛집"), A("sokcho-food-course","속초 먹거리 코스")))],
 [PET, KIDS])

add("sokcho-suljip", "속초 술집", "상황별", "jjim-closeup.jpg",
 "속초에서 한잔할 곳, 생선찜 안주에 소주 한 병.",
 [("생선찜과 술", "<p>매콤한 생선찜은 소주, 막걸리와 잘 어울립니다. 가오리찜의 오독한 연골과 대구뽈의 쫀득한 볼살은 안주로 특히 인기입니다.</p>"),
  ("이 집에 있는 술", "<p>소주, 맥주, 막걸리, 청하, 백세주가 있습니다.</p>"),
  ("안주로 좋은 메뉴", L(A("sokcho-gaori-jjim","가오리찜"), A("sokcho-daegu-ppol-jjim","대구뽈찜"), A("sokcho-nurungji-squid-sundae","누룽지 오징어순대"))),
  ("더 보기", L(A("daepohang-anju","대포항 술안주"), A("jjim-sulanju","생선찜 술안주"), A("sokcho-hoesik","속초 회식 장소")))],
 [("늦게까지 하나요?",f"영업시간은 전화({TEL})로 확인해 주세요."), SIZE])

add("sokcho-parking-matjip", "속초 주차 되는 맛집", "상황별", "storefront.jpg",
 "차 가지고 가는 속초 여행, 주차 걱정 덜고 먹는 곳.",
 [("속초 주차, 이것만 알면", "<p>속초 시내와 항구 앞은 주말에 주차가 빠듯합니다. 식당 앞을 찾기보다 가까운 공영주차장에 세우고 걸어가는 편이 편합니다.</p>"),
  ("대포항에서는", f"<p>대포항생선찜본점에 오실 때는 대포항 공영주차장을 이용하세요. 자세한 내용은 {A('daepohang-parking','대포항 주차 안내')}에 있습니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("daepohang-directions","대포항 가는 법"), A("sokcho-rentcar","속초 렌터카 여행"), A("sokcho-drive","속초 드라이브 코스")))],
 [PARK, WHERE])

add("sokcho-harbor-matjip", "속초 항구 맛집", "대포항", "storefront.jpg",
 "고깃배 드나드는 항구 앞에서 먹는 생선 한 상.",
 [("속초의 항구들", "<p>속초에는 대포항, 동명항, 장사항, 외옹치항 같은 작은 항구가 여럿 있습니다. 항구마다 회센터와 먹거리 골목이 있어 구경하는 재미가 있습니다.</p>"),
  ("대포항에서 생선찜", f"<p>대포항은 속초 남쪽 끝 항구입니다. 항구 안쪽 상가 1층의 대포항생선찜본점에서 {A('sokcho-gaori-jjim','가오리찜')}과 {A('sokcho-saengseon-gui','모듬생선구이')}를 드셔 보세요.</p>"),
  ("더 보기", L(A("daepohang-matjip","대포항 맛집"), A("dongmyeonghang-matjip","동명항 맛집"), A("jangsahang-matjip","장사항 맛집")))],
 [WHERE, PARK])

add("daepohang-nurungji-sundae", "대포항 누룽지 오징어순대", "대포항", "squid-sundae.jpg",
 "대포항에서 먹는 바삭한 누룽지 오징어순대.",
 [("누룽지 오징어순대", "<p>오징어 속에 찹쌀과 채소를 꽉 채우고, 겉을 누룽지처럼 바삭하게 지져 냅니다. 겉은 바삭, 속은 쫄깃해서 한 점이면 손이 또 갑니다.</p>"),
  ("가격과 곁들이기", f"<p>17,000원입니다. 찜과 함께 시키면 매콤한 맛 사이에 고소함을 더해 줍니다. 술안주로도 인기입니다.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-nurungji-squid-sundae","속초 누룽지 오징어순대"), A("nurungji-ojingeo-sundae-how-to-eat","누룽지 오징어순대 먹는 법"), A("ojingeo-sundae-takeout","오징어순대 포장")))],
 [TOGO, KIDS])

# ---------- 이웃 지역 + 메뉴 ----------
def _j(w, a, b):
    return a if (ord(w[-1]) - 0xAC00) % 28 else b
def town_dish(slug, kw, town, dish, dish_slug, about, more):
    add(slug, kw, "근처", "gui.jpg" if "구이" in dish else ("squid-sundae.jpg" if "순대" in dish else "jjim-table.jpg"),
     f"{town} 여행 중 {dish}{_j(dish,'이','가')} 생각나면, 속초 대포항으로.",
     [(f"{town}에서 {dish}", f"<p>{about}</p>"),
      ("대포항생선찜본점", f"<p>대포항은 속초 남쪽 끝이라 {town}에서 오가기 편합니다. {A(dish_slug, dish)}{_j(dish,'을','를')} 비롯해 생선찜, 생선구이, 순대를 한 곳에서 드실 수 있습니다.</p>"),
      ("추천 메뉴", MENU_LINKS),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, TOGO])

town_dish("yangyang-saengseon-jjim", "양양 생선찜", "양양", "생선찜", "sokcho-saengseon-jjim",
 "양양은 서핑 해변과 낙산사로 유명합니다. 바다에서 하루를 보내고 나면 매콤한 생선찜에 밥 한 공기가 생각납니다.",
 L(A("yangyang-matjip","양양 맛집"), A("yangyang-surf-matjip","양양 서핑 후 맛집"), A("fish-jjim-matjip","생선찜 맛집")))
town_dish("yangyang-saengseon-gui", "양양 생선구이", "양양", "모듬생선구이", "sokcho-saengseon-gui",
 "양양 바닷가에서 놀다 보면 맵지 않고 담백한 생선구이가 당길 때가 있습니다. 아이와 함께라면 더욱 그렇습니다.",
 L(A("yangyang-matjip","양양 맛집"), A("fish-gui-matjip","생선구이 맛집"), A("gangwon-fish-gui","강원도 생선구이")))
town_dish("yangyang-squid-sundae", "양양 오징어순대", "양양", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae",
 "오징어순대는 속초를 대표하는 별미입니다. 양양에 머물면서도 속초까지 올라와 맛보는 분이 많습니다.",
 L(A("squid-sundae-matjip","오징어순대 맛집"), A("sokcho-ojingeo-sundae","속초 오징어순대"), A("yangyang-matjip","양양 맛집")))
town_dish("goseong-saengseon-jjim", "고성 생선찜", "고성", "생선찜", "sokcho-saengseon-jjim",
 "고성은 조용한 해변과 통일전망대, 화진포로 유명합니다. 고성 여행 길에 속초를 지난다면 생선찜 한 끼를 넣어 보세요.",
 L(A("goseong-matjip","고성 맛집"), A("goseong-trip-matjip","고성 여행 속초 맛집"), A("fish-jjim-matjip","생선찜 맛집")))
town_dish("goseong-saengseon-gui", "고성 생선구이", "고성", "모듬생선구이", "sokcho-saengseon-gui",
 "고성 바닷가 마을은 예전부터 생선을 말리고 구워 먹는 곳이었습니다. 고성 여행 전후로 속초에서 생선구이를 드셔 보세요.",
 L(A("goseong-matjip","고성 맛집"), A("fish-gui-matjip","생선구이 맛집"), A("saengseon-gui-kinds","생선구이 종류")))
town_dish("donghaean-saengseon-jjim", "동해안 생선찜", "동해안", "가오리찜", "sokcho-gaori-jjim",
 "동해안에서는 생선을 꾸덕하게 말려 찜과 조림으로 먹어 왔습니다. 가오리찜, 코다리찜이 대표적입니다.",
 L(A("donghaean-matjip","동해안 맛집"), A("gangwon-fish-jjim","강원도 생선찜"), A("fish-jjim-matjip","생선찜 맛집")))

add("sokcho-fish-restaurant", "속초 생선요리 전문점", "메뉴", "jjim-table.jpg",
 "찜, 구이, 순대까지. 속초 대포항 생선요리 전문점.",
 [("한 곳에서 고르는 생선 요리", L(f"매콤한 찜: {A('sokcho-gaori-jjim','가오리찜')}, {A('sokcho-kodari-jjim','코다리찜')}, {A('sokcho-daegu-ppol-jjim','대구뽈찜')}, {A('sokcho-saengseon-modeum-jjim','생선모듬찜')}", f"맵지 않은 구이: {A('sokcho-saengseon-gui','모듬생선구이')}", f"속초 별미: {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}, {A('sokcho-abai-sundae','아바이순대')}")),
  ("찜은 인원에 맞춰", "<p>찜은 소(2인), 중(3인), 대(4인)로 준비합니다. 여럿이면 찜 하나에 구이나 순대를 더해 보세요.</p>"),
  ("가게 정보", SHOP),
  ("더 보기", L(A("sokcho-fish-dishes","속초 생선요리"), A("sokcho-fish-matjip","속초 생선 맛집"), A("sokcho-what-to-eat","속초 뭐 먹지")))],
 [SIZE, TOGO])
