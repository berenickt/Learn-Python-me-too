# 9.2.2
class Unit:
    def __init__(self, name, hp, damage):  # 생성자, 전달값 3개
        self.name = name  # 인스턴스 변수 name
        self.hp = hp  # 인스턴스 변수 hp
        self.damage = damage  # 인스턴스 변수 damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 전투기: 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 80, 5)  # 객체 생성, 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))  # 인스턴스 변수 접근

# 은폐 가능
stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloaking = True  # 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태

if stealth2.cloaking == True:  # 은폐 상태라면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))

# 오류 발생
# if stealth1.cloaking == True: # 다른 전투기의 은폐 여부
#     print("{0}는 현재 은폐 상태입니다.".format(stealth1.name))
