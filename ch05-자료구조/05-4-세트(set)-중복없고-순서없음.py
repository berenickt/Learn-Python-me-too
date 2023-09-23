""" 집합(set)
중복안됨, 순서없음
"""
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

java = {"푸", "피글렛", "티거"}  # 자바 개발자 세트
python = set(["푸", "이요르"])  # 파이썬 개발자 세트

# 교집합(자바와 파이썬을 모두 다룰 수 있는 개발자)
print(java & python)  # {'푸'}
print(java.intersection(python))  # {'푸'}

# 합집합(자바 또는 파이썬을 다룰 수 있는 개발자)
print(java | python)  # {'이요르', '티거', '푸', '피글렛'}
print(java.union(python))  # {'이요르', '티거', '푸', '피글렛'}

# 차집합(자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자)
print(java - python)  # {'피글렛', '티거'}
print(java.difference(python))  # {'피글렛', '티거'}

# 파이썬 개발자 추가(기존 개발자: 푸, 이요르)
python.add("피글렛")
print(python)  # {'푸', '이요르', '피글렛'}

# 자바 개발자 삭제(기존 개발자: 푸, 피글렛, 티거)
java.remove("피글렛")
print(java)  # {'푸', '티거'}
