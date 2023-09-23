# 👉 4.5.1 \n : 줄바꿈
print("백문이 불여일견 백견이 불여일타")
# print("백문이 불여일견 # SyntaxError 발생
# 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")


# 👉 4.5.2 문장 내에서 따옴표 표시
# print("저는 "나도코딩"입니다.")
print("저는 '나도코딩'입니다.")  # 작은 따옴표 표시
# 또는
print('저는 "나도코딩"입니다.')  # 큰 따옴표 표시

print('저는 "나도코딩"입니다.')
print("저는 '나도코딩'입니다.")


# 👉 4.5.3 탈출문자, \"\" : 문장 내에서 따옴표
# 👉 \\ : 문장 내에서 \로 바뀜
# print("C:\Users\Nadocoding\Desktop\PythonWorkspace") # SyntaxError 발생
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")


# 👉 4.5.4 \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")  # PineApple

# 👉 4.5.5 \b : 백스페이스 역할(1글자 지우는 역할)
print("Redd\bApple")  # RedApple

# 👉 4.5.6 \t : 키보드 탭역할 (2 or 칸씩 역할함)
print("Red\tApple")  # Red     Apple
