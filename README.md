Python Basic

# 변수 사용법
a = 'Test'
b = '안녕'
c = 17

print("This is" , a, "안녕하세요", b, "내 나이는", c)

# 주석
- 포함되어 있지만 실행은 되지 않는 구문

(#), (''')

# 연산자
- and &, 둘다 포함한값

-or |, 둘중하나

# abs (절댓값)
print(abs(-5)) #5

# pow (제곱)
print(pow(4, 2)) #16

# max (최댓값), min (최솟값)
print(max(5, 12)) #12

print(min(5, 12)) #5

# round (반올림)
print(round(3.14)) #3

# random (함수)
파이썬이 제공하는 렌덤 라이브러리

print(random()) # 0.0 ~ 1 임의의 값 생성
print(random() * 10) # 0 ~ 10 임의의 값 생성
print(int (random() *10) + 1) # 자료만 출력 1 부터 10 이하의 임의의 값 생성
randint (i, j) # i j 를 포함한 값중에 임의의 값

# 슬라이싱
필요한 정보를 가저오는 표기

numbers =  "01049165703"
print("전화번호 : ", numbers[0:12]) #[:] 와 의미가 같음

# 문자열 처리 함수
lower - 소문자
upper - 대문자
len - 길이 반환
replace - 문자 변환
index - 인덱스 값 찾기
find - index 와 비슷함 원하는 문자열이 포함 되어있지 않으면 -1을 반환함
count - 같은 문자가 몇번 포함되어있는지 숫자를 반환함

# 문자열 포멧
print("Im %d " %17) 
print("%s world" % "Hello")
print("%c" % "a")
print("abcde {} ghij {}".format("E", "K"))

# 리스트
순서를 가지는 객체의 집합
a = [ ]

- 리스트 더하기

(a.append( ))

(a.inster(n, ))

- 리스트 빼기

(a.pop())

- 객체들 수 구하기

(a.count( ))

- 객체 정렬하기

a.sort # 숫자들 순서대로 정렬

a.reverse # 거꾸로 정렬

a.clear # 리스트 모두 삭제 

- 리스트 확장

a.extend(b)


# 사전 (dictionary)

변수 = {키 : 벨류, key : value}

- 값이 없을 경우

[ ] = 키를 불러울 경우 오류가 나고 코드가 종료가 됨

get( ) = 키를 불러올 경우 오류가 나지만 코드는 계속 이어진다
get 은 벨류를 불러오지 못할경우 gen ( , ) 뒤에 이어나올 것을 입력할수 있다

print(키 in 변수) - 어떠한 키가 변수안에 들어있다면 True를 출력한다

- 값 추가
변수 = { 키 } = 벨류
  
- 값 변경
변수 = { 기존의 키 } = 새로운 벨류
  
- 값 제거
del 변수 [ 키 ]
  
- 키 출력

print(변수.keys())

- 벨류만 출력

print(변수 . values())

- 둘다 출력 

print(변수 . items())

- 지우기

변수.clear()

# 튜플
고정된  

변수 = (값 , 값)

# 집합 (set)
중복 안됨, 순서 없음

my_set = {1,2,3,4,4,4}
print(my_set) # 1, 2, 3, 4

# 교집합
서로 다른 집합에 있는 공통된 값 출력하기

a = {1,2,3}
b = {3,4,5}

print(a & b) # 3
= print(a.intersection(b))

# 합집합
중복 제거

a = {1,2,3}
b = {3,4,5}

print(a | b) # 1,2,3,4,5
= print(a.union(b))

# 차집합
변수 a를 제외한 b의 포함된 모든 값 삭제

a = {1,2,3}
b = {3,4,5}

print(a | b) # 1,2

# 집합의 추가 

변수.add( 값 )

# 집합의 제거

변수.remove( 값 )

# 자료 구조의 변경 

test_1 = {1, 2, 3, 4, 5} # 자료형을 세트로 설정
print(type(test_1))  # 자료형 타입을 출력 - class 'set'

test_1 = list(test_1) # 자료구조의 값을 리스트로 변경
print(test_1) # [1, 2, 3, 4, 5]

test_1 = tuple(test_1) # 자료 구조의 값을 튜플로 변경
print(test_1) (1, 2, 3, 4, 5)

# 셔플 (shuffle)
리스트 안에 있는 값을 무작위로 변경

shuffle(변수)

# 샘플 (sample)
리스트 안에 값중 n 개를 출력

print (sample(변수, n))

# if
참 거짓으로 구문을 판단

if 조건:
    (실행 명령문) # 참 일시 출력 아닐시 다음

elif (조건):
    (실행 명령문) # 참 일시 출력 아닐시 다음

else: 
    (실행 명령문) # 참이 없을시

# if 조건의 연산자
연산자를 이용해 if 문의 조건을 추가할수 있다

if 조건 or 조건 2
    (실행 명령문)

if 조건 and 조건 2
    (실행 명령문)

if 조건 <= 조건 2
    (실행 명령문)


# input
변수의 값을 지정한다

변수 = input(" ")

int 형태의 값

변수 = int(input())


# for
반복문 

for hello in [1,2,3,4,5]:
    print(hello) # 1,2,3,4,5

test_1 = ['a', 'b', 'c', 'd']

for test_2 in test_1:
    print(test_2) # a, b, c, d

# while 
조건이 만족될때 까지 반복

name = '반복문 수행중'
index = 5

while index >= 1:
    print(name)
    index -= 1
    if index == 0:
        print("반복문 종료")

while (true) : # 무한 루프 

name = '이름이 어떻게 되세요'
person = '현우'

while name !=  person :
    print(name)
    name = input("") # 현우가 출력될떄 까지 반복

# continue , break
continue : 건너 뛰기

test_2 = [2, 5]

for test_1 in range(1, 11):
    if test_1 in test_2:
        continue
    print(test_1)

2, 5 를 제외한 숫자 읽기

break : 끝내기

test_2 = [2, 5]
test_3 = [7]

for test_1 in range(1, 11):
    if test_1 in test_2:
        continue
    elif test_1 in test_3:
        break
    print(test_1) # 7 을 만나면 더 이상 구문을 실행하지 않음

# 한줄 for

test_1 = [1,2,3,4,5]
test_2 = [i + 100 for i in test_1] # i 의 100을 더한값을 test_1 에 삽입
print (test_1) # 1,2,3,4,5 
print (test_2)  # 101, 102, 103, 104, 105

[ 수행문 for 문 ]
 
# 함수

def open_def(): # 함수 열기
    print("안녕하세요") # 입력

open_def() 함수 실

# 전딜깂과 반환값 

ex) 계좌 입금 함수

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다", balance + money)
    return balance + money # 총 금액 반환

