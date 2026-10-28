# 50 keyword pages (added 2026-10-28), batch 801-850.
# Owner asked for keywords near 대포항 that people actually search; places near 대포항 were nearly used up,
# so this batch adds dish words people type (해물찜, 홍어찜, 명태찜, 대구찜), 양양/고성/강원도/동해안 x dish,
# a few lodgings and sights not yet covered, and 속초 dish x meal/추천.
# Store facts only from the listing / photos. Hours unconfirmed (point to the phone). No invented reviews or prices.
# Area facts kept general (no distances or minutes).
from pages2 import add as _add, L, A
from pages18 import TEL, WHERE, OFF, TOGO, SIZE, PARK, KIDS, HOURS, SHOP, DI, MEAL, j, GAORI, MODEUM, GUI, SQUID, KODARI, DAEGU, ABAI

P = []
def add(*a, **k):
    from pages2 import P as P2
    n = len(P2); _add(*a, **k); P.append(P2.pop(n))

def page(slug, kw, cat, img, lede, h1, p1, h2, p2, more, faq):
    add(slug, kw, cat, img, lede, [(h1, f"<p>{p1}</p>"), (h2, f"<p>{p2}</p>"), ("가게 정보", SHOP), ("더 보기", L(*more))], faq)

def dish_page(slug, kw, cat, dk, lede, h1, p1, more, faq=None):
    d, link, img, text, ms, mk = DI[dk]
    page(slug, kw, cat, img, lede, h1, p1, d, f"대포항생선찜본점의 {link}{j(d,'은','는')} {text}",
         more + [A(ms, mk)], faq or [WHERE, TOGO if dk in ('abai','squid','gui') else SIZE])

# ---------- 대포항 근처 ----------
page("daepohang-nearby-matjip", "대포항 근처 맛집", "대포항", "storefront.jpg", "대포항 근처에서 밥 먹을 곳, 항구 안쪽 상가 1층.",
 "대포항에서", "대포항은 속초 남쪽 끝 항구로, 회센터와 튀김 골목이 모여 있습니다. 회 말고 따뜻한 밥 한 끼가 생각나면 항구 안쪽 상가 1층으로 오세요.",
 "무엇을 먹을까", f"대표 메뉴는 {GAORI}입니다. 맵지 않은 메뉴를 원하면 {GUI}, 가볍게는 {SQUID}가 좋습니다.",
 [A("daepohang-matjip","대포항 맛집"), A("daepohang-not-hoe","대포항 회 말고 먹을거")], [WHERE, PARK])
dish_page("daepohang-nearby-gui", "대포항 근처 생선구이", "대포항", "gui", "대포항 근처에서 생선구이 한 판.",
 "대포항에서", "대포항 구경을 마치고 맵지 않은 한 끼를 찾는다면 생선구이가 편합니다. 아이와 어르신도 함께 드시기 좋습니다.",
 [A("daepohang-saengseon-gui","대포항 생선구이")])

# ---------- 찾는 말이 다른 메뉴 ----------
page("sokcho-haemul-jjim", "속초 해물찜", "메뉴", "jjim-table.jpg", "속초에서 해물찜을 찾는다면, 생선찜은 어떠세요.",
 "해물찜 대신", "이 집은 해물찜이 아니라 생선찜 전문점입니다. 매콤한 양념에 콩나물과 함께 쪄 내는 방식은 비슷하지만, 주인공이 생선입니다.",
 "추천 메뉴", f"여러 생선을 한 냄비에 담은 {MODEUM}, 대표 메뉴 {GAORI}, 쫀득한 볼살의 {DAEGU}가 있습니다. 소(2인), 중(3인), 대(4인)로 고를 수 있습니다.",
 [A("sokcho-saengseon-jjim","속초 생선찜"), A("sokcho-jjim-matjip","속초 찜 맛집")], [SIZE, WHERE])
