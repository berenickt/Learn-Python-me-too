# 👉 6.2.2 while 문
customer = "토르"  # 손님 닉네임
index = 5  # 초깃값, 부르는 횟수 최대 5번

while index >= 1:  # 부르는 횟수가 1 이상일 때만 실행
    print("{} 님, 커피가 준비됐습니다.".format(customer))
    index -= 1  # 횟수 1회 차감
    print("{}번 남았어요.".format(index))
    if index == 0:  # 5번 모두 불렀다면
        print("커피를 폐기 처분합니다.")

"""
customer = "아이언맨"
index = 1

while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index += 1
"""

customer = "토르"
person = None

while person != customer:
    print("{0} 님, 커피가 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
