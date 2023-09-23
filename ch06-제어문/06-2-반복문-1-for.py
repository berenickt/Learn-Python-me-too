# 👉 6.2.1 for 문
for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no))  # {0} 위치에 waiting_no의 값이 들어감

for waiting_no in range(5):  # 0부터 5 직전까지(0~4)
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6):  # 1부터 6 직전까지(1~5)
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6, 2):  # 1부터 6 직전까지(1~5)에서 2씩 간격 주기
    print("대기번호 : {0}".format(waiting_no))

orders = ["아이언맨", "토르", "스파이더맨"]  # 손님 닉네임 리스트
for customer in orders:
    print("{0} 님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer))
