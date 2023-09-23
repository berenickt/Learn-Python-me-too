# 7.3.1
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


profile("찰리", 20, "파이썬")
profile("루시", 25, "자바")


def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


profile("찰리")
profile("루시")


def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


profile("찰리")  # age, main_lang은 기본값 사용
profile("찰리", 22)  # main_lang은 기본값 사용
profile("찰리", 24, "자바")  # 기본값을 사용하지 않음


# 마트에서 2가지 상품을 구매하는 경우
def buy(item1, item2="음료수"):  # 올바른 함수 정의: 일반 전달값을 먼저 작성
    print(item1, item2)


buy("빵")  # item1=빵, item2=음료수

"""
# 마트에서 2가지 상품을 구매하는 경우
def buy(item1="음료수", item2): # 잘못된 함수 정의: 기본값을 가지는 전달값을 먼저 작성 
    print(item1, item2)

buy("빵") # item1=빵? item2=빵? 
"""
