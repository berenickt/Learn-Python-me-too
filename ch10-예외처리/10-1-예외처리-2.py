# 10.1.2
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) # 연산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# 값 에러인 경우
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
# 0으로 나눌 수 없는 에러인 경우
except ZeroDivisionError as err:
    print(err)
# 그 외 모든 에러인 경우
except Exception as err:
    print("알 수 없는 오류가 발생했습니다.")
    print(err)
