# 50 keyword pages (added 2026-10-24), batch 601-650.
# Owner asked for keywords that bring people to the shop itself, and left the choice to Claude.
# So: brand-name questions asked right before a visit, dish x nearby lodging/sight, 대포항 + dish x meal/takeout.
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

# ---------- 가게 이름으로 찾는 질문 ----------
def brand(slug, kw, lede, sections, faq):
    add(slug, kw, "대포항", "storefront.jpg", lede, sections + [("가게 정보", SHOP)], faq)

brand("brand-hours", "대포항생선찜본점 영업시간", "가기 전에 영업시간부터 확인하세요.",
 [("영업시간 확인", f"<p>영업시간은 계절과 그날 사정에 따라 달라질 수 있어 전화({TEL})로 확인하시는 게 가장 정확합니다. 매주 수요일은 정기 휴무입니다.</p>"),
  ("늦게 도착한다면", "<p>마감 무렵에 도착할 것 같으면 미리 전화로 주문해 두세요. 포장으로 받아 숙소에서 드셔도 됩니다.</p>")],
 [HOURS, OFF])
brand("brand-dayoff", "대포항생선찜본점 휴무일", "대포항생선찜본점은 매주 수요일 쉽니다.",
 [("정기 휴무", "<p>매주 수요일이 정기 휴무입니다. 명절이나 가게 사정으로 쉬는 날이 바뀔 수 있으니, 수요일 앞뒤나 연휴에는 전화로 한 번 더 확인해 주세요.</p>"),
  ("수요일에 속초라면", f"<p>수요일에 속초에 계신다면 화요일이나 목요일 일정에 넣어 보세요. {A('sokcho-tuesday-matjip','속초 화요일 맛집')}, {A('sokcho-thursday-matjip','속초 목요일 맛집')}도 참고하세요.</p>")],
 [OFF, HOURS])
brand("brand-price", "대포항생선찜본점 가격", "대포항생선찜본점 메뉴와 가격 확인하는 법.",
 [("메뉴", MENU_ALL),
  ("가격 안내", f"<p>누룽지 오징어순대는 17,000원입니다. 찜과 구이는 생선 시세에 따라 가격이 달라질 수 있어 매장이나 전화({TEL})로 확인해 주세요. 찜은 소(2인), 중(3인), 대(4인)로 인원에 맞춰 고르시면 됩니다.</p>")],
 [SIZE, TOGO])
brand("brand-review", "대포항생선찜본점 후기", "다녀간 손님들의 후기는 어디서 볼까.",
 [("후기 보는 곳", "<p>방문 후기는 네이버 지도에서 '대포항생선찜본점'을 검색하면 방문자 리뷰와 블로그 리뷰로 볼 수 있습니다. 사진 리뷰에서 실제 찜과 구이가 어떻게 나오는지 확인해 보세요.</p>"),
  ("손님들이 많이 시키는 메뉴", f"<p>처음 오는 손님은 대표 메뉴인 {A('sokcho-gaori-jjim','가오리찜')}을 가장 많이 고르고, 아이와 함께라면 {A('sokcho-saengseon-gui','모듬생선구이')}를 더합니다.</p>")],
 [WHERE, SIZE])
brand("brand-2in", "대포항생선찜본점 2인 메뉴", "둘이 가면 무엇을 시킬까.",
 [("둘이라면 소 사이즈", f"<p>찜은 소(2인) 사이즈가 있습니다. {A('sokcho-gaori-jjim','가오리찜')} 소 하나에 {A('sokcho-nurungji-squid-sundae','누룽지 오징어순대')}를 더하면 둘이 든든하게 먹을 수 있습니다.</p>"),
  ("맵지 않게 먹고 싶다면", f"<p>매운 걸 잘 못 드시면 {A('sokcho-saengseon-gui','모듬생선구이')}와 순대 조합도 좋습니다.</p>")],
 [SIZE, TOGO])
brand("brand-4in", "대포항생선찜본점 4인 메뉴", "넷이 가면 무엇을 시킬까.",
 [("넷이라면 대 사이즈", f"<p>찜 대(4인) 하나에 {A('sokcho-saengseon-gui','모듬생선구이')}를 더하는 조합이 많습니다. 아이가 있으면 맵지 않은 구이가 아이 몫이 됩니다.</p>"),
  ("여러 생선을 맛보려면", f"<p>한 가지를 고르기 어렵다면 {A('sokcho-saengseon-modeum-jjim','생선모듬찜')} 대를 시켜 여러 생선을 함께 드셔 보세요.</p>")],
 [SIZE, KIDS])
