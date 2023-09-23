# 6.1.1
weather = "비"

if weather == "비":  # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print("우산을 챙기세요.")


# 6.1.2
weather = "맑음"

if weather == "비":
    print("우산을 챙기세요.")


weather = "미세먼지"

if weather == "비":
    print("우산을 챙기세요.")  # 1번
elif weather == "미세먼지":
    print("마스크를 챙기세요.")  # 2번


# 6.1.3
weather = "맑음"

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


# 6.1.4
weather = input("오늘 날씨는 어때요? ")
# print(weather)

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


weather = input("오늘 날씨는 어때요? ")

if weather == "비" or weather == "눈":  # 조건 변경
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


temp = int(input("오늘 기온은 어때요? "))  # 입력값을 정수형으로 형변환

if 30 <= temp:  # 30도 이상이면
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp and temp < 30:  # 10도 이상 30도 미만이면
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp and temp < 10:  # 0도 이상 10도 미만이면
    print("외투를 챙기세요.")
else:  # 그 외의 모든 경우(0도 미만이면)
    print("너무 추워요. 나가지 마세요.")


temp = int(input("오늘 기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp < 30:
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")


temp = int(input("오늘 기온은 어때요? "))

if temp >= 30:
    print("너무 더워요. 외출을 자제하세요.")
elif temp >= 10:
    print("활동하기 좋은 날씨예요.")
elif temp >= 0:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")
