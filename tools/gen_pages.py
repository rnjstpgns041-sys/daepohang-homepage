import json, os, sys

ROOT = sys.argv[1]
BASE = "https://daepohang-fish.pages.dev"
INSTA = "https://www.instagram.com/_crab.ggo"
NAVER_TAG = '<meta name="naver-site-verification" content="8dd3b14817dc29fab7d6907ab8e6febcf467bf17">'
ADDR = "강원특별자치도 속초시 대포항길 10"
PHONE = "0507-1364-4060"

CSS = """:root{
  --bg:#f4f6f7;--surface:#ffffff;--ink:#14233a;--muted:#5a6676;--line:#d9dee4;--chili:#c2361f;--sesame:#e9b949;
  --display:"Black Han Sans","Noto Sans KR","Apple SD Gothic Neo",sans-serif;
  --body:"Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
}
@media (prefers-color-scheme:dark){:root{--bg:#0e1828;--surface:#16233a;--ink:#eef1f5;--muted:#a3adbb;--line:#2a3a54;--chili:#ec5a3f;--sesame:#f2c75c;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.75;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
a{color:inherit}
.wrap{max-width:820px;margin-inline:auto;padding-inline:20px}
h1,h2{font-family:var(--display);font-weight:400;line-height:1.2;text-wrap:balance;margin:0}
.bar{position:sticky;top:0;z-index:10;background:var(--bg);border-bottom:1px solid var(--line)}
.bar .wrap{max-width:1120px;display:flex;align-items:center;justify-content:space-between;gap:16px;height:56px}
.logo{font-family:var(--display);font-size:1.2rem;text-decoration:none;white-space:nowrap}
.logo span{color:var(--chili)}
.bar a.home{font-size:.9rem;color:var(--muted);text-decoration:none;white-space:nowrap}
.crumb{font-size:.85rem;color:var(--muted);padding-top:28px}
.crumb a{color:var(--muted)}
.head{padding-block:12px 24px}
.eyebrow{font-size:.8rem;letter-spacing:.12em;color:var(--chili);font-weight:700;margin:0 0 .4rem}
h1{font-size:clamp(2rem,6vw,3.2rem)}
.lede{font-size:1.1rem;color:var(--muted);margin:14px 0 0}
.photo{margin:0 0 8px;border-radius:6px;overflow:hidden}
.photo img{width:100%;aspect-ratio:4/3;object-fit:cover}
.photo figcaption{font-size:.85rem;color:var(--muted);padding-top:6px}
article h2{font-size:clamp(1.4rem,3.6vw,1.8rem);margin-top:44px}
article p{margin:14px 0 0}
article ul{padding-left:1.2em;margin:14px 0 0}
article li{margin:4px 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px}
.two figure{margin:0;border-radius:6px;overflow:hidden}
.two img{width:100%;aspect-ratio:1/1;object-fit:cover}
@media (max-width:520px){.two{grid-template-columns:1fr}}
.info{margin-top:44px;background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:20px}
.info h2{margin:0 0 10px;font-size:1.4rem}
.info dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:6px 16px}
.info dt{font-weight:700;color:var(--chili);font-size:.9rem}
.info dd{margin:0;min-width:0}
.faq details{border-bottom:1px solid var(--line);padding:12px 0}
.faq summary{font-weight:700;cursor:pointer}
.faq p{color:var(--muted)}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.btn{display:inline-flex;padding:10px 18px;border-radius:999px;font-weight:700;text-decoration:none;font-size:.95rem}
.btn-primary{background:var(--chili);color:#fff}
.btn-line{border:1.5px solid var(--line);background:var(--surface)}
.btn:focus-visible{outline:3px solid var(--sesame);outline-offset:3px}
.more{margin-top:48px;padding-block:28px;border-top:2px solid var(--ink)}
.more h2{font-size:1.3rem}
.more ul{list-style:none;padding:0;margin:12px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(220px,100%),1fr));gap:8px}
.more a{display:block;padding:12px 14px;background:var(--surface);border:1px solid var(--line);border-radius:6px;text-decoration:none;font-weight:500}
.more a:hover{border-color:var(--chili)}
.glist{list-style:none;padding:0;margin:14px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));gap:10px}
.glist a{display:flex;flex-direction:column;gap:2px;padding:14px 16px;background:var(--surface);border:1px solid var(--line);border-radius:6px;text-decoration:none;min-width:0;height:100%}
.glist a:hover,.glist a:focus-visible{border-color:var(--chili)}
.glist b{font-size:1.02rem}
.glist span{color:var(--muted);font-size:.88rem;line-height:1.5}
.copybtn{margin-left:6px;padding:2px 10px;border:1px solid var(--line);border-radius:999px;background:var(--bg);color:var(--ink);font:inherit;font-size:.82rem;cursor:pointer;vertical-align:1px}
.copybtn:hover{border-color:var(--chili)}
.copybtn:focus-visible{outline:3px solid var(--sesame);outline-offset:2px}
.toast{position:fixed;left:50%;bottom:calc(24px + env(safe-area-inset-bottom,0px));transform:translate(-50%,20px);background:var(--ink);color:var(--bg);padding:12px 20px;border-radius:999px;font-weight:700;font-size:.95rem;opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;z-index:50;max-width:calc(100% - 32px);width:max-content;text-align:center}
.toast.show{opacity:1;transform:translate(-50%,0)}
footer{padding-block:28px;color:var(--muted);font-size:.85rem;border-top:1px solid var(--line)}
"""

