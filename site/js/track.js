// 방문과 전화·길찾기 버튼 누름을 기록합니다. 쿠키를 쓰지 않습니다.
(function () {
  var ls; try { ls = window.localStorage; if (ls.getItem("dp-owner") === "1") return; } catch (e) {}
  var ss = {}; try { ss = window.sessionStorage; } catch (e) {}
  function get(k) { try { return ss.getItem(k) || ""; } catch (e) { return ""; } }
  function set(k, v) { try { ss.setItem(k, v); } catch (e) {} }
  var path = location.pathname;
  if (!get("dp-landing")) {
    var src = "직접 방문", q = "", r = document.referrer;
    try {
      if (r) {
        var u = new URL(r), h = u.hostname;
        if (h === location.hostname) src = "사이트 안";
        else if (/naver\./.test(h)) src = "네이버";
        else if (/google\./.test(h)) src = "구글";
        else if (/daum\.|kakao/.test(h)) src = "다음·카카오";
        else if (/instagram\./.test(h)) src = "인스타그램";
        else if (/bing\./.test(h)) src = "빙";
        else src = h.replace(/^www\./, "");
        q = u.searchParams.get("query") || u.searchParams.get("q") || "";
      }
    } catch (e) {}
    set("dp-landing", path); set("dp-src", src); set("dp-q", q);
  }
  var GA = { call: "phone_click", map: "map_click", menu: "menu_click", copy_phone: "phone_copy", copy_addr: "address_copy" };
  function send(t) {
    if (t !== "view" && window.gtag) window.gtag("event", GA[t] || t, { landing_page: get("dp-landing"), traffic_from: get("dp-src") });
    var body = JSON.stringify({ t: t, p: path, l: get("dp-landing"), s: get("dp-src"), q: t === "view" ? get("dp-q") : "" });
    if (navigator.sendBeacon) navigator.sendBeacon("/api/t", body);
    else fetch("/api/t", { method: "POST", body: body, keepalive: true });
  }
  send("view");
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a,button");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("tel:") === 0) send("call");
    else if (/map\.naver\.com|naver\.me|map\.kakao/.test(href)) send("map");
    else if (/#menu$/.test(href)) send("menu");
    else if (a.dataset && a.dataset.copy) send(/\d{3,}-\d{3,}/.test(a.dataset.copy) ? "copy_phone" : "copy_addr");
  }, true);
})();
