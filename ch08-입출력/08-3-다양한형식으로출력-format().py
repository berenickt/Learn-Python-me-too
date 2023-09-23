# 8.3 다양한 출력 포맷
print("{0}".format(500))  # {0} 위치에 값 500 출력

print("{0}".format(500))
# 빈칸으로 두기, 오른쪽 정렬, 공간 10칸 확보
print("{0: >10}".format(500))

# 빈칸으로 두기, 오른쪽 정렬, + 기호 붙이기, 공간 10칸 확보
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))  # 음수일 때

print("{0:_<10}".format(500))  # 빈칸을 _로 채우기, 왼쪽 정렬, 공간 10칸 확보

print("{0:,}".format(100000000000))  # 3자리마다 쉼표 찍기
print("{0:+,}".format(100000000000))  # + 기호 붙이기, 3자리마다 쉼표 찍기
print("{0:+,}".format(-100000000000))  # 음수일 때, 3자리마다 쉼표 찍기

# 빈칸을 ^로 채우기, 왼쪽 정렬, + 기호 붙이기, 공간 30칸 확보, 3자리마다 쉼표 찍기
print("{0:^<+30,}".format(100000000000))

print("{0}".format(5 / 3))

print("{0:f}".format(5 / 3))

print("{0:.2f}".format(5 / 3))  # 소수점 이하 둘째 자리까지 출력
