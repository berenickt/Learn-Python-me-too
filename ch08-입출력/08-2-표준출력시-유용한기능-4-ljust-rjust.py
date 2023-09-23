# 8.2.4
scores = {"수학": 0, "영어": 50, "코딩": 100}

for subject, score in scores.items():  # (key, value)
    print(subject, score)
"""위 코드의 실행결과
수학 0
영어 50
코딩 100
"""

""" 💡 ljust와 rjust
ljust(8) : 왼쪽으로 8칸 공간을 확보한 상태에서 왼쪽으로 정렬 후 출력
rjust(4) : 오른쪽으로 4칸 공간을 확보한 상태에서 오른쪽으로 정렬 후 출력
"""
scores = {"수학": 0, "영어": 50, "코딩": 100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
"""위 코드의 실행결과
수학      :   0
영어      :  50
코딩      : 100
"""