page("daepohang-haemul-jjim", "대포항 해물찜", "대포항", "jjim-table.jpg", "대포항에서 매콤한 찜 한 냄비.",
 "대포항에서", "대포항에서 매콤한 찜이 당긴다면 항구 안쪽 상가 1층 생선찜집을 찾아 주세요. 해물찜 대신 생선찜을 냅니다.",
 "추천 메뉴", f"처음이라면 {GAORI}, 여러 가지를 맛보고 싶다면 {MODEUM}을 추천합니다.",
 [A("daepohang-saengseon-jjim","대포항 생선찜"), A("daepohang-matjip","대포항 맛집")], [SIZE, PARK])
page("yangyang-haemul-jjim", "양양 해물찜", "근처", "jjim-table.jpg", "양양에서 매콤한 찜이 생각나면, 속초 대포항.",
 "양양에서", "양양 북쪽 물치, 정암, 설악해변에서는 속초 대포항이 가깝습니다. 해물찜 대신 생선찜 한 냄비는 어떠세요.",
 "추천 메뉴", f"대표 메뉴 {GAORI}과 여러 생선을 담은 {MODEUM}이 있습니다. 숙소로 포장해 가셔도 됩니다.",
 [A("yangyang-saengseon-jjim","양양 생선찜"), A("yangyang-matjip","양양 맛집")], [SIZE, TOGO])
page("sokcho-hongeo-jjim", "속초 홍어찜", "메뉴", "gaori-jjim.jpg", "홍어찜 찾다가 만나는 속초 가오리찜.",
 "홍어찜과 가오리찜", f"홍어와 가오리는 생김새가 닮은 사촌 사이입니다. 이 집 {GAORI}은 삭히지 않아 톡 쏘는 냄새가 없고, 쫀득한 살과 오독한 연골을 즐길 수 있습니다.",
 "이렇게 드세요", f"살을 발라 양념과 콩나물을 함께 올려 드시고, 남은 양념에는 밥을 비벼 보세요. 자세한 차이는 {A('gaori-vs-hongeo','가오리 홍어 차이')}에 정리했습니다.",
 [A("sokcho-gaori-jjim","속초 가오리찜"), A("gaori-jjim-matjip","가오리찜 맛집")], [SIZE, WHERE])
dish_page("sokcho-myeongtae-jjim", "속초 명태찜", "메뉴", "kodari", "속초에서 명태찜을 찾는다면, 코다리찜.",
 "명태찜과 코다리찜", "코다리는 명태를 반쯤 말린 것입니다. 생물 명태보다 살이 단단하고 쫄깃해서 찜으로 하면 양념이 잘 배어듭니다.",
 [A("myeongtae-names","명태 이름 정리")])
dish_page("sokcho-daegu-jjim", "속초 대구찜", "메뉴", "daegu", "속초 대구찜, 볼살 가득 대구뽈찜으로.",
 "대구찜", "대구찜을 찾는다면 대구 머리의 볼살만 모아 찐 대구뽈찜을 드셔 보세요. 살이 쫀득하고 뜨끈해서 추운 날 특히 좋습니다.",
 [A("sokcho-daegu-ppol-jjim","속초 대구뽈찜")])

# ---------- 양양·고성·강원도·동해안 ----------
REG = {
 "yangyang": ("양양", "양양 북쪽 바닷가에서 올라오면 속초 대포항이 가장 먼저 닿는 항구입니다.", "yangyang-matjip", "양양 맛집"),
 "goseong": ("고성", "고성 바닷가에서 속초 시내를 지나 남쪽 끝까지 내려오면 대포항입니다.", "goseong-matjip", "고성 맛집"),
 "gangwon": ("강원도", "강원도 동해안을 여행한다면 속초 대포항에 들러 생선찜 한 냄비를 드셔 보세요.", "gangwon-matjip", "강원도 맛집"),
 "donghae": ("동해안", "동해안 바닷길을 따라 여행하다 속초에 닿으면, 대포항에서 한 끼 쉬어 가세요.", "donghaean-matjip", "동해안 맛집"),
}
for rk, dk in (("yangyang","daegu"),("yangyang","abai"),("goseong","kodari"),("goseong","daegu"),("goseong","abai"),
               ("gangwon","gaori"),("gangwon","kodari"),("gangwon","daegu"),("donghae","gaori"),("donghae","gui")):
    n, intro, ns, nk = REG[rk]; d = DI[dk][0]
    dish_page(f"{'gangwondo' if rk=='gangwon' else 'donghaean' if rk=='donghae' else rk}-{dk}", f"{n} {d}", "근처", dk,
              f"{n}에서 {d}{j(d,'을','를')} 찾는다면, 속초 대포항.", f"{n}에서", intro, [A(ns, nk)])