brand("brand-seats", "대포항생선찜본점 좌석", "넓은 홀, 단체도 앉을 수 있는 자리.",
 [("홀", "<p>가게 안은 넓은 홀로 되어 있어 가족 단위나 여러 명이 함께 앉기 좋습니다. 벽에는 사인볼이 가득합니다.</p>"),
  ("여럿이 갈 때", f"<p>인원이 많으면 미리 전화({TEL})로 자리를 문의해 주세요.</p>")],
 [("단체 자리 되나요?",f"전화({TEL})로 문의해 주세요."), KIDS])
brand("brand-waiting", "대포항생선찜본점 웨이팅", "기다리지 않고 먹는 방법.",
 [("붐비는 때", "<p>주말 저녁과 연휴, 단풍철처럼 속초에 사람이 몰리는 때에는 자리가 차 있을 수 있습니다.</p>"),
  ("덜 기다리려면", f"<p>가기 전에 전화({TEL})로 자리를 물어보거나 미리 주문해 두세요. 이른 점심이나 이른 저녁 시간이 비교적 여유롭습니다.</p>")],
 [HOURS, TOGO])
brand("brand-signball", "대포항생선찜본점 사인볼", "벽 가득한 사인볼, 운동선수들이 다녀간 집.",
 [("사인볼 벽", f"<p>가게 벽에는 운동선수들의 사인볼이 가득합니다. 삼성썬더스 농구단도 다녀갔습니다. 자세한 이야기는 {A('sokcho-ball-wall','사인볼 벽 식당')}에 있습니다.</p>"),
  ("사진 찍기 좋은 곳", "<p>식사 전후로 사인볼 벽 앞에서 사진을 남기는 손님이 많습니다.</p>")],
 [WHERE, OFF])
brand("brand-first-visit", "대포항생선찜본점 처음", "대포항생선찜본점에 처음 간다면 알아 둘 것.",
 [("알아 둘 것", L("대표 메뉴는 가오리찜", "찜은 소(2인)·중(3인)·대(4인)", "맵지 않은 메뉴는 모듬생선구이와 순대", "매주 수요일 휴무", "전 메뉴 포장 가능, 반려동물 동반 가능")),
  ("찾아오는 길", f"<p>대포항 안쪽 상가 1층입니다. {A('brand-location','위치 안내')}와 {A('brand-parking','주차 안내')}를 참고하세요.</p>")],
 [SIZE, PARK])

# ---------- 메뉴 x 근처 숙소·명소 ----------
def dish_place(slug, kw, place, dish, dish_slug, img, about, tip, more):
    add(slug, kw, "근처", img, f"{place} 근처에서 {dish}{j(dish,'을','를')} 찾는다면, 대포항으로.",
     [(f"{place}에서", f"<p>{about}</p>"),
      (dish, f"<p>대포항생선찜본점의 {A(dish_slug, dish)}{j(dish,'은','는')} {tip}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", more)],
     [WHERE, TOGO])

