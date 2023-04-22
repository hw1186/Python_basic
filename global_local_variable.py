# # 지역변수, 전역변수
# 지역변수 - 함수 호출이 될때 사용하고 함수가 종료되면 사라진다
# 전역변수 - 프로그램 내에서 모두 사용가능하는 변수
#
# ex)

'''gun = 10

def checkpoint(soldiers): # 경계 근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 :", gun)

print("전체 총 :", gun)
checkpoint(2) # 2명이 경계 근무를 나감
print("남은 총", gun)'''

# 오류 발생 이유 - 할당이 안됨 gun이 함수 안에서 초기화가 안됨
#
# ex2 )

'''gun = 10

def checkpoint(soldiers): # 경계 근무됨
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 :", gun)

print("전체 총 :", gun)
checkpoint(2) # 2명이 경계 근무를 나감
print("남은 총", gun)'''

# - 함수 내에서 남은 총은 할당된 20 이지만 함수 밖에서 할당된 총은 10자루 이다
#
# ex 3)

'''gun = 10

def checkpoint(soldiers): # 경계 근무됨
    global gun # 전역변수에 있는 변수를 사용
    gun = gun - soldiers 
    print("[함수 내] 남은 총 :", gun)

print("전체 총 :", gun)
checkpoint(2) # 2명이 경계 근무를 나감
print("남은 총", gun)'''

# - 함수 내에서 전역변수를 지역변수로 사용할수 있게 바꾼다

# ex 4)

'''gun = 10

def checkpoint(gun, soldiers):
    gun = gun - soldiers 
    print("[함수 내] 남은 총 :", gun)
    return gun

print("전체 총 :", gun)
gun = checkpoint(gun, 2)
print("남은 총", gun)'''