# ---------- 숙소 ----------
HO = {
 "ipark": ("아이파크 스위트 속초", "아이파크 스위트 속초는 속초해수욕장 쪽 바닷가 호텔입니다. 바다를 따라 남쪽으로 내려오면 대포항입니다.", "아이파크 스위트"),
 "chestertons": ("체스터톤스 속초", "체스터톤스 속초에 묵는다면 바다 쪽 남쪽 끝 대포항으로 나와 항구 식당에서 식사해 보세요.", "체스터톤스"),
}
for hk, (n, intro, short) in HO.items():
    page(f"{hk}-sokcho-matjip", f"{n} 근처 맛집", "근처", "hall3.jpg", f"{short}에 묵는다면, 식사는 대포항.",
     f"{n}에서", intro, "무엇을 먹을까", f"대표 메뉴 {GAORI}, 맵지 않은 {GUI}, 가볍게 {SQUID}가 있습니다. 숙소로 포장해 가셔도 됩니다.",
     [A("sokcho-hotel-matjip","속초 호텔 근처 맛집"), A("sokcho-beach-matjip","속초해수욕장 근처 맛집")], [WHERE, TOGO])
    for dk, w in (("modeum","생선찜"),("gui","생선구이")):
        dish_page(f"{hk}-{'jjim' if dk=='modeum' else 'gui'}", f"{n} {w}", "근처", dk, f"{short} 근처 {w}, 대포항에서.",
                  f"{n}에서", intro, [A(f"{hk}-sokcho-matjip", f"{n} 근처 맛집")])
page("sokcho-resort-matjip", "속초 리조트 근처 맛집", "근처", "hall3.jpg", "속초 리조트에 묵는다면, 한 끼는 대포항에서.",
 "리조트에서", "속초의 바닷가 리조트는 외옹치, 대포동, 설악산 쪽에 모여 있어 대포항으로 나오기 좋습니다. 리조트 안 식당이 붐빌 때 항구로 나와 보세요.",
 "무엇을 먹을까", f"가족이라면 {GAORI} 대(4인)에 아이 몫으로 {GUI}를 더하세요. 숙소에서 드시려면 전화로 포장 주문하시면 됩니다.",
 [A("sokcho-lotte-resort-matjip","속초 롯데리조트 근처 맛집"), A("sokcho-pension-matjip","속초 펜션 근처 맛집")], [TOGO, KIDS])
page("sokcho-residence-matjip", "속초 레지던스 근처 맛집", "근처", "jjim-table.jpg", "레지던스 숙소에서 먹을 저녁, 대포항에서 포장.",
 "레지던스에서", "속초에는 바닷가 레지던스 숙소가 많습니다. 객실에서 편하게 드시고 싶다면 대포항에서 찜을 포장해 가세요.",
 "포장", f"전 메뉴 포장됩니다. 미리 전화({TEL})로 주문하고 시간 맞춰 찾으러 오세요. 데우는 법은 {A('saengseon-jjim-reheat','생선찜 포장 데우는 법')}을 참고하세요.",
 [A("sokcho-takeout-matjip","속초 포장 맛집"), A("sokcho-stay-in-dinner","속초 숙소에서 먹는 저녁")], [TOGO, HOURS])
