# 50 keyword pages (added 2026-10-29), batch 851-900.
# Owner asked for places people actually visit, built and sent automatically. Busy Sokcho/Yangyang sights x meal/menu not used before.
# Store facts only from the listing / photos. Hours unconfirmed. Area facts kept general (no distances or minutes).
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




GAORI = A('sokcho-gaori-jjim','가오리찜'); MODEUM = A('sokcho-saengseon-modeum-jjim','생선모듬찜'); GUI = A('sokcho-saengseon-gui','모듬생선구이')
SQUID = A('sokcho-nurungji-squid-sundae','누룽지 오징어순대'); KODARI = A('sokcho-kodari-jjim','코다리찜'); DAEGU = A('sokcho-daegu-ppol-jjim','대구뽈찜'); ABAI = A('sokcho-abai-sundae','아바이순대')

# place key: (name, intro, near slug, near keyword)
PL = {
 "sogongwon": ("설악산 소공원", "설악산 소공원은 케이블카와 신흥사로 가는 설악산 여행의 출발점입니다. 산을 내려와 바다 쪽으로 나오면 대포항이 있습니다.", "seorak-sogongwon-matjip", "설악산 소공원 근처 맛집"),
 "cablecar": ("설악 케이블카", "설악 케이블카를 타고 권금성에 다녀오면 반나절이 금방 갑니다. 내려와서 식사는 바다 쪽 대포항에서 하세요.", "seorak-cablecar-matjip", "설악 케이블카 맛집"),
 "ulsanbawi": ("울산바위", "울산바위 코스는 계단이 많아 다녀오면 배가 많이 고픕니다. 하산 뒤 든든한 한 끼가 필요합니다.", "ulsanbawi-matjip", "울산바위 등산 후 맛집"),
 "gwongeumseong": ("권금성", "권금성은 케이블카로 올라 설악산 봉우리를 가까이 보는 곳입니다. 내려와서 바다 쪽으로 나와 식사하세요.", "gwongeumseong-matjip", "권금성 맛집"),
 "sinheungsa": ("신흥사", "신흥사는 소공원에서 가볍게 걸어 닿는 설악산의 큰 절입니다. 둘러본 뒤 대포항으로 내려와 보세요.", "sinheungsa-matjip", "신흥사 맛집"),
 "biseondae": ("비선대", "비선대는 소공원에서 계곡을 따라 걷는 비교적 편한 길 끝에 있습니다. 걷고 나면 출출해집니다.", "biseondae-matjip", "비선대 맛집"),
 "jungang-market": ("속초중앙시장", "속초중앙시장(관광수산시장)은 닭강정과 간식으로 유명합니다. 간식 말고 제대로 된 한 끼는 대포항에서 드셔 보세요.", "sokcho-tourist-market-matjip", "속초관광수산시장 근처 맛집"),
 "abai": ("아바이마을", "아바이마을은 갯배를 타고 건너는 실향민 마을입니다. 구경을 마치고 남쪽 대포항으로 오면 식사할 수 있습니다.", "abai-village-matjip", "아바이마을 근처 맛집"),
 "yeonggeumjeong": ("영금정", "영금정은 바위 위 정자에서 파도를 보는 곳입니다. 바다 구경 뒤 대포항으로 내려와 식사하세요.", "yeonggeumjeong-matjip", "영금정 근처 맛집"),
 "dongmyeong": ("동명항", "동명항은 영금정 바로 옆 속초 북쪽 항구입니다. 남쪽 끝 항구 대포항에서 생선 요리로 이어 가 보세요.", "dongmyeonghang-matjip", "동명항 맛집"),
 "lighthouse": ("속초등대", "속초등대 전망대에 오르면 바다와 설악산이 함께 보입니다. 내려와서 식사는 대포항에서 하세요.", "sokcho-lighthouse-matjip", "속초등대 맛집"),
 "naksan-beach": ("낙산해수욕장", "낙산해수욕장은 양양의 넓은 해변입니다. 북쪽으로 올라오면 속초 첫 항구 대포항이 나옵니다.", "naksan-beach-matjip", "낙산해수욕장 근처 맛집"),
 "naksansa": ("낙산사", "낙산사는 바닷가 절벽 위 절로, 의상대와 홍련암이 유명합니다. 둘러보고 속초로 오는 길에 대포항이 있습니다.", "naksansa-matjip", "낙산사 가는 길 맛집"),
 "surf": ("양양 서핑", "양양 바다에서 서핑을 하고 나면 허기가 몰려옵니다. 속초 쪽으로 올라오면 대포항이 가깝습니다.", "yangyang-surf-matjip", "양양 서핑 후 맛집"),
 "sokcho-eye": ("속초아이 대관람차", "속초아이 대관람차는 속초해수욕장 앞 바닷가 관람차입니다. 타고 나서 남쪽 대포항으로 내려오면 식사할 수 있습니다.", "sokcho-eye-matjip", "속초아이 대관람차 근처 맛집"),
 "museum": ("국립산악박물관", "국립산악박물관은 설악산과 산악 문화를 보여 주는 실내 전시관이라 비 오는 날에도 좋습니다.", "mountain-museum-matjip", "국립산악박물관 근처 맛집"),
 "solbeach": ("쏠비치 양양", "쏠비치 양양에서 속초 쪽으로 올라오면 처음 만나는 항구가 대포항입니다.", "solbeach-yangyang-matjip", "쏠비치 양양 근처 맛집"),
 "hanwha": ("한화리조트 설악", "한화리조트 설악에서 시내로 나오는 날, 대포항에 들러 한 끼를 드셔 보세요.", "hanwha-seorak-matjip", "한화리조트 설악 맛집"),
 "kensington": ("켄싱턴 설악", "켄싱턴 설악은 설악산 바로 아래 호텔입니다. 산 구경 뒤 바다 쪽 대포항으로 나와 보세요.", "kensington-seorak-matjip", "켄싱턴 설악 근처 맛집"),
 "delpino": ("델피노", "델피노에 묵으며 울산바위를 보고 온 날, 식사는 바다 쪽 항구에서 하세요.", "delpino-matjip", "델피노 근처 맛집"),
 "ramada": ("라마다 속초", "라마다 속초에 묵는다면 대포항까지 나와 항구 저녁을 즐겨 보세요.", "ramada-sokcho-matjip", "라마다 속초 근처 맛집"),
 "terminal": ("속초 고속버스터미널", "고속버스로 속초에 도착했다면 택시로 대포항까지 와서 첫 끼를 드세요.", "sokcho-terminal-matjip", "속초 고속버스터미널 근처 맛집"),
}
# dish: (name, link, img, text, more slug, more kw)
DI = {
 "kodari": ("코다리찜", KODARI, "jjim-closeup.jpg", "꾸덕하게 말린 명태를 매콤달콤한 양념에 쪄 내 쫄깃하고 밥반찬으로 좋습니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.", "kodari-jjim-matjip", "코다리찜 맛집"),
 "daegu": ("대구뽈찜", DAEGU, "jjim-closeup.jpg", "대구 머리의 쫀득한 볼살을 뜨끈하게 쪄 냅니다. 찬바람 부는 날 특히 잘 어울립니다.", "daegu-ppol-matjip", "대구뽈찜 맛집"),
 "abai": ("아바이순대", ABAI, "abai-sundae.jpg", "실향민의 손맛에서 시작된 속초 아바이순대입니다. 찜에 곁들이거나 포장해 가기 좋습니다.", "abai-sundae-matjip", "아바이순대 맛집"),
 "jjim": ("생선찜", MODEUM, "jjim-table.jpg", "여러 생선을 매콤한 양념에 쪄 냅니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.", "fish-jjim-matjip", "생선찜 맛집"),
 "modeum": ("생선모듬찜", MODEUM, "jjim-table.jpg", "여러 생선을 한 냄비에 담아 매콤하게 쪄 냅니다. 무엇을 먹을지 고르기 어려울 때 좋습니다.", "fish-jjim-matjip", "생선찜 맛집"),
 "squid": ("오징어순대", SQUID, "squid-sundae.jpg", "팬에 지져 겉을 누룽지처럼 바삭하게 만든 누룽지 오징어순대입니다. 17,000원입니다(바뀔 수 있습니다).", "squid-sundae-matjip", "오징어순대 맛집"),
 "gui": ("생선구이", GUI, "gui.jpg", "그날 들어온 여러 생선을 노릇하게 구워 한 판에 냅니다. 맵지 않아 아이와 어르신도 편합니다.", "fish-gui-matjip", "생선구이 맛집"),
 "gaori": ("가오리찜", GAORI, "gaori-jjim.jpg", "이 집 대표 메뉴입니다. 쫀득한 살과 오독한 연골, 삭히지 않아 냄새가 없습니다.", "gaori-jjim-matjip", "가오리찜 맛집"),
}
MEAL = {
 "점심": ("gui.jpg", f"점심에는 맵지 않은 {GUI}나 {GAORI} 소(2인)가 부담 없습니다. 오후 일정이 있다면 {SQUID}로 가볍게 드셔도 좋습니다."),
 "저녁": ("jjim-table.jpg", f"저녁에는 대표 메뉴 {GAORI}이나 여러 생선을 담은 {MODEUM}을 추천합니다. 소주, 맥주, 막걸리도 있습니다."),
}

