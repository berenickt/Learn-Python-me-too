from random import *  # random 모듈의 모든 기능을 가져다 쓰겠다는 의미

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성

print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46))  # 1 이상 46 미만에서 난수 생성
print(randint(1, 45))  # 1 이상 45 이하에서 난수 생성
