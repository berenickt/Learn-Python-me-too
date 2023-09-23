print("ab" + "ab")
print("ab", "ab")

# 👉 4.4.1 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)  # %s로도 정수값 표현 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 값이 여럿일 때

# 👉 4.4.2 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 👉 4.4.3 방법 3, (v3.6 이상~ 부터 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
