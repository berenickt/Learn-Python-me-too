# 7.2.3
def open_account():
    print("새로운 계좌를 개설합니다.")


open_account()  # open_account() 함수 호출


def deposit(balance, money):  # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money  # 입금 후 잔액 정보 반환


def withdraw_night(balance, money):  # 업무 시간 외 출금
    commission = 100  # 출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance - money - commission


balance = 0  # 초기 잔액
balance = deposit(balance, 1000)  # 1,000원 입금

# 업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


(name, age, hobby) = ("피글렛", 20, "코딩")  # 변수명에 소괄호가 없어도 실행결과는 동일
print(name, age, hobby)

name, age, hobby = ("피글렛", 20, "코딩")  # 변수명에 소괄호가 없어도 실행결과는 동일
print(name, age, hobby)

name, age, hobby = "피글렛", 20, "코딩"  # 값에 소괄호가 없어도 실행결과는 동일
print(name, age, hobby)
