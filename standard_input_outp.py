# 표준 입출력
'''
1. sep 를 통해 간격을 지정할수 있다

2. end 는 문장에 끝 부분을 지정할수 있다

3. import sys - sys.sterr 는 에러를 확인할수 있다

4. zfill(n) n의 개수 만큼 0으로 빈칸을 채운다

'''
'''

1.
print("python", "java", sep = " C++ ") # sep 를 통해 간격을 지정할수 있다

2.
print("python", "java", sep = ",", end = "?") # end 는 문장에 끝 부분을 지정할수 있다

3.
import sys

print("python", "java", file=sys.stdout) # 표준 출력
print("python", "java", file=sys.stderr) # 표준 에러

4.
scores = {"수학": 0, "영어": 50, "코딩": 100}

for subject, score in scores.items(): # iteams() = 키 벨류 출력
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 왼 쪽으로 8 칸 공간 확보 후 정렬 스코어는 4칸의 공간 확보후 오른쪽 정렬
    
5.
for num in range(1, 21):
    print("대기번호 :", str(num).zfill(3)) # 값이 없는 빈 공간은 0으로 3칸 채운다
    
6.
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 :", answer) # 사용자에서 입력을 받으면 항상 문자열 형태로 저장이 된다


'''