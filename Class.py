'''
name = "Marine" # unit name
hp = 40 # unit hp
damege = 5 # unit damage

print("{0} unit set".format(name))
print("hp {0}, damage{1}\n".format(hp, damege))

tank_name = "Tank"
tank_hp = 150
tank_damage = 35

print("{0} unit set".format(tank_name))
print("hp {0}, damage{1}\n".format(tank_hp, tank_damage))

tank_name2 = "Tank2"
tank_hp2 = 150
tank_damage2 = 35

print("{0} unit set".format(tank_name2))
print("hp {0}, damage{1}\n".format(tank_hp2, tank_damage2))

def attack(name, loccation, damage):
    print("{0} : {1} 방향으로 적군을 공격. [공격력 {2}]".format(name, loccation, damage))

attack(name, "1h", damege)
attack(tank_name, "2h", tank_damage)
attack(tank_name2, "3h", tank_damage2)
'''

# 이걸 class 로 만들어 보기

'''class Unit:
    def __init__(self, name, hp, damage): # 유닛 클래스를 만들고
        self.name = name # 필요한 값들을 만들기
        self.hp = hp
        self.damage = damage
        print("{0}, 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
'''

class Unit: # 일반 유닛, 부모클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 공격 유닛
class AttackUnit(Unit): # 자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속 값 불러오기
        self.damage = damage # Unit의 값을 상속 받음

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 공격 받은 함수
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 남았습니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}2 : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]".format(name, location, self.flying_speed))
#
# # 공중 공격 유닛 클래스
#     class FlyableAttackUnit(AttackUnit, Flyable):
#         def __int__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp, damage)
#             Flyable.__init__(self, flying_speed)


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location

'''
#유닛 만들기

firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5시")

#공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)
'''


'''
# 클래스 쓰는법
marin = Unit("Marin", 40, 5)
marin2 = Unit("Marin2", 40, 5)
tank = Unit("Tank", 150, 50)

warith1 = Unit("Warith", 80, 5) # 외부에서 맴버 변수 쓰기
print("유닛이름 : {0}, 공격력 : {1}".format(warith1.name, warith1.damage)) # 멤버 변수 접근

warith2 = Unit("Warith2", 80, 5)
warith2.clocking = True # 변수 추가 할당

if warith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다".format(warith2.name))
'''


''' 
     __init__
    객체의 생성자 

마린이나 탱크나 같이 클래스로 만들어지는 것을 객체라고 한다
마린과 탱크는 유닛의 인스턴스 라고 한다
객체가 생성될때는 init 함수가 정해진 갯수와 동일하게 해야한 (self 제외)

'''


'''

    멤버변수
클레스 내에서 정의된 변수

warith1 = Unit("Warith", 80, 5) # 외부에서 맴버 변수 쓰기
print("유닛이름 : {0}, 공격력 : {1}".format(warith1.name, warith1.damage)) # 멤버 변수 접근

'''


'''
    pass
구문을 넘어간다

'''

'''
    super

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


'''