PAGES = [
 dict(slug="sokcho-gaori-jjim", kw="속초 가오리찜", short="속초 가오리찜",
  title="속초 가오리찜 맛집 | 대포항생선찜본점",
  desc="속초 대포항 앞 가오리찜 전문 생선찜집. 매콤한 양념에 쫄깃하게 쪄낸 가오리찜을 소·중·대로. 속초시 대포항길 10, 0507-1364-4060.",
  h1="속초 가오리찜,<br>대포항생선찜본점",
  lede="양념은 진하게, 살은 결대로. 대포항 앞에서 가오리찜 한 판 드시고 가세요.",
  img="gaori-jjim.jpg", alt="양념을 올려 쪄낸 속초 가오리찜",
  body="""
<h2>가오리찜이 어떤 음식인가요</h2>
<p>가오리찜은 가오리를 큼직하게 손질해 고춧가루 양념을 올리고 대파와 함께 쪄낸 음식입니다. 살이 결을 따라 길게 찢어지고, 뼈가 물렁한 연골이라 씹는 맛이 쫄깃합니다. 속초와 강원 동해안에서 오래전부터 즐겨 먹던 생선 요리입니다.</p>
<p>대포항생선찜본점의 가오리찜은 깨를 듬뿍 뿌린 매콤달콤한 양념이 특징입니다. 양념이 살 사이사이 배어 있어 밥 위에 올려 비벼 먹기 좋습니다.</p>
<div class="two">
  <figure><img src="/img/jjim-closeup.jpg" alt="결대로 찢어지는 가오리찜 속살" loading="lazy"></figure>
  <figure><img src="/img/jjim-table.jpg" alt="가오리찜과 기본 반찬 한 상" loading="lazy"></figure>
</div>
<h2>몇 인분을 시켜야 할까요</h2>
<ul>
  <li><b>소</b>: 2인이 식사하기 좋은 양</li>
  <li><b>중</b>: 3인 기준</li>
  <li><b>대</b>: 4인 기준</li>
</ul>
<p>가오리찜 하나에 누룽지 오징어순대나 모듬생선구이를 곁들이면 여럿이 나눠 먹기 좋습니다. 가격은 시세에 따라 달라질 수 있어 매장 메뉴판이나 전화로 확인해 주세요.</p>
""",
  faq=[("가오리찜은 많이 맵나요?","고춧가루 양념이라 칼칼한 편이지만 단맛이 함께 있어 맵기에 약한 분도 대부분 잘 드십니다."),
       ("포장도 되나요?","가오리찜을 포함해 모든 메뉴를 포장해 드립니다. 숙소에서 드실 때 미리 전화 주시면 편합니다.")]),

 dict(slug="daepohang-matjip", kw="대포항 맛집", short="대포항 맛집",
  title="대포항 맛집 생선찜·생선구이 | 대포항생선찜본점",
  desc="속초 대포항 맛집 대포항생선찜본점. 가오리찜, 생선모듬찜, 모듬생선구이, 누룽지 오징어순대. 반려동물 동반, 아기의자, 전 메뉴 포장. 대포항길 10.",
  h1="대포항 맛집,<br>생선찜 한 상",
  lede="대포항 구경하고 배고플 때, 걸어서 바로 오는 생선찜집입니다.",
  img="storefront.jpg", alt="밤에 불이 켜진 대포항생선찜본점 간판",
  body="""
<h2>대포항에서 무엇을 먹을까</h2>
<p>대포항은 활어회와 대게로 유명하지만, 회가 부담스럽거나 따뜻한 밥 한 끼를 원할 때는 생선찜과 생선구이가 좋은 선택입니다. 대포항생선찜본점은 대포항 안쪽 상가 1층, 노란색과 분홍색 네온 간판이 있는 곳입니다.</p>
<h2>이 집에서 드셔볼 메뉴</h2>
<ul>
  <li><a href="/sokcho-gaori-jjim/">가오리찜</a>: 손님들이 가장 많이 찾는 대표 메뉴</li>
  <li>생선모듬찜: 여러 생선을 무와 함께 쪄낸 찜</li>
  <li>대구뽈찜 · 코다리찜</li>
  <li><a href="/sokcho-saengseon-gui/">모듬생선구이</a>: 철판에 담겨 나오는 구이</li>
  <li><a href="/sokcho-nurungji-squid-sundae/">누룽지 오징어순대</a> · 속초 아바이순대</li>
</ul>
<div class="two">
  <figure><img src="/img/hall3.jpg" alt="칸막이가 있는 넓은 홀" loading="lazy"></figure>
  <figure><img src="/img/ball-wall.jpg" alt="선수 사인볼이 진열된 벽" loading="lazy"></figure>
</div>
<h2>가족, 반려견과 함께 오기 좋은 곳</h2>
<p>홀이 넓고 테이블 사이에 칸막이가 있어 가족 식사나 모임에 편합니다. 아기 의자가 여러 개 있고, 반려동물 동반도 가능합니다. 벽 한 면에는 선수 사인볼과 농구공이 진열되어 있고, 삼성썬더스 농구단이 다녀간 현수막도 걸려 있어 구경하는 재미가 있습니다.</p>
""",
  faq=[("대포항 주차는 어디에 하나요?","대포항 공영주차장에 주차하시고 걸어오시면 됩니다."),
       ("쉬는 날이 있나요?","매주 수요일이 정기휴무입니다. 영업시간은 10:00부터 21:00까지입니다.")]),

 dict(slug="sokcho-matjip", kw="속초 맛집", short="속초 맛집",
  title="속초 맛집 대포항 생선찜 | 대포항생선찜본점",
  desc="속초 여행 중 들르기 좋은 속초 맛집. 대포항 앞 생선찜·생선구이·오징어순대. 반려동물 동반, 가족 식사, 전 메뉴 포장. 0507-1364-4060.",
  h1="속초 맛집 찾을 때,<br>대포항 생선찜",
  lede="속초에서 바다 음식을 맛보고 싶은데 회는 망설여질 때 좋은 한 끼입니다.",
  img="jjim-table.jpg", alt="생선찜과 반찬이 차려진 한 상",
  body="""
<h2>속초에 오면 먹는 음식</h2>
<p>속초를 대표하는 음식으로는 생선찜과 생선구이, 그리고 오징어순대와 아바이순대가 꼽힙니다. 대포항생선찜본점에서는 이 메뉴를 한 곳에서 드실 수 있어, 여행 중 한 끼로 속초 음식을 두루 맛보기 좋습니다.</p>
<h2>여행 동선에 넣기 좋은 위치</h2>
<p>가게는 속초 대포항 바로 앞에 있습니다. 대포항 수산시장과 외옹치 바다향기로 산책길이 가깝고, 설악산이나 속초 시내로 오가는 길에 들르기도 편합니다. 오전 10시에 문을 열어 늦은 아침 겸 점심으로 드셔도 좋습니다.</p>
<div class="two">
  <figure><img src="/img/gui.jpg" alt="모듬생선구이" loading="lazy"></figure>
  <figure><img src="/img/abai-sundae.jpg" alt="속초 아바이순대" loading="lazy"></figure>
</div>
<h2>이런 분께 추천해요</h2>
<ul>
  <li>아이와 함께 오는 가족 여행: 아기 의자 여러 개 준비</li>
  <li>반려견과 함께하는 여행: 반려동물 동반 가능</li>
  <li>숙소에서 먹고 싶은 분: 모든 메뉴 포장</li>
  <li>단체 모임: 칸막이로 나뉜 넓은 홀</li>
</ul>
""",
  faq=[("몇 시까지 하나요?","10:00부터 21:00까지 영업하고, 매주 수요일은 쉽니다."),
       ("예약이 되나요?","전화(0507-1364-4060)로 문의해 주세요.")]),

 dict(slug="sokcho-saengseon-gui", kw="속초 생선구이", short="속초 생선구이",
  title="속초 생선구이 대포항 모듬생선구이 | 대포항생선찜본점",
  desc="속초 대포항 모듬생선구이. 노릇하게 구운 생선을 뜨거운 철판에 담아 냅니다. 생선찜과 함께 즐기는 대포항생선찜본점. 속초시 대포항길 10.",
  h1="속초 생선구이,<br>철판째 나오는 모듬구이",
  lede="껍질은 바삭하게, 속살은 촉촉하게 구워 뜨거운 철판에 담아 드립니다.",
  img="gui.jpg", alt="철판 위에 담긴 속초 모듬생선구이",
  body="""
<h2>모듬생선구이</h2>
<p>대포항생선찜본점의 모듬생선구이는 여러 종류의 생선을 노릇하게 구워 무쇠 철판에 담아 냅니다. 철판이 뜨거워 마지막 한 점까지 따뜻하게 드실 수 있습니다. 생선 구성은 그날 들어온 생선에 따라 달라질 수 있습니다.</p>
<h2>구이와 찜을 같이 드세요</h2>
<p>생선구이만으로도 한 끼가 되지만, 여럿이 오시면 매콤한 <a href="/sokcho-gaori-jjim/">가오리찜</a>이나 생선모듬찜을 함께 시켜 담백한 맛과 매운맛을 번갈아 즐기는 손님이 많습니다.</p>
<div class="two">
  <figure><img src="/img/jjim-table.jpg" alt="생선찜 한 상" loading="lazy"></figure>
  <figure><img src="/img/squid-sundae.jpg" alt="누룽지 오징어순대" loading="lazy"></figure>
</div>
<h2>기본 반찬</h2>
<p>김치, 콩나물무침, 나물, 콘샐러드, 양배추 샐러드 같은 기본 반찬이 함께 나옵니다.</p>
""",
  faq=[("생선구이 포장도 되나요?","네, 모든 메뉴를 포장해 드립니다."),
       ("아이도 먹기 좋나요?","맵지 않은 메뉴라 아이와 함께 드시기 좋습니다. 아기 의자도 있습니다.")]),

 dict(slug="sokcho-nurungji-squid-sundae", kw="속초 누룽지 오징어순대", short="속초 누룽지 오징어순대",
  title="속초 누룽지 오징어순대 17,000원 | 대포항생선찜본점",
  desc="겉은 누룽지처럼 바삭, 속은 촉촉한 속초 누룽지 오징어순대 17,000원. 대포항생선찜본점, 속초시 대포항길 10, 0507-1364-4060.",
  h1="속초 누룽지<br>오징어순대",
  lede="오징어 속을 꽉 채우고 겉을 누룽지처럼 바삭하게 지져 냅니다. 17,000원.",
  img="squid-sundae.jpg", alt="바삭하게 지진 속초 누룽지 오징어순대",
  body="""
<h2>누룽지 오징어순대가 뭔가요</h2>
<p>오징어순대는 오징어 몸통에 찹쌀, 채소 등을 채워 쪄낸 속초의 향토 음식입니다. 누룽지 오징어순대는 이것을 썰어 팬에 지져, 단면이 누룽지처럼 노릇하고 바삭하게 만든 것입니다. 바삭한 겉과 촉촉한 속, 쫄깃한 오징어를 한 입에 즐길 수 있습니다.</p>
<div class="two">
  <figure><img src="/img/squid-sundae.jpg" alt="누룽지 오징어순대 한 접시" loading="lazy"></figure>
  <figure><img src="/img/abai-sundae.jpg" alt="고추 장아찌를 곁들인 아바이순대" loading="lazy"></figure>
</div>
<h2>함께 먹기 좋은 메뉴</h2>
<p>고추 장아찌를 곁들여 드시면 느끼함 없이 깔끔합니다. 속초의 또 다른 순대인 <b>아바이순대</b>도 함께 준비되어 있어 두 가지 순대를 비교해 드셔보셔도 좋습니다. 식사로는 <a href="/sokcho-gaori-jjim/">가오리찜</a>과 잘 어울립니다.</p>
<h2>가격</h2>
<p>누룽지 오징어순대 <b>17,000원</b>. 가격은 바뀔 수 있으니 매장에서 한 번 더 확인해 주세요.</p>
""",
  faq=[("포장해서 숙소에서 먹어도 되나요?","네, 포장됩니다. 식으면 팬에 살짝 데우시면 다시 바삭해집니다."),
       ("오징어순대만 따로 시킬 수 있나요?","네, 단품으로 주문하실 수 있습니다.")]),
]

