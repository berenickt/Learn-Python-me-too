# 5.2.1 딕셔너리 : 키와 값이 있는 구조
cabinet = {3: "푸", 100: "피글렛"}

print(cabinet[3])  # key 3에 해당하는 value, 푸
print(cabinet[100])  # key 100에 해당하는 value, 피글렛

print(cabinet.get(3))  # key 3에 해당하는 value, 푸

print(cabinet.get(5))  # None
print("hi")
# print(cabinet[5]) # KeyError 발생
print("hi")

print(cabinet.get(5, "사용 가능"))  # key에 해당하는 값이 없으면 기본값을 사용하게 함, 사용 가능

print(3 in cabinet)  # True
print(5 in cabinet)  # False


cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet["A-3"])  # 푸
print(cabinet["B-100"])  # 피글렛

print("곰" in "곰돌이")  # True
print("돌이" in "곰돌이")  # True
print("푸" in "곰돌이")  # False
