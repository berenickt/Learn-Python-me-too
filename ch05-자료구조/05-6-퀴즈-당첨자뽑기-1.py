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
# 방법1
from random import *

users = range(1, 21)  # 리스트 생성, 1부터 21 직전(20)까지 연속한 숫자 모음
users = list(users)  # users를 리스트 자료구조로 변환
shuffle(users)  # 리스트 섞기
winners = sample(users, 4)  # users 리스트에서 중복 없이 4명 추첨

print("-- 당첨자 발표 -- ")  # 당첨자 출력
print("치킨 당첨자 : {0}".format(winners[0]))  # 0번째 인덱스(1명)
print("커피 당첨자 : {0}".format(winners[1:]))  # 1번째부터 마지막까지 슬라이싱(3명)
print("-- 축하합니다! --")
