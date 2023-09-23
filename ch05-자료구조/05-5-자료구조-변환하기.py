menu = {"커피", "우유", "주스"}
print(menu)  # {'주스', '커피', '우유'}
print(type(menu))  # <class 'set'>

menu = list(menu)  # 리스트로 변환
print(menu, type(menu))  # ['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu)  # 튜플로 변환
print(menu, type(menu))  # ('주스', '커피', '우유') <class 'tuple'>

menu = set(menu)  # 세트로 변환
print(menu, type(menu))  # {'주스', '커피', '우유'} <class 'set'>
