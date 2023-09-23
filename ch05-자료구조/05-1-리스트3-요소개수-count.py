# 5.1.3
# 같은 이름이 몇 명 있는지 확인
subway = ["푸", "피글렛", "티거"]
subway.append("푸")  # 푸 추가

print(subway)  # ['푸', '피글렛', '티거', '푸']
print(subway.count("푸"))  # 2
