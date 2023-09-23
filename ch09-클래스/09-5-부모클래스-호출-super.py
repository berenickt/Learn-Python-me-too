class Unit:
    def __init__(self, name, hp, speed):  # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed  # 지상 이동 속도

    def move(self, location):  # 이동 동작 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) # 지상 이동 속도 0, 건물은 지상 이동 불가
        super().__init__(name, hp, 0)  # 부모 클래스 접근, self 없이 사용
        self.location = location