page("lotte-waterpark-matjip", "롯데리조트 속초 워터파크 근처 맛집", "근처", "hall3.jpg", "워터파크에서 놀고 난 뒤, 대포항에서 한 끼.",
 "워터파크 다음", "롯데리조트 속초 워터파크에서 물놀이를 하고 나면 배가 고픕니다. 리조트에서 남쪽으로 조금 내려오면 대포항입니다.",
 "아이랑 메뉴", f"맵지 않은 {GUI}와 {SQUID}가 아이 몫으로 좋습니다. 어른은 {GAORI}을 곁들이세요. 아기의자가 있습니다.",
 [A("sokcho-lotte-resort-matjip","속초 롯데리조트 근처 맛집"), A("sokcho-kids-matjip","속초 아이랑 맛집")], [KIDS, PARK])
page("yeongrangho-resort-matjip", "영랑호리조트 근처 맛집", "근처", "jjim-table.jpg", "영랑호리조트에서 바다 쪽 대포항으로.",
 "영랑호에서", "영랑호리조트는 속초 북쪽 영랑호 가에 있습니다. 시내를 지나 바다를 따라 남쪽 끝까지 오면 대포항입니다.",
 "무엇을 먹을까", f"대표 메뉴 {GAORI}과 여러 생선을 담은 {MODEUM}을 추천합니다. 숙소로 포장해 가셔도 됩니다.",
 [A("yeongnangho-matjip","영랑호 근처 맛집"), A("sokcho-resort-matjip","속초 리조트 근처 맛집")], [TOGO, WHERE])

# ---------- 근처 항구·명소 ----------
page("seorakhang-matjip", "설악항 맛집", "근처", "storefront.jpg", "설악항에서 회 말고 따뜻한 한 끼.",
 "설악항에서", "설악항은 속초와 맞닿은 양양 북쪽의 작은 항구입니다. 바다를 따라 속초 쪽으로 올라오면 대포항입니다.",
 "무엇을 먹을까", f"회 대신 따뜻한 찜을 원하면 {GAORI}, 맵지 않은 메뉴는 {GUI}입니다.",
 [A("mulchihang-matjip","물치항 근처 맛집"), A("daepohang-not-hoe","대포항 회 말고 먹을거")], [WHERE, SIZE])
page("hujinhang-matjip", "후진항 맛집", "근처", "storefront.jpg", "후진항 들른 길에, 대포항에서 식사.",
 "후진항에서", "후진항은 양양 북쪽 바닷가의 작은 항구입니다. 조용한 바다를 본 뒤 속초 쪽으로 올라와 대포항에서 식사하세요.",
 "무엇을 먹을까", f"대표 메뉴 {GAORI}, 여러 생선을 담은 {MODEUM}, 바삭한 {SQUID}가 있습니다.",
 [A("jeongam-matjip","정암해변 근처 맛집"), A("yangyang-matjip","양양 맛집")], [WHERE, TOGO])
page("daecheongbong-matjip", "대청봉 등산 후 맛집", "근처", "jjim-table.jpg", "대청봉 다녀온 날, 든든한 생선찜.",
 "대청봉 산행 뒤", "설악산 대청봉 산행은 하루를 꼬박 쓰는 긴 길입니다. 내려오면 바다 쪽 대포항으로 나와 뜨끈한 찜으로 기운을 채우세요.",
 "추천 메뉴", f"든든하게는 {GAORI}이나 {MODEUM}, 뜨끈한 국물이 당기면 {DAEGU}입니다. 소주, 맥주, 막걸리도 있습니다.",
 [A("ulsanbawi-matjip","울산바위 등산 후 맛집"), A("seoraksan-matjip","설악산 근처 맛집")], [SIZE, HOURS])
page("towangseong-matjip", "토왕성폭포 근처 맛집", "근처", "gui.jpg", "토왕성폭포 보고 내려와, 대포항에서 한 끼.",
 "토왕성폭포에서", "토왕성폭포는 설악산 소공원에서 걸어 오르는 전망대 길로 볼 수 있습니다. 내려와 바다 쪽으로 나오면 대포항입니다.",
 "추천 메뉴", f"가볍게는 {GUI}나 {SQUID}, 든든하게는 {GAORI}을 추천합니다.",
 [A("seorak-sogongwon-matjip","설악산 소공원 근처 맛집"), A("seoraksan-matjip","설악산 근처 맛집")], [WHERE, KIDS])