def jsonld(p):
    data = {
      "@context":"https://schema.org","@type":"Restaurant","name":"대포항생선찜본점",
      "url":BASE+"/","telephone":PHONE,"sameAs":[INSTA],"image":BASE+"/img/"+p["img"],
      "servesCuisine":["생선찜","생선구이","오징어순대"],
      "address":{"@type":"PostalAddress","streetAddress":"대포항길 10","addressLocality":"속초시","addressRegion":"강원특별자치도","addressCountry":"KR"},
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Thursday","Friday","Saturday","Sunday"],"opens":"10:00","closes":"21:00"}]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    return ('<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script>\n'
            '<script type="application/ld+json">'+json.dumps(faq,ensure_ascii=False)+'</script>')

def page(p):
    url = f"{BASE}/{p['slug']}/"
    same=[o for o in PAGES if o is not p and o.get("cat")==p.get("cat")]
    rest=[o for o in PAGES[:5] if o is not p and o not in same]
    others = "\n".join(f'    <li><a href="/{o["slug"]}/">{o["short"]}</a></li>' for o in (same+rest)[:8])
    others += '\n    <li><a href="/guide/">전체 안내 보기</a></li>'
    faq = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in p["faq"])
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
{NAVER_TAG}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="keywords" content="{p['kw']}, 대포항생선찜본점, 속초, 대포항">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/{p['img']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;500;700&display=swap">
<link rel="stylesheet" href="/css/sub.css">
{jsonld(p)}
</head>
<body>
<header class="bar"><div class="wrap">
  <a class="logo" href="/">대포항<span>생선찜</span>본점</a>
  <a class="home" href="/#visit">오시는 길</a>
</div></header>
<main class="wrap">
  <nav class="crumb" aria-label="현재 위치"><a href="/">홈</a> › {p['short']}</nav>
  <div class="head">
    <p class="eyebrow">{p['kw']}</p>
    <h1>{p['h1']}</h1>
    <p class="lede">{p['lede']}</p>
  </div>
  <figure class="photo"><img src="/img/{p['img']}" alt="{p['alt']}"><figcaption>대포항생선찜본점 · {p['kw']}</figcaption></figure>
  <article>
{p['body']}
  <section class="info" aria-label="매장 정보">
    <h2>대포항생선찜본점</h2>
    <dl>
      <dt>주소</dt><dd><span class="cv">{ADDR}</span> <button class="copybtn" type="button" data-copy="{ADDR}" data-label="주소">복사</button></dd>
      <dt>영업</dt><dd>10:00 ~ 21:00 · 매주 수요일 휴무</dd>
      <dt>전화</dt><dd><span class="cv">{PHONE}</span> <button class="copybtn" type="button" data-copy="{PHONE}" data-label="전화번호">복사</button></dd>
      <dt>주차</dt><dd>대포항 공영주차장</dd>
    </dl>
    <div class="cta">
      <a class="btn btn-primary" href="https://map.naver.com/p/search/%EB%8C%80%ED%8F%AC%ED%95%AD%EC%83%9D%EC%84%A0%EC%B0%9C%EB%B3%B8%EC%A0%90" target="_blank" rel="noopener">네이버 지도</a>
      <a class="btn btn-line" href="/#menu">전체 메뉴</a>
    </div>
  </section>
  <h2>자주 묻는 질문</h2>
  <div class="faq">
{faq}
  </div>
  </article>
  <nav class="more" aria-label="더 보기">
    <h2>대포항생선찜본점 더 보기</h2>
    <ul>
{others}
    </ul>
  </nav>
</main>
<footer><div class="wrap">대포항생선찜본점 · {ADDR} · {PHONE} · <a href="{INSTA}" target="_blank" rel="noopener">인스타그램</a></div></footer>
<script src="/js/copy.js" defer></script>
</body>
</html>
"""

# ---- extra pages ----
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages2 import P as EXTRA
for p in PAGES: p.setdefault("cat","대표")
for e in EXTRA:
    body = "".join(f"\n<h2>{h}</h2>\n{html}" for h,html in e["sections"])
    kw = e["kw"]
    PAGES.append(dict(slug=e["slug"], kw=kw, short=kw, cat=e["cat"],
        title=f"{kw} | 대포항생선찜본점",
        desc=e.get("desc") or f"{kw} 찾는다면 속초 대포항생선찜본점. {e['lede']} 속초시 대포항길 10, 0507-1364-4060.",
        h1=f"{kw}", lede=e["lede"], img=e["img"], alt=f"{kw} 대포항생선찜본점", body=body, faq=e["faq"]))

os.makedirs(os.path.join(ROOT,"css"),exist_ok=True)
open(os.path.join(ROOT,"css","sub.css"),"w",encoding="utf-8").write(CSS)
for p in PAGES:
    d = os.path.join(ROOT,p["slug"]); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(page(p))


cats=[]
for p in PAGES:
    if p["cat"] not in cats: cats.append(p["cat"])
glist="".join(f'<h2>{c}</h2><ul class="glist">'+"".join(f'<li><a href="/{p["slug"]}/"><b>{p["short"]}</b><span>{p["lede"]}</span></a></li>' for p in PAGES if p["cat"]==c)+"</ul>" for c in cats)
gp=dict(slug="guide",kw="속초 대포항 맛집 안내",short="전체 안내",title="속초 대포항 맛집 안내 모음 | 대포항생선찜본점",
  desc="속초 생선찜, 생선구이, 오징어순대부터 대포항 여행 코스, 애견동반, 아이랑 식사까지. 대포항생선찜본점 안내 모음.",
  h1="속초 대포항<br>맛집 안내 모음",lede="메뉴, 대포항 주변, 상황별 식사, 속초 여행 코스를 한곳에 모았습니다.",
  img="hall3.jpg",alt="대포항생선찜본점 홀",body=glist,faq=[("가게 위치는?","속초시 대포항길 10입니다."),("휴무일은?","매주 수요일입니다.")],cat="안내")
os.makedirs(os.path.join(ROOT,"guide"),exist_ok=True)
html=page(gp).replace('<nav class="more"','<nav hidden class="more"')
open(os.path.join(ROOT,"guide","index.html"),"w",encoding="utf-8").write(html)
urls = [BASE+"/", BASE+"/guide/"] + [f"{BASE}/{p['slug']}/" for p in PAGES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{u}</loc><lastmod>2026-10-06</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write(sm)

# home: add keyword links section + restaurant JSON-LD
hp = os.path.join(ROOT,"index.html"); s = open(hp,encoding="utf-8").read()
if 'id="guide"' not in s or True:
    import re
    s=re.sub(r'  <section id="guide".*?</section>\n','',s,flags=re.S)
    s=re.sub(r'\.guide\{.*?\.guide span\{[^}]*\}\n','',s,flags=re.S)
    s=re.sub(r'<script type="application/ld\+json">.*?</script>\n','',s,flags=re.S)
    s=s.replace('<meta name="description" content="속초 대포항 맛집 대포항생선찜본점. 생선찜·생선구이 전문점.','<meta name="description" content="속초 대포항 생선찜·생선구이 전문점.')
    links = "\n".join(f'        <a href="/{p["slug"]}/"><b>{p["short"]}</b><span>{p["lede"]}</span></a>' for p in PAGES[:5]) + '\n        <a href="/guide/"><b>전체 안내 보기</b><span>메뉴, 대포항 주변, 상황별 식사, 여행 코스 48가지</span></a>'
    block = f"""  <section id="guide" class="alt">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">더 알아보기</p><h2>메뉴와 여행 안내</h2></div></div>
      <div class="guide">
{links}
      </div>
    </div>
  </section>
</main>"""
    s = s.replace("</main>", block, 1)
    css = """.guide{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));gap:12px}
.guide a{display:flex;flex-direction:column;gap:4px;padding:16px 18px;background:var(--bg);border:1px solid var(--line);border-radius:6px;text-decoration:none;min-width:0}
.guide a:hover,.guide a:focus-visible{border-color:var(--chili)}
.guide b{font-family:var(--display);font-weight:400;font-size:1.25rem}
.guide span{color:var(--muted);font-size:.92rem}
</style>"""
    s = s.replace("</style>", css, 1)
    s = s.replace("</head>", jsonld(PAGES[1]).split("\n")[0].replace(PAGES[1]["img"],"gaori-jjim.jpg")+"\n</head>",1)
    s = s.replace('<meta name="description" content="속초 대포항 생선찜·생선구이 전문점.','<meta name="description" content="속초 대포항 맛집 대포항생선찜본점. 생선찜·생선구이 전문점.',1)
    open(hp,"w",encoding="utf-8").write(s)
print("ok", urls)
