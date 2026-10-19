// 인원별 추천 한 상 + 포장 주문 메모. #order-helper 자리에 그립니다.
(function () {
  var box = document.getElementById("order-helper");
  if (!box) return;
  var TEL = "050713644060", TEL_TXT = "0507-1364-4060";
  var JJIM = ["가오리찜", "생선모듬찜", "대구뽈찜", "코다리찜"];
  var PEOPLE = ["2명", "3명", "4명", "5명", "6명", "7명 이상"];
  // 인원별 추천 예시 (찜 소 2인 · 중 3인 · 대 4인 기준)
  function plan(n, j) {
    return [
      [j + " 소", "누룽지 오징어순대"],
      [j + " 중", "모듬생선구이"],
      [j + " 대", "모듬생선구이"],
      [j + " 대", "모듬생선구이", "누룽지 오징어순대"],
      [j + " 대", "다른 찜 소 (한 가지 더 맛보기)", "모듬생선구이"],
      [j + " 대 2개", "모듬생선구이", "누룽지 오징어순대"]
    ][n];
  }
  var st = { n: 0, j: 0, take: false, time: "" };

  var css = document.createElement("style");
  css.textContent =
    ".oh{max-width:640px;margin:0 auto;background:var(--paper2,#e9dcc3);border:1px solid var(--line,#c9b996);padding:26px 20px;text-align:left}" +
    ".oh h2{margin:0 0 4px;text-align:center}.oh .oh-sub{margin:0 0 18px;text-align:center;color:var(--muted,#5d5246);font-size:.95rem}" +
    ".oh .oh-q{font-weight:700;margin:14px 0 8px;font-size:.98rem}" +
    ".oh .oh-chips{display:flex;flex-wrap:wrap;gap:8px}" +
    ".oh .oh-chips button{font:inherit;font-size:.95rem;padding:9px 14px;border:1px solid var(--ink,#221d19);background:transparent;color:var(--ink,#221d19);cursor:pointer;border-radius:0}" +
    ".oh .oh-chips button[aria-pressed=true]{background:var(--ink,#221d19);color:#fff}" +
    ".oh input[type=time]{font:inherit;padding:8px 10px;border:1px solid var(--ink,#221d19);background:#fff;color:var(--ink,#221d19)}" +
    ".oh .oh-res{margin-top:20px;background:#fffaf0;border:1px dashed var(--chili,#a3302a);padding:18px}" +
    ".oh .oh-res b.t{display:block;color:var(--chili,#a3302a);margin-bottom:6px}" +
    ".oh .oh-res ul{margin:0 0 10px;padding-left:20px}.oh .oh-res li{margin:2px 0}" +
    ".oh .oh-memo{font-size:.92rem;color:var(--muted,#5d5246);background:#fff;border:1px solid var(--line,#c9b996);padding:10px 12px;margin:10px 0 0;white-space:pre-line}" +
    ".oh .oh-btns{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}" +
    ".oh .oh-btns a,.oh .oh-btns button{flex:1;min-width:140px;text-align:center;font:inherit;font-weight:700;padding:13px 10px;text-decoration:none;cursor:pointer;border-radius:0}" +
    ".oh .oh-call{background:var(--chili,#a3302a);color:#fff;border:1px solid var(--chili,#a3302a)}" +
    ".oh .oh-copy{background:transparent;color:var(--ink,#221d19);border:1px solid var(--ink,#221d19)}" +
    ".oh .oh-note{font-size:.82rem;color:var(--muted,#5d5246);margin:10px 0 0}";
  document.head.appendChild(css);

  function chips(list, key, cur) {
    return '<div class="oh-chips">' + list.map(function (t, i) {
      return '<button type="button" data-k="' + key + '" data-v="' + i + '" aria-pressed="' + (i === cur) + '">' + t + "</button>";
    }).join("") + "</div>";
  }
  function memo() {
    var items = plan(st.n, JJIM[st.j]);
    var head = st.take ? "포장 주문할게요." : "자리 문의드려요.";
    var when = st.take ? (st.time ? " " + st.time + " 픽업" : " 픽업 시간은 통화로 말씀드릴게요") : "";
    return head + "\n" + PEOPLE[st.n] + " · " + items.join(", ") + "\n" + (st.take ? "받는 시간:" + when : "지금 자리 있을까요?");
  }
  function draw() {
    var items = plan(st.n, JJIM[st.j]);
    box.innerHTML =
      '<div class="oh"><h2>몇 분이 오세요? 한 상 골라드릴게요</h2>' +
      '<p class="oh-sub">인원과 찜 종류만 고르면 추천 메뉴와 주문 메모가 나와요</p>' +
      '<p class="oh-q">인원</p>' + chips(PEOPLE, "n", st.n) +
      '<p class="oh-q">찜 종류</p>' + chips(JJIM, "j", st.j) +
      '<p class="oh-q">드시는 방법</p>' + chips(["가게에서 식사", "포장해 가기"], "take", st.take ? 1 : 0) +
      (st.take ? '<p class="oh-q">받으실 시간</p><input type="time" id="oh-time" value="' + st.time + '">' : "") +
      '<div class="oh-res"><b class="t">' + PEOPLE[st.n] + " 추천 한 상</b><ul>" +
      items.map(function (t) { return "<li>" + t + "</li>"; }).join("") + "</ul>" +
      '<div class="oh-memo" id="oh-memo">' + memo() + "</div>" +
      '<div class="oh-btns"><a class="oh-call" href="tel:' + TEL + '">' + (st.take ? "전화로 포장 주문" : "전화로 자리 문의") + "</a>" +
      '<button type="button" class="oh-copy" id="oh-copy">주문 메모 복사</button></div>' +
      '<p class="oh-note">추천은 예시예요. 정확한 양과 가격은 전화로 물어봐 주세요. ' + TEL_TXT + "</p></div></div>";
  }
  box.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b) return;
    if (b.id === "oh-copy") {
      var t = memo();
      var done = function () { b.textContent = "복사됐어요"; setTimeout(function () { b.textContent = "주문 메모 복사"; }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(done, function () {});
      return;
    }
    var k = b.getAttribute("data-k"); if (!k) return;
    var v = +b.getAttribute("data-v");
    if (k === "take") st.take = v === 1; else st[k] = v;
    draw();
    if (window.gtag) window.gtag("event", "order_helper", { step: k, value: b.textContent });
  });
  box.addEventListener("change", function (e) {
    if (e.target.id === "oh-time") { st.time = e.target.value; document.getElementById("oh-memo").textContent = memo(); }
  });
  draw();
})();