# ---------- 대포항 포장 ----------
for dk, slug in (("kodari","daepohang-kodari-takeout"),("daegu","daepohang-daegu-takeout")):
    d = DI[dk][0]
    dish_page(slug, f"대포항 {d} 포장", "대포항", dk, f"대포항에서 {d} 포장해 숙소로.",
              "포장", f"전 메뉴 포장됩니다. 미리 전화({TEL})로 주문하고 시간 맞춰 찾으러 오세요. 데우는 법은 {A('saengseon-jjim-reheat','생선찜 포장 데우는 법')}을 참고하세요.",
              [A("daepohang-takeout","대포항 포장")], [TOGO, SIZE])

# ---------- 속초 메뉴 추천·끼니 ----------
for dk in ("kodari","daegu","abai"):
    d = DI[dk][0]
    dish_page(f"sokcho-{dk}-recommend", f"속초 {d} 추천", "메뉴", dk, f"속초에서 {d} 먹을 곳, 대포항.",
              "왜 여기인가", "대포항생선찜본점은 생선찜과 생선구이를 전문으로 하는 대포항 안쪽 상가 1층 식당입니다. 찜 메뉴는 소·중·대로 인원에 맞춰 고를 수 있습니다.",
              [A("sokcho-matjip-recommend","속초 맛집 추천")])
for dk, meal in (("gaori","점심"),("gui","저녁"),("daegu","저녁"),("modeum","저녁"),("abai","점심")):
    d = DI[dk][0]; img, text = MEAL[meal]
    dish_page(f"sokcho-{dk}-{'lunch' if meal=='점심' else 'dinner'}", f"속초 {d} {meal}", "메뉴", dk, f"속초 {meal}, {d} 한 끼.",
              f"{meal}에", text, [A("sokcho-lunch-matjip" if meal=="점심" else "sokcho-dinner-matjip", f"속초 {meal} 맛집")],
              [WHERE, PARK] if meal=="점심" else [SIZE, HOURS])
dish_page("sokcho-kids-gui", "속초 아이랑 생선구이", "메뉴", "gui", "아이와 함께라면 맵지 않은 생선구이.",
 "아이랑", "아이와 속초에 왔다면 맵지 않은 생선구이가 편합니다. 아기의자가 있고, 가시는 발라서 덜어 주세요.",
 [A("sokcho-kids-matjip","속초 아이랑 맛집")], [KIDS, WHERE])
dish_page("sokcho-family-gui", "속초 가족 생선구이", "메뉴", "gui", "가족이 함께 먹는 생선구이 한 판.",
 "가족이라면", f"생선구이는 맵지 않아 온 가족이 함께 드시기 좋습니다. 어른 몫으로 {GAORI}을 함께 시키는 가족이 많습니다.",
 [A("sokcho-family-dining","속초 가족 외식")], [KIDS, SIZE])
dish_page("sokcho-gui-2in", "속초 생선구이 2인", "메뉴", "gui", "둘이서 먹는 속초 생선구이.",
 "둘이라면", f"둘이라면 {GUI}에 {SQUID}를 곁들이거나, {GAORI} 소(2인)와 함께 드셔 보세요.",
 [A("sokcho-jjim-2in","속초 2인 생선찜")], [WHERE, TOGO])

# ---------- 속초 동네 생선구이 ----------
DONG = {"gyodong":"교동","nohakdong":"노학동","cheonghodong":"청호동","dongmyeongdong":"동명동","yeongnangdong":"영랑동"}
for dk_, n in DONG.items():
    dish_page(f"{dk_}-gui", f"속초 {n} 생선구이", "근처", "gui", f"속초 {n}에서 생선구이 먹으러, 대포항.",
              f"{n}에서", f"속초 {n}에서 바다를 따라 남쪽 끝까지 오면 대포항입니다. 항구 안쪽 상가 1층에서 생선구이를 드실 수 있습니다.",
              [A("sokcho-saengseon-gui","속초 생선구이")])

assert len(P) == 50, len(P)
