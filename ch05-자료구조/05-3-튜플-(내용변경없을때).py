# 튜플은 내용 변경이 없을 때 사용
menu = ("돈가스", "치즈돈가스")
print(menu[0])  # 돈가스
print(menu[1])  # 치즈돈가스

name = "피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)  # 피글렛 20 코딩


(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)  # 피글렛 20 코딩

(departure, arrival) = ("김포", "제주")
print(departure, ">", arrival)  # 김포 > 제주

(departure, arrival) = (arrival, departure)
print(departure, ">", arrival)  # 제주 > 김포
