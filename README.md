# 대포항생선찜본점 홈페이지

https://daepohang-fish.netlify.app

- `site/` : 실제로 배포되는 홈페이지 파일 (Netlify가 이 폴더를 올립니다)
- `tools/gen_pages.py` : 키워드 페이지, 안내 페이지, sitemap.xml 생성기
- `tools/pages2.py` : 키워드 페이지 내용

페이지 다시 만들기: `python3 tools/gen_pages.py site`
