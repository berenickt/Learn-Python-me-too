# 7.3.2
def profile(name, age, main_lang):  # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)


profile(name="찰리", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="루시")


def profile(name, age, main_lang):  # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)


profile("찰리", age=20, main_lang="파이썬")  # 올바른 함수 호출: 일반 전달값을 먼저 작성
# profile(name="루시", 25, "파이썬") # 잘못된 함수 호출: 키워드 인자를 먼저 작성


def profile(name, age, main_lang):
    print(name, age, main_lang)

    profile("찰리", 20, "파이썬")  # 위치 인자: "찰리", 20, "파이썬"
