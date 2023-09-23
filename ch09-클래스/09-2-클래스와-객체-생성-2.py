class Unit:
    def __init__(self, name, hp, damage):  # 생성자, self 외 전달값 3개
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


soldier1 = Unit("보병", 40, 5)  # 객체 생성
soldier2 = Unit("보병", 40, 5)  # 객체 생성
tank = Unit("탱크", 150, 35)  # 객체 생성
# soldier3 = Unit("보병") # 전달값 3개 중 1개만 넘김, TypeError 발생
# soldier3 = Unit("보병", 40) # 전달값 3개 중 2개만 넘김, TypeError 발생