blance = 0 # 잔액
blance = deposit(blance, 1000) # 함수 호출
print(blance) # 반환

ex) 출금 함수

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은", balance-money)
    else:
        print("출금이 완료되지 않았습니다", balance)
        return balance

blance = 0 # 잔액
blance = deposit(blance, 1000)
blance = withdraw(blance, 500)

# 기본값  

ex )

def profile(name, age= 17, main_lang = 'Python'): # 함수의 값을 미리 지정하여 사용할수 있다
    print("이름 :",name, "\t", "나이 :", age, "\t", "주 사용언어 :",main_lang)

profile("현우") 

# 키워드 값
함수의 순서가 바뀌어 있어도 함수의 키워드만 전달이 된다면 순서대로 출력된다

def profile(name, age, main_lang):
    print("이름 :",name, "\t", "나이 :", age, "\t", "주 사용언어 :", main_lang)

profile(main_lang='python', name='현우', age=17)

# 가변인자 
함수의 값이 추가될때 원하는 값만큼 불러낼수 있는 함수 

def profile(name, age, *lang): # * 을 이용해 가변인자 생성
    print("이름 :",name,'\t' "나이 :",age)
    for language in lang: # language 안에 lang의 값들을 입력후 출력
        print(language)
    print()

profile("현우", 17, "Python", "Java", "C", "C++", "C#")

# 출력 포멧

# 빈 자리는 빈공간으로 두고, 오른쪽으로 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +, 음수일 땐 - 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정려하고 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000))

# 3자리 마다 콤마를 찍어주고 부호도 붙이고 , 자릿수 확보하기 빈 자라는 ^로
print("{0:^<+30,}".format(100000000000))

# 소숫점 출략
print("{0:f}".format(5/3))

# 소숫점 특정 자리수 짜기만 쵸시
print("{0:.2f}".format(5/3)) # 소숫점 3자리에서 반올림

# pickle
프로그램 상에서 데이터를 파일 형태로 저장하는것

- 피클 사용 

import pickle
profile_file = open("profile.pickle", "wb") # 바이너리 타입은 wb로 지정해야하 한다
prifile = {"name":"hw", "age":17, "hobby":["game", "music", "codding"]} # 프로필 설정
print(prifile) # 출력
pickle.dump(prifile, profile_file) # profile에 있는 정보를 파일에 저장
profile_file.close() # 닫는다 

- 피클 가져오는 법

import pickle
profile_file = open("profile.pickle", "rb") # 바이너리 타입은 읽기 니까 Read 로 지정
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# with

1.
import pickle

with open("profile.pickle", "rb") as profile_file: # 피클 파일을 읽고 파일정보를 profile_file 에 넣는다
    print(pickle.load(profile_file)) # pickle.load를 통해서 proflie_file 을 읽을수 있다

2.
with open("study.txt", "w") as study_file: # study.txt 파일을 만든다 쓰기모드로
    study_file.write("안녕하세요") # 쓰기 완료하면 자동으로 닫히며 파일이 완성 된다

3.
with open("study.txt", "r") as study_file: # study.txt 파일을 만든다 읽기 모드로
    print(study_file.read())

# 예외처리
오류가 발생했을떄 처리하는것

try:
    print("나누기 전용")
    num1 = int(input("첫 번째 값:"))
    num2 = int(input("두 번째 값:"))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러 발생")

에러 발생시 마지막 구문에서 처리

# 패키지
모듈들의 집합

# Python_basic
