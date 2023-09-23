import time

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 연-월-일 시:분:초

import datetime

print("오늘 날짜는", datetime.date.today())
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일째 날짜 저장
print("우리가 만난 지 100일은", today + td)  # 오늘부터 100일 후 날짜
