# 50 keyword pages (added 2026-10-31), batch 1001-1050.
# Owner asked for keywords many people actually search. Near-대포항 place x menu combos are used up, so this batch
# is the plain high-volume forms not built yet: 속초 + dish + 맛집, 속초/대포항 맛집 순위·리스트·유명한·줄서는,
# 점심·저녁 추천/메뉴, 속초 식당/밥집 추천, who-with (커플/가족여행/2인), 대표 음식·별미, 대포항 웨이팅/영업시간.
# Store facts only from the listing / photos. No invented reviews, ranks or prices. Area facts kept general.
from pages2 import add as _add, L, A
from pages18 import WHERE, TOGO, SIZE, SHOP, j
from pages20 import DI
from reviews import NAVER_RATING as R, NAVER_REVIEW_COUNT as RC

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

GAORI, MODEUM, GUI, SQUID = DI['gaori'][1], DI['modeum'][1], DI['gui'][1], DI['squid'][1]
KODARI, DAEGU, ABAI = DI['kodari'][1], DI['daegu'][1], DI['abai'][1]
OFF = ("휴무일은?", "매주 수요일입니다.")
WAIT = ("기다려야 하나요?", "주말 저녁이나 연휴에는 기다릴 수 있습니다. 출발 전에 전화(0507-1364-4060)로 자리를 물어보세요.")
KIDS = ("아이와 가도 되나요?", "네, 아기 의자가 있고 맵지 않은 생선구이와 순대가 있습니다.")
STAR = f"네이버 플레이스 별점 {R}, 방문자 리뷰 {RC}개(2026년 10월 기준)"
SMAT, DMAT = A("sokcho-matjip", "속초 맛집"), A("daepohang-matjip", "대포항 맛집")