JJ = ("생선찜","sokcho-saengseon-modeum-jjim","jjim-table.jpg","여러 생선을 매콤한 양념에 쪄 냅니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.")
GU = ("생선구이","sokcho-saengseon-gui","gui.jpg","그날 들어온 생선을 노릇하게 구워 한 판에 냅니다. 맵지 않아 아이와 어르신도 편합니다.")
PLACES = [
 ("lotte-resort","속초 롯데리조트","롯데리조트 속초는 외옹치 바닷가에 있는 큰 리조트입니다. 남쪽으로 조금만 내려오면 대포항입니다.","sokcho-lotte-resort-matjip","속초 롯데리조트 근처 맛집"),
 ("cassia","카시아 속초","카시아 속초에 묵는다면 저녁 한 끼는 숙소 밖 항구 식당에서 드셔 보세요. 대포항이 가깝습니다.","cassia-sokcho-matjip","카시아 속초 근처 맛집"),
 ("maremons","마레몬스","마레몬스 호텔 쪽에서 바다를 따라 남쪽으로 오면 대포항에 닿습니다.","maremons-matjip","마레몬스 근처 맛집"),
 ("kensington","켄싱턴 설악","켄싱턴 설악에 묵으며 설악산을 다녀왔다면 저녁은 바다 쪽 대포항으로 내려와 보세요.","kensington-seorak-matjip","켄싱턴 설악 근처 맛집"),
 ("solbeach","쏠비치 양양","쏠비치 양양에서 북쪽으로 올라오면 속초의 첫 항구가 대포항입니다.","solbeach-yangyang-matjip","쏠비치 양양 근처 맛집"),
 ("hanwha","한화리조트 설악","한화리조트 설악 쪽에서 시내로 나올 때 대포항에 들러 한 끼를 드셔 보세요.","hanwha-seorak-matjip","한화리조트 설악 맛집"),
 ("delpino","델피노","델피노에 묵는 날, 저녁은 바닷가 항구에서 드시는 건 어떨까요.","delpino-matjip","델피노 근처 맛집"),
 ("ramada","라마다 속초","라마다 속초에 묵는다면 대포항까지 나와 항구 저녁을 즐겨 보세요.","ramada-sokcho-matjip","라마다 속초 근처 맛집"),
 ("cheongchoho","청초호","청초호 둘레길을 걷고 나면 출출해집니다. 바다 쪽 대포항으로 내려와 식사하세요.","cheongchoho-matjip","청초호 근처 맛집"),
 ("yeongnangho","영랑호","영랑호 산책을 마치고 남쪽 대포항으로 오면 따뜻한 한 끼가 기다립니다.","yeongnangho-matjip","영랑호 근처 맛집"),
 ("expo","속초 엑스포공원","엑스포공원과 엑스포타워를 둘러본 뒤 대포항 쪽으로 이동해 식사하기 좋습니다.","sokcho-expo-matjip","속초 엑스포공원 맛집"),
 ("abai","아바이마을","아바이마을에서 갯배를 타고 구경했다면, 식사는 대포항에서 생선 요리로 이어 가 보세요.","abai-village-matjip","아바이마을 근처 맛집"),
 ("market","속초관광수산시장","시장에서 간식을 사고 나서 제대로 된 한 끼가 필요하다면 대포항으로 오세요.","sokcho-tourist-market-matjip","속초관광수산시장 근처 맛집"),
 ("dongmyeong","동명항","동명항과 영금정에서 바다를 본 날, 남쪽 대포항에서 생선 요리로 하루를 마무리하세요.","dongmyeonghang-matjip","동명항 맛집"),
 ("terminal","속초 고속버스터미널","버스로 속초에 도착했다면 첫 끼는 바닷가 항구에서. 택시로 대포항까지 오시면 됩니다.","sokcho-terminal-matjip","속초 고속버스터미널 근처 맛집"),
]
for key, place, about, near_slug, near_kw in PLACES:
    for d, suffix in ((JJ, "jjim"), (GU, "gui")):
        dish_place(f"{key}-saengseon-{suffix}", f"{place} {d[0]}", place, d[0], d[1], d[2], about, d[3],
                   L(A(near_slug, near_kw), A("fish-jjim-matjip" if suffix == "jjim" else "fish-gui-matjip", "생선찜 맛집" if suffix == "jjim" else "생선구이 맛집")))

# ---------- 대포항 + 메뉴 x 점심·저녁·포장 ----------
def dp(slug, kw, dish, dish_slug, img, lede, scene, order, more, faq):
    add(slug, kw, "대포항", img, lede,
     [(kw, f"<p>{scene}</p>"),
      ("이렇게 드세요", f"<p>{order}</p>"),
      ("가게 정보", SHOP),
      ("더 보기", L(A(dish_slug, dish), *more))],
     faq)

dp("daepohang-jjim-lunch", "대포항 생선찜 점심", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "대포항 구경하고 점심은 생선찜.",
 "오전에 대포항을 한 바퀴 돌고 나면 점심때입니다. 항구 안쪽 상가 1층에서 바로 생선찜을 드실 수 있습니다.",
 "여러 생선을 맛보려면 생선모듬찜, 가볍게 먹으려면 소(2인) 사이즈를 고르세요.",
 [A("daepohang-lunch","대포항 점심")], [SIZE, PARK])
dp("daepohang-jjim-dinner", "대포항 생선찜 저녁", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-closeup.jpg",
 "해 질 녘 대포항, 저녁은 생선찜.",
 "해 질 무렵 대포항은 불빛이 켜지며 분위기가 달라집니다. 항구 산책 뒤 따뜻한 생선찜으로 저녁을 드세요.",
 "찜에 술 한잔 곁들이는 손님도 많습니다. 소주, 맥주, 막걸리가 있습니다.",
 [A("daepohang-dinner","대포항 저녁")], [SIZE, HOURS])
dp("daepohang-gui-dinner", "대포항 생선구이 저녁", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 "맵지 않은 저녁, 대포항 생선구이.",
 "저녁에 매운 음식이 부담스럽다면 생선구이가 좋습니다. 여러 생선을 한 판에 구워 냅니다.",
 "찜과 함께 시켜 나눠 먹으면 매운 것과 담백한 것을 함께 즐길 수 있습니다.",
 [A("daepohang-saengseon-gui","대포항 생선구이")], [KIDS, HOURS])
