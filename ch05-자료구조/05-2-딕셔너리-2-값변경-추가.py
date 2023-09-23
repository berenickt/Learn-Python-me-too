# 5.2.2 값 변경 추가 삭제
cabinet = {"A-3": "푸", "B-100": "피글렛"}

print(cabinet)  # {'A-3': '푸', 'B-100': '피글렛'}

cabinet["A-3"] = "티거"  # key에 해당하는 값이 있을 때 -> 값 변경
cabinet["C-20"] = "이요르"  # key에 해당하는 값이 없을 때 - > 값 추가


print(cabinet)  # {'A-3': '티거', 'B-100': '피글렛', 'C-20': '이요르'}

del cabinet["A-3"]  # key 'A-3'에 해당하는 값 삭제
print(cabinet)  # {'B-100': '피글렛', 'C-20': '이요르'}