def page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    add(slug, kw, cat, img, lede, [(h1, f"<p>{p1}</p>"), (h2, f"<p>{p2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))], faq)

# ---------- 속초 + dish + 맛집 ----------
def dish(slug, kw, dk, img, lede, p1, p2, base, faq2):
    d = DI[dk][0]
    page(slug, kw, "메뉴", img, lede, f"속초에서 {d}{j(d,'을','를')} 찾는다면", p1, "주문 팁", p2,
         [A(base, f"속초 {d}"), SMAT], [WHERE, faq2])
dish("sokcho-saengseon-jjim-matjip", "속초 생선찜 맛집", "jjim", "jjim-table.jpg", "속초 생선찜 맛집, 대포항 안쪽 대포항생선찜본점.",
     f"속초에서 생선찜은 회만큼 많이 찾는 메뉴입니다. 대포항생선찜본점은 이름 그대로 생선찜을 전문으로 하고, 대표는 {GAORI}, 여러 생선을 담은 {MODEUM}, {KODARI}, {DAEGU} 네 가지입니다.",
     "찜은 소(2인), 중(3인), 대(4인) 중에서 고릅니다. 처음이라면 대표 메뉴 가오리찜, 여러 맛을 보고 싶다면 생선모듬찜이 좋습니다. 남은 양념에 공깃밥을 비벼 마무리하세요.",
     "sokcho-saengseon-jjim", SIZE)
dish("sokcho-saengseon-gui-matjip", "속초 생선구이 맛집", "gui", "gui.jpg", "속초 생선구이 맛집, 맵지 않은 모듬생선구이 한 판.",
     f"매운 걸 못 드시는 분, 아이와 어르신이 함께라면 생선구이가 편합니다. 대포항생선찜본점의 {GUI}는 그날 들어온 여러 생선을 노릇하게 구워 한 판에 냅니다.",
     f"둘이라면 생선구이 하나에 {SQUID}를 곁들이고, 넷이라면 찜 하나와 생선구이를 같이 시켜 매운맛과 담백한 맛을 나눠 드세요.",
     "sokcho-saengseon-gui", TOGO)
dish("sokcho-gaori-jjim-matjip", "속초 가오리찜 맛집", "gaori", "gaori-jjim.jpg", "속초 가오리찜 맛집, 이 집 대표 메뉴입니다.",
     "가오리찜은 대포항생선찜본점에서 가장 많이 나가는 대표 메뉴입니다. 쫀득한 살과 오독한 연골을 매콤한 양념에 쪄 냅니다. 삭히지 않은 가오리라 냄새가 없어 처음 드시는 분도 편합니다.",
     "소(2인), 중(3인), 대(4인)로 고르고, 맵기가 걱정되면 주문할 때 말씀해 주세요. 콩나물과 양념에 밥을 비벼 먹는 것까지가 가오리찜입니다.",
     "sokcho-gaori-jjim", SIZE)
dish("sokcho-kodari-jjim-matjip", "속초 코다리찜 맛집", "kodari", "jjim-closeup.jpg", "속초 코다리찜 맛집, 쫄깃한 명태를 매콤달콤하게.",
     f"코다리찜은 꾸덕하게 말린 명태를 양념에 쪄 낸 강원도 바닷가 대표 반찬 같은 요리입니다. 대포항생선찜본점의 {KODARI}은 매콤달콤한 양념이 살에 배어 밥반찬으로 좋습니다.",
     "가시가 적고 살이 쫄깃해서 어르신들이 특히 좋아하십니다. 소(2인)부터 시킬 수 있습니다.",
     "sokcho-kodari-jjim", SIZE)
dish("sokcho-daegu-ppol-jjim-matjip", "속초 대구뽈찜 맛집", "daegu", "jjim-closeup.jpg", "속초 대구뽈찜 맛집, 쫀득한 대구 볼살.",
     f"대구뽈찜은 대구 머리의 볼살을 쪄 낸 요리로, 한 마리에서 조금밖에 나오지 않는 쫀득한 부위를 먹습니다. 대포항생선찜본점에서는 {DAEGU}을 소·중·대로 냅니다.",
     "뼈 사이 살을 발라 먹는 재미가 있어 술안주로도 좋고, 찬바람 부는 계절에 특히 잘 어울립니다.",
     "sokcho-daegu-ppol-jjim", SIZE)
dish("sokcho-modeum-jjim-matjip", "속초 생선모듬찜 맛집", "modeum", "jjim-table.jpg", "속초 생선모듬찜 맛집, 여러 생선을 한 냄비에.",
     f"메뉴를 하나만 고르기 어렵다면 {MODEUM}이 답입니다. 여러 생선을 한 냄비에 담아 매콤하게 쪄 내서 일행마다 좋아하는 생선을 골라 먹을 수 있습니다.",
     "가족이나 친구 넷이라면 대(4인) 하나에 아이 몫 생선구이를 더하면 모두 편합니다.",
     "sokcho-saengseon-modeum-jjim", SIZE)
dish("sokcho-ojingeo-sundae-matjip", "속초 오징어순대 맛집", "squid", "squid-sundae.jpg", "속초 오징어순대 맛집, 겉이 바삭한 누룽지 오징어순대.",
     f"오징어순대는 속초에 오면 꼭 먹는 음식 중 하나입니다. 대포항생선찜본점의 {SQUID}는 팬에 지져 겉을 누룽지처럼 바삭하게 만든 것이 특징입니다. 17,000원입니다(바뀔 수 있습니다).",
     "찜이 나오기 전에 먼저 시켜 나눠 먹기 좋고, 포장해서 숙소에서 드셔도 됩니다.",
     "sokcho-ojingeo-sundae", TOGO)
dish("sokcho-nurungji-squid-sundae-matjip", "속초 누룽지 오징어순대 맛집", "squid", "squid-sundae2.jpg", "속초 누룽지 오징어순대 맛집, 바삭하게 지진 한 접시.",
     "누룽지 오징어순대는 오징어순대를 팬에 눌러 지져 겉면을 누룽지처럼 바삭하게 만든 메뉴입니다. 겉은 바삭하고 속은 촉촉해서 그냥 오징어순대와 식감이 다릅니다.",
     "한 접시 17,000원(바뀔 수 있습니다). 맥주나 막걸리 안주로도 좋고, 아이들도 잘 먹습니다.",
     "sokcho-nurungji-squid-sundae", TOGO)
dish("sokcho-abai-sundae-matjip", "속초 아바이순대 맛집", "abai", "abai-sundae.jpg", "속초 아바이순대 맛집, 찜에 곁들이는 속초 순대.",
     f"아바이순대는 함경도 실향민의 손맛에서 시작된 속초 대표 음식입니다. 대포항생선찜본점에서도 {ABAI}를 내서, 생선찜과 함께 속초 음식을 한 번에 맛볼 수 있습니다.",
     "찜을 기다리는 동안 먼저 한 접시 시키거나, 포장해서 숙소에서 드세요.",
     "sokcho-abai-sundae", TOGO)
page("sokcho-haemul-jjim-matjip", "속초 해물찜 맛집", "메뉴", "jjim-table.jpg", "속초 해물찜 찾는다면, 생선찜은 어떠세요.",
     "해물찜 대신 생선찜", f"대포항생선찜본점은 해물찜이 아니라 생선찜 전문점입니다. 매콤한 양념에 콩나물, 밥 비벼 먹는 마무리는 해물찜과 같지만, 주인공이 {GAORI}, {MODEUM}, {KODARI}, {DAEGU} 같은 생선입니다.",
     "이런 분께", "아귀찜이나 해물찜을 좋아한다면 쫀득한 가오리찜이 잘 맞습니다. 여러 가지를 맛보고 싶다면 생선모듬찜을 고르세요.",
     [A("sokcho-haemul-jjim", "속초 해물찜"), A("sokcho-saengseon-jjim", "속초 생선찜")], [SIZE, WHERE])
page("daepohang-haemul-jjim-matjip", "대포항 해물찜 맛집", "대포항", "gaori-jjim.jpg", "대포항에서 해물찜 생각날 때, 항구 안쪽 생선찜집.",
     "대포항에서 찜 한 냄비", "대포항은 회센터와 튀김이 유명하지만, 찜을 먹을 곳을 찾는 분도 많습니다. 대포항생선찜본점은 항구 안쪽 상가 1층에서 생선찜을 냅니다.",
     "무엇을 시킬까", f"해물찜처럼 매콤하고 푸짐한 걸 원하면 {MODEUM}, 쫀득한 식감을 좋아하면 대표 메뉴 {GAORI}입니다.",
     [A("daepohang-haemul-jjim", "대포항 해물찜"), DMAT], [SIZE, TOGO])

# ---------- 맛집 순위 / 리스트 / 유명한 ----------
def best(slug, kw, img, lede, h1, p1, h2, p2, more, faq):
    page(slug, kw, "맛집", img, lede, h1, p1, h2, p2, more, faq)
best("sokcho-matjip-ranking", "속초 맛집 순위", "storefront.jpg", "속초 맛집 순위를 볼 때 함께 보면 좋은 집.",
     "순위보다 리뷰 수", f"속초 맛집 순위는 어디서 보느냐에 따라 다릅니다. 순위표 대신 실제 다녀간 사람 수를 보는 것도 방법입니다. 대포항생선찜본점은 {STAR}입니다.",
     "이 집을 고르는 이유", f"회 말고 따뜻한 한 끼를 찾는 분들이 많이 옵니다. 대표 메뉴는 {GAORI}이고, 맵지 않은 {GUI}와 {SQUID}도 있습니다.",
     [SMAT, DMAT], [WHERE, OFF])
best("sokcho-matjip-list", "속초 맛집 리스트", "jjim-table.jpg", "속초 맛집 리스트에 생선찜 한 곳을 넣는다면.",
     "리스트에 넣을 한 곳", "속초 맛집 리스트에는 보통 물회, 순두부, 닭강정, 오징어순대가 들어갑니다. 여기에 생선찜 한 곳을 더하면 여행 식단이 겹치지 않습니다.",
     "대포항생선찜본점", f"대포항 안쪽 상가 1층, {GAORI}과 {MODEUM}, {GUI}를 내는 집입니다. {STAR}.",
     [SMAT, A("sokcho-food", "속초 먹거리")], [WHERE, SIZE])
best("sokcho-famous-matjip", "속초 유명한 맛집", "ball-wall.jpg", "속초 유명한 맛집, 사인볼이 가득한 벽.",
     "가게에 들어서면", "대포항생선찜본점 안쪽 벽에는 다녀간 손님들이 남긴 사인볼이 가득합니다. 프로농구 삼성썬더스 선수단이 다녀간 사진도 있습니다.",
     "많이 찾는 메뉴", f"가장 많이 나가는 메뉴는 {GAORI}입니다. {STAR}.",
     [SMAT, A("sokcho-matjip-ranking", "속초 맛집 순위")], [WHERE, WAIT])
best("sokcho-must-go-matjip", "속초 꼭 가야할 맛집", "gaori-jjim.jpg", "속초에서 꼭 한 번 먹어볼 음식, 가오리찜.",
     "속초에서 한 번은", f"속초에 왔다면 회와 물회 말고도 꼭 먹어볼 음식이 있습니다. 쫀득한 {GAORI}과 바삭한 {SQUID}, 실향민의 {ABAI}는 속초다운 한 상입니다.",
     "언제 가면 좋을까", "점심이나 이른 저녁이 여유롭습니다. 매주 수요일은 쉽니다.",
     [SMAT, A("sokcho-must-eat", "속초 꼭 먹어야 할 음식")], [OFF, WHERE])
best("sokcho-matjip-map", "속초 맛집 지도", "storefront.jpg", "속초 맛집 지도에서 대포항을 찾으세요.",
     "지도에서 찾기", "속초 맛집은 크게 시내(중앙시장, 동명항), 청초호·아바이마을, 남쪽 대포항으로 나뉩니다. 대포항생선찜본점은 남쪽 대포항 안쪽 상가 1층, 속초시 대포항길 10에 있습니다.",
     "동선 짜기", "외옹치, 롯데리조트, 설악해맞이공원 쪽 일정이라면 대포항에서 식사하는 동선이 편합니다. 아래 버튼으로 바로 길찾기를 할 수 있습니다.",
     [SMAT, A("daepohang-parking", "대포항 주차")], [WHERE, ("주차는?", "대포항 공영주차장을 이용하시면 됩니다.")])
best("sokcho-line-up-matjip", "속초 줄서는 맛집", "hall.jpg", "속초 줄서는 맛집, 기다리기 싫다면 이렇게.",
     "줄이 생기는 때", "주말 저녁과 연휴, 여름 성수기에는 대포항 일대 식당 대부분에 줄이 생깁니다. 대포항생선찜본점도 붐비는 시간에는 기다릴 수 있습니다.",
     "덜 기다리는 법", "점심 조금 지난 시간이나 이른 저녁에 오시고, 출발 전에 전화로 자리를 물어보세요. 포장도 됩니다.",
     [SMAT, A("sokcho-no-wait-matjip", "속초 웨이팅 없는 맛집")], [WAIT, TOGO])
best("sokcho-no-wait-matjip", "속초 웨이팅 없는 맛집", "hall3.jpg", "속초에서 오래 기다리기 싫을 때, 넓은 홀이 있는 집.",
     "넓은 홀", "대포항생선찜본점은 홀이 넓어 여럿이 와도 자리 잡기가 수월한 편입니다. 그래도 주말 저녁과 연휴에는 기다릴 수 있으니 전화로 먼저 확인하세요.",
     "기다리지 않는 방법", "평일이나 식사 시간을 조금 비켜서 오시면 여유롭습니다. 기다리기 싫다면 포장해서 숙소에서 드셔도 됩니다.",
     [SMAT, A("sokcho-line-up-matjip", "속초 줄서는 맛집")], [WAIT, TOGO])
best("sokcho-jjin-matjip", "속초 찐맛집", "jjim-closeup.jpg", "속초 찐맛집, 한 가지를 오래 해 온 집.",
     "한 가지를 잘하는 집", f"대포항생선찜본점은 이름처럼 생선찜이 중심입니다. {GAORI}, {MODEUM}, {KODARI}, {DAEGU}에 {GUI}와 순대가 전부라 메뉴가 단출합니다.",
     "다녀간 사람들", f"{STAR}. 안쪽 벽의 사인볼도 볼거리입니다.",
     [SMAT, A("sokcho-hidden-matjip", "속초 숨은 맛집")], [WHERE, SIZE])
best("daepohang-matjip-ranking", "대포항 맛집 순위", "storefront.jpg", "대포항 맛집 순위, 회 말고 찜집 한 곳.",
     "대포항 맛집 고르기", "대포항 맛집 순위에는 회센터, 튀김, 새우구이가 많이 오릅니다. 회 말고 밥이 되는 한 끼를 찾는다면 생선찜집도 함께 보세요.",
     "대포항생선찜본점", f"항구 안쪽 상가 1층, {STAR}. 대표 메뉴는 {GAORI}입니다.",
     [DMAT, A("daepohang-matjip-recommend", "대포항 맛집 추천")], [WHERE, OFF])
best("daepohang-matjip-best", "대포항 맛집 베스트", "jjim-table.jpg", "대포항 맛집 베스트, 찜 한 냄비.",
     "베스트 메뉴", f"대포항생선찜본점에서 대표 메뉴는 {GAORI}이고, 여러 생선을 담은 {MODEUM}도 많이 찾습니다. 매운 걸 못 드시면 {GUI}를 고르세요.",
     "같이 시키면 좋은 것", f"찜이 나오기 전에 {SQUID} 한 접시, 마무리로 공깃밥을 양념에 비벼 드세요.",
     [DMAT, A("daepohang-matjip-ranking", "대포항 맛집 순위")], [SIZE, WHERE])
best("daepohang-famous-matjip", "대포항 유명한 맛집", "ball-wall.jpg", "대포항 유명한 맛집, 사인볼 벽이 있는 생선찜집.",
     "사인볼 벽", "대포항생선찜본점 안쪽 벽에는 손님들이 남긴 사인볼이 가득합니다. 삼성썬더스 농구단이 다녀간 사진도 걸려 있습니다.",
     "대표 메뉴", f"{GAORI}, {MODEUM}, {GUI}. {STAR}.",
     [DMAT, A("sokcho-famous-matjip", "속초 유명한 맛집")], [WHERE, WAIT])
best("daepohang-matjip-list", "대포항 맛집 리스트", "storefront.jpg", "대포항 맛집 리스트에 넣을 생선찜집.",
     "대포항에서 먹는 것들", "대포항 하면 회센터, 튀김골목, 새우·대게가 먼저 떠오릅니다. 여기에 밥이 되는 생선찜을 더하면 대포항 한 바퀴 먹거리가 완성됩니다.",
     "리스트에 넣을 한 곳", f"대포항생선찜본점: {GAORI}, {MODEUM}, {GUI}, {SQUID}. 매주 수요일 휴무.",
     [DMAT, A("daepohang-meokgeori", "대포항 먹거리")], [WHERE, OFF])
best("daepohang-gasungbi-matjip", "대포항 가성비 맛집", "jjim-table.jpg", "대포항 가성비, 찜 하나로 넷이 배부르게.",
     "인원에 맞춰 고르기", "찜은 소(2인), 중(3인), 대(4인)로 나뉘어 있어 인원에 맞게 고르면 남기지 않습니다. 남은 양념에 공깃밥을 비비면 든든합니다.",
     "가볍게 먹고 싶다면", f"{SQUID}(17,000원, 바뀔 수 있습니다)나 {GUI}로 가볍게 드셔도 됩니다.",
     [DMAT, A("sokcho-gaseongbi", "속초 가성비 맛집")], [SIZE, TOGO])
best("daepohang-delicious", "대포항 맛있는 집", "gaori-jjim.jpg", "대포항 맛있는 집, 가오리찜 잘하는 곳.",
     "맛있는 이유", "가오리는 삭히지 않은 것을 써서 냄새가 없고, 쫀득한 살과 오독한 연골을 함께 씹는 맛이 있습니다. 양념은 매콤하면서 밥을 부르는 맛입니다.",
     "다녀간 사람들", f"{STAR}.",
     [DMAT, A("sokcho-gaori-jjim", "속초 가오리찜")], [SIZE, WHERE])
best("daepohang-waiting", "대포항 웨이팅", "hall2.jpg", "대포항 웨이팅, 기다리기 전에 전화 한 통.",
     "언제 붐비나", "대포항은 주말 오후부터 저녁, 연휴에 가장 붐빕니다. 대포항생선찜본점도 이때는 기다릴 수 있습니다.",
     "기다리지 않으려면", "출발 전에 전화(0507-1364-4060)로 자리를 물어보세요. 평일이나 이른 저녁이 여유롭고, 포장도 됩니다.",
     [DMAT, A("sokcho-no-wait-matjip", "속초 웨이팅 없는 맛집")], [WAIT, TOGO])
best("daepohang-hours", "대포항 영업시간", "storefront.jpg", "대포항생선찜본점 영업시간과 휴무일.",
     "영업시간", "대포항생선찜본점은 매일 10시에 문을 열어 21시까지 영업합니다. 매주 수요일은 쉽니다.",
     "가기 전에", "명절이나 가게 사정으로 바뀔 수 있으니 멀리서 오신다면 전화(0507-1364-4060)로 한 번 확인해 주세요.",
     [DMAT, A("daepohang-parking", "대포항 주차")], [OFF, WHERE])

# ---------- 점심 / 저녁 추천·메뉴 ----------
def meal(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq)
meal("sokcho-lunch-recommend", "속초 점심 추천", "맛집", "gui.jpg", "속초 점심 추천, 맵지 않은 생선구이 한 판.",
     "속초 점심", "오전에 설악산이나 바다를 보고 왔다면 점심은 든든하게. 대포항생선찜본점은 10시에 문을 열어 점심에 여유롭게 드실 수 있습니다.",
     "점심 메뉴", f"둘이서는 {GAORI} 소(2인), 가볍게는 {GUI}나 {SQUID}가 좋습니다.",
     [A("sokcho-lunch-matjip", "속초 점심 맛집"), SMAT], [OFF, WHERE])
meal("sokcho-dinner-recommend", "속초 저녁 추천", "맛집", "jjim-table.jpg", "속초 저녁 추천, 찜 한 냄비에 한 잔.",
     "속초 저녁", "속초 여행 저녁은 회가 흔하지만, 따뜻한 찜 한 냄비도 좋습니다. 저녁은 21시까지라 너무 늦지 않게 오세요.",
     "저녁 메뉴", f"{GAORI}이나 {MODEUM}을 가운데 두고, 소주, 맥주, 막걸리를 곁들이세요.",
     [A("sokcho-dinner-matjip", "속초 저녁 맛집"), SMAT], [SIZE, WHERE])
meal("sokcho-lunch-menu", "속초 점심 메뉴", "맛집", "squid-sundae.jpg", "속초 점심 메뉴 고민, 찜·구이·순대 중에서.",
     "점심 메뉴 고르기", "속초 점심은 물회, 순두부, 생선구이, 오징어순대가 흔한 선택지입니다. 대포항생선찜본점에서는 이 중 생선구이와 오징어순대를 한 번에, 여기에 생선찜까지 고를 수 있습니다.",
     "인원별", f"1~2명: {GUI} 또는 {SQUID}. 2~3명: {GAORI} 소·중. 4명: 찜 대(4인)에 구이 추가.",
     [A("sokcho-lunch-recommend", "속초 점심 추천"), SMAT], [SIZE, TOGO])
meal("sokcho-dinner-menu", "속초 저녁 메뉴", "맛집", "jjim-closeup.jpg", "속초 저녁 메뉴, 오늘은 회 말고 생선찜.",
     "저녁 메뉴 고르기", "속초에서 이틀째 저녁이라면 회는 이미 드셨을 겁니다. 매콤한 생선찜은 술안주와 밥 둘 다 되는 메뉴입니다.",
     "저녁 메뉴판", f"{GAORI}, {MODEUM}, {KODARI}, {DAEGU}(소·중·대), {GUI}, {SQUID}, {ABAI}.",
     [A("sokcho-dinner-recommend", "속초 저녁 추천"), SMAT], [SIZE, OFF])
meal("daepohang-lunch-menu", "대포항 점심 메뉴", "대포항", "gui.jpg", "대포항 점심 메뉴, 회센터 말고 밥 한 끼.",
     "대포항 점심", "대포항 점심은 회와 튀김만 있는 게 아닙니다. 항구 안쪽 상가 1층에서 생선찜과 생선구이로 밥 한 끼를 드실 수 있습니다.",
     "점심 메뉴", f"맵지 않은 {GUI}, 바삭한 {SQUID}, 둘이 든든하게 {GAORI} 소(2인).",
     [A("daepohang-lunch-matjip", "대포항 점심 맛집"), DMAT], [OFF, WHERE])
meal("daepohang-dinner-menu", "대포항 저녁 메뉴", "대포항", "jjim-table.jpg", "대포항 저녁 메뉴, 항구 불빛 아래 찜 한 냄비.",
     "대포항 저녁", "해가 지면 대포항에 불이 켜집니다. 튀김골목을 한 바퀴 돌고 저녁은 찜으로 드세요. 21시까지 영업합니다.",
     "저녁 메뉴", f"{GAORI}, {MODEUM}, {DAEGU}에 소주나 막걸리를 곁들이세요.",
     [A("daepohang-dinner-matjip", "대포항 저녁 맛집"), DMAT], [SIZE, WHERE])
meal("daepohang-what-to-eat", "대포항 뭐 먹지", "대포항", "jjim-closeup.jpg", "대포항 뭐 먹지? 회, 튀김 다음은 생선찜.",
     "대포항에서 고민될 때", "대포항에는 회센터, 튀김, 새우구이, 대게가 있습니다. 회를 못 먹는 일행이 있거나 밥이 당긴다면 생선찜집이 답입니다.",
     "이렇게 고르세요", f"매콤한 게 좋으면 {GAORI}, 여러 가지면 {MODEUM}, 맵지 않게는 {GUI}.",
     [DMAT, A("daepohang-meokgeori", "대포항 먹거리")], [SIZE, TOGO])
meal("daepohang-nearby-bapjip", "대포항 근처 밥집", "대포항", "jjim-table.jpg", "대포항 근처 밥집, 공깃밥 부르는 생선찜.",
     "밥이 되는 한 끼", "대포항 근처는 회와 간식거리가 많아 밥 먹을 곳을 찾기 어렵다는 분이 많습니다. 대포항생선찜본점은 찜과 구이에 공깃밥을 곁들이는 밥집입니다.",
     "추천", f"{KODARI}이나 {GAORI}에 공깃밥, 남은 양념에 밥을 비벼 드세요.",
     [DMAT, A("daepohang-bapjip-recommend", "대포항 밥집 추천")], [WHERE, SIZE])

# ---------- 식당 / 밥집 / 음식 ----------
def gen(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq)
gen("sokcho-restaurant", "속초 식당", "맛집", "hall.jpg", "속초 식당, 대포항 안쪽 넓은 홀의 생선찜집.",
    "어떤 식당인가요", "대포항생선찜본점은 속초 남쪽 대포항 안쪽 상가 1층에 있는 생선찜·생선구이 식당입니다. 홀이 넓고 아기 의자가 있으며 반려동물도 함께 올 수 있습니다.",
    "메뉴", f"{GAORI}, {MODEUM}, {KODARI}, {DAEGU}, {GUI}, {SQUID}, {ABAI}.",
    [SMAT, A("sokcho-restaurant-recommend", "속초 식당 추천")], [WHERE, OFF])
gen("sokcho-restaurant-recommend", "속초 식당 추천", "맛집", "storefront.jpg", "속초 식당 추천, 회 못 먹는 일행도 편한 집.",
    "이런 분께 추천", "회를 못 먹는 일행이 있을 때, 아이나 어르신과 함께일 때, 밥이 당길 때 좋은 식당입니다. 맵지 않은 메뉴도 있습니다.",
    "주문 추천", f"둘이면 {GAORI} 소(2인), 셋이면 중(3인)에 {SQUID}, 넷이면 대(4인)에 {GUI}.",
    [SMAT, A("sokcho-restaurant", "속초 식당")], [SIZE, KIDS])
gen("sokcho-bapjip-recommend", "속초 밥집 추천", "맛집", "jjim-closeup.jpg", "속초 밥집 추천, 양념에 밥 비벼 먹는 생선찜.",
    "밥이 당길 때", "여행 중 간식만 먹다 보면 밥 한 끼가 그립습니다. 매콤한 생선찜 양념은 공깃밥을 부르고, 생선구이는 그 자체로 밥반찬입니다.",
    "추천 메뉴", f"{KODARI}, {GAORI}, {GUI}에 공깃밥. 마지막엔 남은 양념에 밥을 비벼 드세요.",
    [A("sokcho-bapjip", "속초 밥집"), SMAT], [SIZE, WHERE])
gen("daepohang-sikdang", "대포항 식당", "대포항", "storefront.jpg", "대포항 식당, 노란색·분홍색 네온 간판.",
    "찾아오는 법", "대포항 안쪽 상가 1층, 노란색과 분홍색 네온 간판이 대포항생선찜본점입니다. 주소는 속초시 대포항길 10입니다.",
    "메뉴", f"생선찜({GAORI}, {MODEUM}, {KODARI}, {DAEGU}), {GUI}, {SQUID}, {ABAI}. 전 메뉴 포장됩니다.",
    [DMAT, A("daepohang-restaurant", "대포항 식당 추천")], [WHERE, TOGO])
gen("sokcho-anju-matjip", "속초 안주 맛집", "맛집", "squid-sundae2.jpg", "속초 안주 맛집, 바삭한 오징어순대에 찜 한 냄비.",
    "술안주로 좋은 메뉴", f"맥주에는 바삭한 {SQUID}, 소주에는 매콤한 {GAORI}이나 {DAEGU}이 잘 어울립니다.",
    "주류", "소주, 맥주, 막걸리, 청하, 백세주가 있습니다. 저녁은 21시까지라 2차보다는 1차로 오세요.",
    [A("sokcho-suljip", "속초 술집"), SMAT], [SIZE, TOGO])
gen("sokcho-not-hoe", "속초 회 말고", "맛집", "jjim-table.jpg", "속초 회 말고 뭐 먹지? 생선찜과 생선구이.",
    "회 말고 먹을 것", "속초는 회가 유명하지만 매 끼니 회만 먹을 수는 없습니다. 생선을 회가 아닌 찜과 구이로 먹으면 바다의 맛은 그대로, 밥 한 끼가 됩니다.",
    "추천", f"매콤한 {GAORI}, 맵지 않은 {GUI}, 속초 별미 {SQUID}와 {ABAI}.",
    [SMAT, A("daepohang-not-hoe", "대포항 회 말고")], [SIZE, KIDS])
gen("sokcho-representative-food", "속초 대표 음식", "맛집", "abai-sundae.jpg", "속초 대표 음식, 순대와 생선요리를 한 상에.",
    "속초 대표 음식", "속초 대표 음식으로는 오징어순대와 아바이순대, 물회, 생선구이, 닭강정이 많이 꼽힙니다. 실향민 음식과 바다 음식이 섞인 것이 속초 음식의 특징입니다.",
    "한 집에서", f"대포항생선찜본점에서는 {SQUID}, {ABAI}, {GUI}에 생선찜까지 한 번에 맛볼 수 있습니다.",
    [A("sokcho-food", "속초 먹거리"), SMAT], [TOGO, WHERE])
gen("sokcho-hyangto-food", "속초 향토음식", "맛집", "abai-sundae.jpg", "속초 향토음식, 아바이순대와 오징어순대.",
    "속초의 향토음식", "속초 향토음식은 함경도 실향민이 고향 음식을 이곳 재료로 만든 데서 시작한 것이 많습니다. 아바이순대와 오징어순대가 대표적입니다.",
    "맛보는 곳", f"대포항생선찜본점에서 {ABAI}와 {SQUID}를 생선찜과 함께 드실 수 있습니다.",
    [A("sokcho-representative-food", "속초 대표 음식"), SMAT], [TOGO, WHERE])
gen("sokcho-byeolmi", "속초 별미", "맛집", "gaori-jjim.jpg", "속초 별미, 쫀득한 가오리찜.",
    "속초에서 맛볼 별미", "가오리찜은 다른 지역에서는 흔하지 않은 메뉴입니다. 쫀득한 살과 오독한 연골을 함께 씹는 식감이 별미입니다. 삭히지 않아 냄새가 없습니다.",
    "함께 맛볼 별미", f"겉이 바삭한 {SQUID}, 실향민의 {ABAI}.",
    [A("sokcho-gaori-jjim", "속초 가오리찜"), SMAT], [SIZE, WHERE])
gen("sokcho-maeun-matjip", "속초 매운 맛집", "맛집", "jjim-closeup.jpg", "속초 매운 맛집, 매콤한 생선찜.",
    "매콤한 한 냄비", f"매운 음식이 당긴다면 생선찜 양념이 딱입니다. {GAORI}, {KODARI}, {DAEGU} 모두 매콤한 양념에 쪄 냅니다.",
    "맵기 조절", f"맵기가 걱정되면 주문할 때 말씀해 주세요. 매운 걸 못 드시는 일행은 {GUI}를 드시면 됩니다.",
    [A("sokcho-spicy-jjim", "속초 매운 생선찜"), SMAT], [SIZE, KIDS])
gen("daepohang-food-what", "대포항 음식", "대포항", "jjim-table.jpg", "대포항 음식, 회와 튀김 다음은 생선찜.",
    "대포항 음식", "대포항 음식 하면 회, 튀김, 새우구이, 대게가 떠오릅니다. 항구 안쪽에는 생선찜과 생선구이를 내는 식당도 있습니다.",
    "대포항생선찜본점", f"{GAORI}, {MODEUM}, {GUI}, {SQUID}. 전 메뉴 포장됩니다.",
    [DMAT, A("daepohang-meokgeori", "대포항 먹거리")], [WHERE, TOGO])

# ---------- 누구와 / 언제 ----------
gen("sokcho-couple-matjip", "속초 커플 맛집", "맛집", "gaori-jjim.jpg", "속초 커플 맛집, 둘이서 가오리찜 소(2인).",
    "둘이서 속초", f"둘이라면 {GAORI} 소(2인)가 딱 맞습니다. 바삭한 {SQUID} 한 접시를 더하면 든든합니다.",
    "데이트 동선", "대포항 튀김골목과 외옹치 바다향기로를 걷고 저녁을 드세요. 저녁은 21시까지입니다.",
    [A("sokcho-date-matjip", "속초 데이트 맛집"), SMAT], [SIZE, WHERE])
gen("sokcho-family-trip-matjip", "속초 가족여행 맛집", "맛집", "hall3.jpg", "속초 가족여행 맛집, 넓은 홀과 아기 의자.",
    "가족이 편한 집", "가족여행이라면 아이와 어른이 같이 먹을 메뉴, 넓은 자리, 아기 의자가 필요합니다. 대포항생선찜본점은 셋 다 있습니다.",
    "가족 주문", f"넷이라면 {GAORI}이나 {MODEUM} 대(4인)에 아이 몫 {GUI}를 더하세요.",
    [A("sokcho-family-dining", "속초 가족 외식"), SMAT], [KIDS, SIZE])
gen("sokcho-2in-matjip", "속초 2인 맛집", "맛집", "gaori-jjim.jpg", "속초 2인 맛집, 둘이 시키기 좋은 소(2인) 찜.",
    "둘이 시키기 좋은 메뉴", "찜이 소(2인)부터 있어 둘이서도 부담 없이 시킬 수 있습니다. 대표 메뉴 가오리찜 소(2인)가 가장 많이 나갑니다.",
    "조합", f"{GAORI} 소 + {SQUID}, 또는 {GUI} + {ABAI}.",
    [A("sokcho-jjim-2in", "속초 2인 생선찜"), SMAT], [SIZE, WHERE])
page("daepohang-modeum-jjim-matjip", "대포항 생선모듬찜 맛집", "대포항", "jjim-table.jpg", "대포항 생선모듬찜 맛집, 여러 생선을 한 냄비에.",
     "대포항에서 모듬찜", f"대포항에 왔는데 무엇을 먹을지 고르기 어렵다면 {MODEUM}을 시키세요. 여러 생선을 한 냄비에 담아 매콤하게 쪄 내서 일행마다 좋아하는 생선을 골라 먹을 수 있습니다.",
     "주문 팁", "소(2인), 중(3인), 대(4인)로 고릅니다. 남은 양념에 공깃밥을 비벼 마무리하세요.",
     [A("daepohang-modeum-jjim", "대포항 생선모듬찜"), DMAT], [SIZE, WHERE])
