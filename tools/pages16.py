# 50 keyword pages (added 2026-10-25), batch 651-700.
# Owner asked again for keywords that bring visitors. Not repeating 601-650:
# 가오리찜 x lodgings/sights, new sights x 생선찜·생선구이, 동네 x 생선찜, "속초 OO 추천", 대포항 takeout/lunch.
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


def dish_place(slug, kw, place, dish, dish_slug, img, about, tip, more):
    add(slug, kw, "근처", img, f"{place} 근처에서 {dish}{j(dish,'을','를')} 찾는다면, 대포항으로.",
     [(f"{place}에서", f"<p>{about}</p>"),
      (dish, f"<p>대포항생선찜본점의 {A(dish_slug, dish)}{j(dish,'은','는')} {tip}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, TOGO])

GA = ("가오리찜","sokcho-gaori-jjim","gaori-jjim.jpg","이 집 대표 메뉴입니다. 꾸덕한 가오리를 매콤달콤한 양념에 쪄 내 살은 쫀득하고 연골은 오독합니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.")
JJ = ("생선찜","sokcho-saengseon-modeum-jjim","jjim-table.jpg","여러 생선을 매콤한 양념에 쪄 냅니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.")
GU = ("생선구이","sokcho-saengseon-gui","gui.jpg","그날 들어온 생선을 노릇하게 구워 한 판에 냅니다. 맵지 않아 아이와 어르신도 편합니다.")
MORE_D = {"가오리찜": ("gaori-jjim-matjip","가오리찜 맛집"), "생선찜": ("fish-jjim-matjip","생선찜 맛집"), "생선구이": ("fish-gui-matjip","생선구이 맛집")}

def run(rows, dishes):
    for key, place, about, near_slug, near_kw in rows:
        for d, suffix in dishes:
            m = MORE_D[d[0]]
            dish_place(f"{key}-{suffix}", f"{place} {d[0]}", place, d[0], d[1], d[2], about, d[3], L(A(near_slug, near_kw), A(*m)))

# ---------- 가오리찜 x 숙소·명소 ----------
run([
 ("lotte-resort","속초 롯데리조트","롯데리조트 속초에 묵는다면 이 집 대표 메뉴 가오리찜을 드셔 보세요. 외옹치에서 남쪽으로 내려오면 대포항입니다.","sokcho-lotte-resort-matjip","속초 롯데리조트 근처 맛집"),
 ("cassia","카시아 속초","카시아 속초에서 가까운 대포항에 가오리찜 전문 생선찜 집이 있습니다.","cassia-sokcho-matjip","카시아 속초 근처 맛집"),
 ("maremons","마레몬스","마레몬스에 묵는 날 저녁, 바닷가를 따라 대포항으로 와서 가오리찜을 드셔 보세요.","maremons-matjip","마레몬스 근처 맛집"),
 ("solbeach","쏠비치 양양","쏠비치 양양에서 속초 쪽으로 올라오면 처음 만나는 항구가 대포항입니다.","solbeach-yangyang-matjip","쏠비치 양양 근처 맛집"),
 ("kensington","켄싱턴 설악","설악산 아래 켄싱턴 설악에서 바다 쪽으로 나오면 대포항 가오리찜을 만날 수 있습니다.","kensington-seorak-matjip","켄싱턴 설악 근처 맛집"),
 ("hanwha","한화리조트 설악","한화리조트 설악에서 시내로 나오는 날, 대포항에서 가오리찜으로 한 끼를 채우세요.","hanwha-seorak-matjip","한화리조트 설악 맛집"),
 ("delpino","델피노","델피노에 묵으며 울산바위를 보고 온 날, 저녁 메뉴로 가오리찜은 어떨까요.","delpino-matjip","델피노 근처 맛집"),
 ("ramada","라마다 속초","라마다 속초에 묵는다면 대포항까지 나와 쫀득한 가오리찜을 맛보세요.","ramada-sokcho-matjip","라마다 속초 근처 맛집"),
 ("sokcho-beach","속초해수욕장","속초해수욕장에서 놀고 난 뒤 남쪽 대포항으로 내려오면 가오리찜이 기다립니다.","sokcho-beach-matjip","속초해수욕장 근처 맛집"),
 ("oeongchi","외옹치","외옹치 바다향기로를 걷고 나면 바로 아래 대포항에서 가오리찜으로 식사하세요.","oeongchi-matjip","외옹치 맛집"),
 ("mulchi","물치","물치항에서 속초 쪽으로 넘어오면 대포항이 가깝습니다.","mulchihang-matjip","물치항 근처 맛집"),
 ("seoraksan","설악산","설악산을 다녀와 출출할 때, 매콤달콤한 가오리찜이 산행 피로를 풀어 줍니다.","seoraksan-matjip","설악산 근처 맛집"),
 ("naksan","낙산","낙산 해변과 낙산사를 둘러보고 속초로 올라오는 길에 대포항에 들러 보세요.","naksan-beach-matjip","낙산해수욕장 근처 맛집"),
 ("abai-village","아바이마을","아바이마을에서 갯배를 탄 날, 식사는 대포항 가오리찜으로 이어 가 보세요.","abai-village-matjip","아바이마을 근처 맛집"),
 ("tourist-market","속초관광수산시장","시장 간식으로는 부족할 때, 대포항에서 가오리찜으로 제대로 한 끼를 드세요.","sokcho-tourist-market-matjip","속초관광수산시장 근처 맛집"),
], [(GA, "gaori-jjim")])

# ---------- 새 명소 x 생선찜·생선구이 ----------
run([
 ("yeonggeumjeong","영금정","영금정 정자에서 파도를 보고 난 뒤, 남쪽 대포항으로 내려와 식사하세요.","yeonggeumjeong-matjip","영금정 근처 맛집"),
 ("jangsahang","장사항","속초 북쪽 장사항을 둘러본 날, 시내를 지나 대포항에서 하루를 마무리해 보세요.","jangsahang-matjip","장사항 맛집"),
 ("sokcho-lighthouse","속초등대","속초등대 전망대에서 바다와 설악산을 본 뒤 대포항으로 이동해 식사하기 좋습니다.","sokcho-lighthouse-matjip","속초등대 맛집"),
 ("seorak-haemaji","설악해맞이공원","설악해맞이공원에서 해돋이를 본 아침이나 산책 뒤, 대포항이 가깝습니다.","seorak-haemaji-matjip","설악해맞이공원 맛집"),
 ("cheoksan","척산온천","척산온천에서 몸을 녹인 뒤 따뜻한 한 끼가 생각난다면 대포항으로 오세요.","cheoksan-oncheon-matjip","척산온천 근처 맛집"),
 ("waterpia","설악워터피아","워터피아에서 신나게 놀고 나면 배가 고픕니다. 바다 쪽 대포항에서 식사하세요.","seorak-waterpia-matjip","설악워터피아 근처 맛집"),
 ("naksansa","낙산사","낙산사와 의상대를 둘러보고 속초로 올라오는 길에 대포항이 있습니다.","naksansa-matjip","낙산사 가는 길 맛집"),
 ("hajodae","하조대","하조대에서 바다 정자를 보고 북쪽으로 올라오면 속초의 첫 항구 대포항입니다.","hajodae-matjip","하조대 여행 맛집"),
 ("yangyang-airport","양양공항","양양공항에 내려 속초로 가는 길, 첫 끼를 대포항에서 드셔 보세요.","yangyang-airport-matjip","양양공항 맛집"),
 ("intercity-terminal","속초 시외버스터미널","시외버스로 속초에 도착했다면 택시로 대포항까지 와서 첫 끼를 드세요.","sokcho-intercity-terminal-matjip","속초 시외버스터미널 근처 맛집"),
], [(JJ, "saengseon-jjim"), (GU, "saengseon-gui")])

# ---------- 속초 동네 x 생선찜 ----------
run([
 ("joyangdong","속초 조양동","조양동에 사는 분들이 가족 외식으로 찾기 좋은 대포항 생선찜 집입니다.","joyangdong-matjip","조양동 맛집"),
 ("gyodong","속초 교동","교동에서 대포항까지 나와 생선찜으로 외식해 보세요.","gyodong-matjip","속초 교동 맛집"),
 ("nohakdong","속초 노학동","노학동 쪽에서 바다 쪽 대포항으로 나오면 생선찜 전문점이 있습니다.","nohakdong-matjip","속초 노학동 맛집"),
 ("cheonghodong","속초 청호동","청호동 아바이마을 쪽에서 남쪽 대포항으로 오면 생선찜을 드실 수 있습니다.","cheonghodong-matjip","속초 청호동 맛집"),
 ("yeongnangdong","속초 영랑동","영랑동에서 시내를 지나 대포항으로 오는 생선찜 외식, 주말 가족 식사로 좋습니다.","yeongnangdong-matjip","속초 영랑동 맛집"),
 ("dongmyeongdong","속초 동명동","동명동에서 남쪽 대포항까지 나와 생선찜 한 냄비 어떠세요.","dongmyeongdong-matjip","속초 동명동 맛집"),
 ("geumhodong","속초 금호동","금호동 쪽 동네 외식으로 대포항 생선찜을 찾는 분들이 많습니다.","geumhodong-matjip","속초 금호동 맛집"),
 ("seorakdong","설악동","설악동에서 내려와 바다 쪽 대포항에서 생선찜을 드셔 보세요.","seorakdong-matjip","설악동 맛집"),
], [(JJ, "saengseon-jjim")])

# ---------- 속초 OO 추천 ----------
def rec(slug, kw, dish, dish_slug, img, why, order, more):
    add(slug, kw, "메뉴", img, f"속초에서 {dish}{j(dish,'을','를')} 먹는다면 이 집을 추천하는 이유.",
     [("추천하는 이유", f"<p>{why}</p>"),
      ("이렇게 시켜 보세요", f"<p>{order}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", L(A(dish_slug, dish), *more))],
     [SIZE, TOGO])

rec("sokcho-jjim-recommend", "속초 생선찜 추천", "생선찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "대포항생선찜본점은 이름 그대로 생선찜 전문점입니다. 가오리찜, 코다리찜, 대구뽈찜, 생선모듬찜까지 찜 메뉴만 네 가지입니다.",
 "고르기 어렵다면 생선모듬찜, 하나만 고른다면 대표 메뉴 가오리찜을 추천합니다.",
 [A("fish-jjim-matjip","생선찜 맛집"), A("jjim-size-guide","생선찜 사이즈 고르기")])
rec("sokcho-gui-recommend", "속초 생선구이 추천", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 "여러 생선을 한 판에 구워 내 골라 먹는 재미가 있고, 맵지 않아 아이와 어르신도 편하게 드십니다.",
 "찜 하나와 구이 하나를 함께 시키면 매콤한 맛과 담백한 맛을 같이 즐길 수 있습니다.",
 [A("fish-gui-matjip","생선구이 맛집"), A("jjim-gui-together","생선찜 생선구이 같이")])
rec("sokcho-gaori-recommend", "속초 가오리찜 추천", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg",
 "가오리찜은 이 집에서 가장 많이 나가는 대표 메뉴입니다. 삭히지 않은 가오리라 냄새 걱정이 없습니다.",
 "둘이면 소(2인), 셋이면 중(3인), 넷이면 대(4인)입니다. 남은 양념에 밥을 비벼 드세요.",
 [A("gaori-jjim-matjip","가오리찜 맛집"), A("gaori-jjim-how-to-eat","가오리찜 맛있게 먹는 법")])
rec("sokcho-squid-sundae-recommend", "속초 오징어순대 추천", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg",
 "오징어순대를 팬에 지져 겉을 누룽지처럼 바삭하게 만든 것이 이 집만의 방식입니다. 17,000원입니다(바뀔 수 있습니다).",
 "찜에 곁들이는 메뉴로도, 포장해 숙소 야식으로도 좋습니다.",
 [A("squid-sundae-matjip","오징어순대 맛집"), A("nurungji-ojingeo-sundae-how-to-eat","누룽지 오징어순대 먹는 법")])

# ---------- 대포항 포장·점심 ----------
def dp(slug, kw, dish, dish_slug, img, lede, scene, order, more, faq):
    add(slug, kw, "대포항", img, lede,
     [(kw, f"<p>{scene}</p>"),
      ("이렇게 드세요", f"<p>{order}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", L(A(dish_slug, dish), *more))],
     faq)

dp("daepohang-jjim-takeout", "대포항 생선찜 포장", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "숙소에서 먹는 생선찜, 대포항에서 포장해 가세요.",
 "찜은 국물이 있어 포장해 가도 다시 데우기 쉽습니다. 숙소에서 편하게 드시고 싶은 분들이 많이 포장해 갑니다.",
 f"미리 전화({TEL})로 주문하면 기다리지 않고 받아 가실 수 있습니다. {A('saengseon-jjim-reheat','생선찜 포장 데우는 법')}도 참고하세요.",
 [A("daepohang-takeout","대포항 포장")], [TOGO, SIZE])
dp("daepohang-gaori-takeout", "대포항 가오리찜 포장", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg",
 "대표 메뉴 가오리찜, 대포항에서 포장해 가기.",
 "가오리찜을 숙소나 집에서 드시고 싶다면 포장하세요. 소(2인)부터 대(4인)까지 모두 포장됩니다.",
 f"전화({TEL})로 사이즈를 말씀하고 시간 맞춰 오시면 됩니다.",
 [A("gaori-jjim-takeout","가오리찜 포장")], [TOGO, SIZE])
dp("daepohang-kodari-lunch", "대포항 코다리찜 점심", "코다리찜", "sokcho-kodari-jjim", "jjim-closeup.jpg",
 "밥도둑 코다리찜으로 대포항 점심.",
 "양념이 속까지 밴 코다리찜은 밥과 잘 맞아 점심 메뉴로 좋습니다.",
 "공깃밥을 넉넉히 시켜 남은 양념에 비벼 드세요.",
 [A("daepohang-kodari-jjim","대포항 코다리찜")], [SIZE, PARK])

assert len(P) == 50, len(P)
