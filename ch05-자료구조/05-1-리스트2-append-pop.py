# 5.1.2
subway = ["푸", "피글렛", "티거"]
print(subway)  # ['푸', '피글렛', '티거']

# 피글렛이 몇 번째 칸에 탔는가?
print(subway.index("피글렛"))  # 1

# 이요르 탑승
subway.append("이요르")
print(subway)  # ['푸', '피글렛', '티거', '이요르']

# 루를 푸와 피글렛 사이(인덱스 1 위치)에 삽입
subway.insert(1, "루")
print(subway)  # ['푸', '루', '피글렛', '티거', '이요르']

# 지하철 역마다 한 명씩 내림
print(subway.pop())  # 이요르 내림
print(subway)
print(subway.pop())  # 티거 내림
print(subway)
print(subway.pop())  # 피글렛 내림
print(subway)

# 지하철에서 모두 내림
subway.clear()
print(subway)  # []
