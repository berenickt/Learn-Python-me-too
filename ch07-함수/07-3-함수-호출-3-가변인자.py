# 7.3.3
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age))
    print(lang1, lang2, lang3, lang4, lang5)


profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")
profile("루시", 25, "코틀린", "스위프트", "", "", "")


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")  # 줄 바꿈 대신 띄어쓰기
    print(lang1, lang2, lang3, lang4, lang5)


profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")
profile("루시", 25, "코틀린", "스위프트", "", "", "")


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(language, type(language))


profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")  # 자바스크립트 추가
profile("루시", 25, "코틀린", "스위프트")


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # print(language, type(language))
    for lang in language:
        print(lang, end=" ")  # 언어를 모두 한 줄에 표시
    print()  # 줄 바꿈 목적


profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트")


def add(item):
    print(item, "붓기")


def americano():
    add("뜨거운 물")
    add("에스프레소")


print("아메리카노 만드는 법")
americano()