dp("daepohang-gaori-lunch", "대포항 가오리찜 점심", "가오리찜", "sokcho-gaori-jjim", "gaori-jjim.jpg",
 "점심으로 먹는 대포항 가오리찜.",
 "이 집 대표 메뉴인 가오리찜은 점심으로도 많이 찾습니다. 쫀득한 살과 오독한 연골을 맛보세요.",
 "남은 양념에 공깃밥을 비벼 드시면 점심 한 끼로 충분합니다.",
 [A("daepohang-gaori-jjim","대포항 가오리찜")], [SIZE, TOGO])
dp("daepohang-kodari-dinner", "대포항 코다리찜 저녁", "코다리찜", "sokcho-kodari-jjim", "jjim-closeup.jpg",
 "쫄깃한 코다리찜으로 대포항 저녁.",
 "양념이 속까지 밴 코다리찜은 밥반찬으로도 안주로도 좋아 저녁에 잘 어울립니다.",
 "매운 정도가 걱정되면 주문할 때 물어보세요.",
 [A("daepohang-kodari-jjim","대포항 코다리찜")], [SIZE, HOURS])
dp("daepohang-daegu-dinner", "대포항 대구뽈찜 저녁", "대구뽈찜", "sokcho-daegu-ppol-jjim", "jjim-closeup.jpg",
 "찬바람 부는 저녁, 대포항 대구뽈찜.",
 "날이 쌀쌀해지면 쫀득한 볼살의 대구뽈찜이 생각납니다. 뜨끈하게 쪄 내 저녁 한 끼로 좋습니다.",
 "살을 발라 양념에 찍어 드시고, 마지막엔 밥을 비벼 보세요.",
 [A("daepohang-daegu-ppol-jjim","대포항 대구뽈찜")], [SIZE, TOGO])
dp("daepohang-modeum-dinner", "대포항 생선모듬찜 저녁", "생선모듬찜", "sokcho-saengseon-modeum-jjim", "jjim-table.jpg",
 "여러 생선을 한 냄비에, 대포항 저녁.",
 "무엇을 먹을지 의견이 갈릴 때는 생선모듬찜이 답입니다. 여러 생선을 한 냄비에 담아 냅니다.",
 "넷이라면 대(4인), 셋이라면 중(3인)을 고르세요.",
 [A("daepohang-modeum-jjim","대포항 생선모듬찜")], [SIZE, KIDS])
dp("daepohang-squid-takeout", "대포항 오징어순대 포장", "누룽지 오징어순대", "sokcho-nurungji-squid-sundae", "squid-sundae.jpg",
 "숙소에서 먹을 대포항 오징어순대, 포장해 가세요.",
 "누룽지 오징어순대는 포장해서 숙소에서 야식이나 안주로 드시기 좋습니다. 17,000원입니다(바뀔 수 있습니다).",
 f"미리 전화({TEL})로 주문하면 기다리지 않고 받아 가실 수 있습니다. 다시 데우는 법은 {A('squid-sundae-reheat','오징어순대 데우는 법')}을 참고하세요.",
 [A("daepohang-ojingeo-sundae","대포항 오징어순대")], [TOGO, HOURS])
dp("daepohang-abai-takeout", "대포항 아바이순대 포장", "속초 아바이순대", "sokcho-abai-sundae", "abai-sundae.jpg",
 "대포항에서 아바이순대 포장해 가기.",
 "속이 꽉 찬 아바이순대는 포장해서 숙소에서 드시거나 집에 사 가기 좋습니다.",
 f"찜이나 구이와 함께 주문해 포장하셔도 됩니다. 전화({TEL})로 미리 주문하세요.",
 [A("daepohang-abai-sundae","대포항 아바이순대")], [TOGO, HOURS])
dp("daepohang-gui-takeout", "대포항 생선구이 포장", "모듬생선구이", "sokcho-saengseon-gui", "gui.jpg",
 "숙소에서 먹는 생선구이, 대포항에서 포장.",
 "생선구이도 포장됩니다. 숙소에 조리 도구가 있으면 다시 데워 바삭하게 드실 수 있습니다.",
 f"데우는 법은 {A('fish-gui-airfryer','생선구이 에어프라이어')}를 참고하세요.",
 [A("saengseon-gui-takeout","생선구이 포장")], [TOGO, KIDS])

assert len(P) == 50, len(P)
