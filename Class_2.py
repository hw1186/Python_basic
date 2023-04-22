class unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(unit, Flyable):
    def __init__(self):
        # super().__init__()
        unit.__init__(self)
        Flyable.__init__(self) # 하나씩 확ㅇ

dropship = FlyableUnit()