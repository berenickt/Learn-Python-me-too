glasses = 10  # 전체 3D 안경 개수: 10개


def rent(people):  # 3D 안경을 대여한 관객 수
    # glasses = 20 # 변수 정의 추가
    # global glasses # 전역 공간에 있는 glasses 변수를 함수 안에서 사용하겠다는 표시
    glasses = glasses - people  # 잔여 3D 안경 개수 = 전체 개수 - 대여한 개수
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))


print("전체 3D 안경 개수: {0}".format(glasses))
rent(2)  # 3D 안경을 대여한 관객이 2명일 때
print("남은 3D 안경 개수: {0}".format(glasses))

glasses = 10


def rent_return(glasses, people):  # 전체 3D 안경 수와 대여 관객 수를 전달받음
    glasses = glasses - people  # 전달값을 담은 glasses 사용
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))
    return glasses


print("전체 3D 안경 개수: {0}".format(glasses))
glasses = rent_return(glasses, 2)  # 함수 안에서 수정된 glasses 값을 반환받음
print("남은 3D 안경 개수: {0}".format(glasses))
