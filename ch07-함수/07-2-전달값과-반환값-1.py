# 7.2.1
def open_account():
    print("새로운 계좌를 개설합니다.")


open_account()  # open_account() 함수 호출


def deposit(balance, money):  # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money  # 입금 후 잔액 정보 반환


balance = 0  # 초기 잔액, balance 변수에 초깃값으로 0 저장
balance = deposit(balance, 1000)  # 1,000원 입금, balance 변수에 deposit() 함수의 반환값을 다시 저장
# deposit(balance, 1000)
