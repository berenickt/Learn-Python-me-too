# 5.1.5 리스트 확장
mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list)  # ['푸', 20, True, [5, 2, 4, 3, 1]]


mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)  # 리스트 합치기
print(mix_list)  # ['푸', 20, True]
print(num_list)  # [5, 2, 4, 3, 1, '푸', 20, True]
