"""
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

e.g.) http://naver.com

규칙1 : http:// 부분은 제외 => naver.com 
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'의 갯수 + "!"로 구성
          (nav)               (5)         (1)             (!)

e.g.) 생성된 비밀번호 : nav51!
"""
# url = "http://naver.com"

url = "http://daum.net"  # dau40!
# url = "http://google.com" # goo61!
# url = "http://youtube.com" # you71!

my_str = url.replace("http://", "")

# naver.com일 때 my_str.index(".")의 결과는 5이므로 다음 문장은 my_str = mystr[0:5]와 같음
my_str = my_str[: my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(url, password))
