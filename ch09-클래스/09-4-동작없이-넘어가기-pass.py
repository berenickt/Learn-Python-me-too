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
        pass  # pass : 아무것도 안하고 넘어간다


# 보급고: 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시")  # 체력 500, 생성 위치 7시


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()
