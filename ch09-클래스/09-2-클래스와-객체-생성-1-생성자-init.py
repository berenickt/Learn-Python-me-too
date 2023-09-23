class Unit:
    # __init__ 생성자 : 한 객체(보병, 탱크 1개)가 만들어질 떄 자동으로 호출되는 함수
    # self는 자기자신을 의미, python의 클래스 안에서 메소드들은 모두 self를 작성함
    def __init__(self, name, hp, damage):
        self.name = name  # 인스턴스 변수 name에 전달값 name 저장
        self.hp = hp  # 인스턴스 변수 hp에 전달값 hp 저장
        self.damage = damage  # 인스턴스 변수 damage에 전달값 damage 저장
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


soldier1 = Unit("보병", 40, 5)  # 보병1 생성, 전달값으로 이름/체력/공격력 전달
soldier2 = Unit("보병", 40, 5)  # 보병2 생성, 전달값으로 이름/체력/공격력 전달
tank = Unit("탱크", 150, 35)  # 탱크 생성, 전달값으로 이름/체력/공격력 전달
