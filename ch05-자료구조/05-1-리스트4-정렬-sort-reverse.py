# 5.1.4
num_list = [5, 2, 4, 3, 1]

num_list.sort()  # 👉 오름차순 정렬
print(num_list)  # [1, 2, 3, 4, 5]

num_list.sort(reverse=True)  # 👉 내림차순 정렬
print(num_list)  # [5, 4, 3, 2, 1]

num_list.reverse()  # 👉 순서 뒤집기
print(num_list)  # [1, 2, 3, 4, 5]


my_list = [1, 3, 2]

my_list.sort()  # 리스트 정렬
print(my_list)  # my_list 리스트 데이터 변경, [1, 2, 3]

your_list = [1, 3, 2]
new_list = sorted(your_list)  # 정렬할 리스트를 소괄호 안에 넣음

print(your_list)  # your_list 리스트 데이터는 변경되지 않음, [1, 2, 3]
print(new_list)  # 정렬된 새로운 리스트, [1, 2, 3]