def page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    add(slug, kw, cat, img, lede, [(h1, f"<p>{p1}</p>"), (h2, f"<p>{p2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))], faq)

def place_dish(pk, dk):
    n, intro, ns, nk = PL[pk]; d, link, img, text, ms, mk = DI[dk]
    page(f"{pk}-{dk}", f"{n} {d}", "근처", img, f"{n} 근처에서 {d}{j(d,'을','를')} 찾는다면, 대포항으로.",
         f"{n}에서", intro, d, f"대포항생선찜본점의 {link}{j(d,'은','는')} {text}",
         [A(ns, nk), A(ms, mk)], [WHERE, TOGO if dk in ('abai','squid','gui') else SIZE])

def place_meal(pk, meal):
    n, intro, ns, nk = PL[pk]; img, text = MEAL[meal]
    page(f"{pk}-{'lunch' if meal=='점심' else 'dinner'}", f"{n} {meal}", "근처", img, f"{n}에서 {meal} 먹을 곳, 대포항.",
         f"{n}에서", intro, f"{meal} 메뉴", text,
         [A(ns, nk), A("daepohang-lunch" if meal=="점심" else "daepohang-dinner", "대포항 점심" if meal=="점심" else "대포항 저녁")],
         [WHERE, PARK] if meal=="점심" else [SIZE, HOURS])

def place_takeout(pk):
    n, intro, ns, nk = PL[pk]
    page(f"{pk}-takeout", f"{n} 포장 맛집", "근처", "jjim-table.jpg", f"{n} 숙소에서 먹을 저녁, 대포항에서 포장.",
         f"{n}에서", intro, "포장", f"전 메뉴 포장됩니다. 미리 전화({TEL})로 주문하고 시간 맞춰 찾으러 오세요. 데우는 법은 {A('saengseon-jjim-reheat','생선찜 포장 데우는 법')}을 참고하세요.",
         [A(ns, nk), A("sokcho-takeout-matjip","속초 포장 맛집")], [TOGO, HOURS])


def place_family(pk):
    n, intro, ns, nk = PL[pk]
    page(f"{pk}-family", f"{n} 가족 식사", "근처", "hall3.jpg", f"{n} 다녀온 가족, 식사는 대포항 생선찜.",
         f"{n}에서", intro, "가족 주문", f"넷이라면 {GAORI} 대(4인)에 아이 몫으로 맵지 않은 {GUI}를 더하세요. 아기의자가 있고 홀이 넓습니다.",
         [A(ns, nk), A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])

def pd(pk, dk): place_dish(pk, dk)
def pm(pk, m): place_meal(pk, m)

pd("sogongwon","jjim"); pd("sogongwon","gui"); pm("sogongwon","점심"); pm("sogongwon","저녁")
pm("cablecar","점심"); pm("cablecar","저녁"); place_family("cablecar")
pd("ulsanbawi","jjim"); pm("ulsanbawi","점심"); pm("ulsanbawi","저녁")
pm("gwongeumseong","점심"); pm("gwongeumseong","저녁")
pm("sinheungsa","점심"); pd("sinheungsa","gui")
pm("biseondae","점심"); pd("biseondae","jjim")
pd("jungang-market","jjim"); pd("jungang-market","gui"); pd("jungang-market","gaori"); pm("jungang-market","저녁")
pm("abai","저녁"); pd("abai","squid"); place_family("abai")
pd("yeonggeumjeong","gaori"); pm("yeonggeumjeong","점심"); pm("yeonggeumjeong","저녁")
pd("dongmyeong","gaori"); pm("dongmyeong","점심"); pm("dongmyeong","저녁")
pm("lighthouse","점심"); pm("lighthouse","저녁")
pd("naksan-beach","jjim"); pd("naksan-beach","gui"); pm("naksan-beach","점심")
pm("naksansa","점심"); pd("naksansa","gaori")
pm("surf","점심"); pm("surf","저녁")
pd("sokcho-eye","jjim"); place_family("sokcho-eye")
pm("museum","점심"); pd("museum","jjim")
pm("solbeach","점심"); place_family("solbeach")
pm("hanwha","점심"); pm("hanwha","저녁")
pm("kensington","점심"); pm("delpino","점심"); pm("ramada","저녁"); pm("terminal","점심")

assert len(P) == 50, len(P)
