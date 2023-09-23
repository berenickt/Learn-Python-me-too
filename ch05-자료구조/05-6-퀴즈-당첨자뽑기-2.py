"""
Quiz) 학교에서 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤르를 진행합니다.
댓글 작성자 중 추점을 통해 1명은 치킨, 3명은 커피 쿠폰을 받습니다.
추첨 프로그램을 작성하시오.

조건 1 : 편의상 댓글은 20명이 작성했고, 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다! --

(활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
"""

# 방법2
from random import *

users = list(range(1, 21))  # range()를 list()로 바로 감싸서 한 줄 줄이기
shuffle(users)
chicken_winner = sample(users, 1)  # 치킨 당첨자 1명 추첨
remain_users = set(users) - set(chicken_winner)  # 전체 집합에서 치킨 당첨자 집합 제외
coffee_winners = sample(remain_users, 3)  # 남은 19명 중에서 3명 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken_winner))
print("커피 당첨자 : {0}".format(coffee_winners))
print("-- 축하합니다! --")
