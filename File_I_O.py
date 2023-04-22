# 파일 입출력

'''
score_file = open("score.txt", "w") # 파일 열기
# 오픈으로 파일을 열고 -> 파일 이름 -> w 는 쓰기 위한 목적으로 정의 -> encoding에서 utf8으로 정의 하지 않으먼 파일을 열었을때 꺠질수도 있다

print("수학 : 0", file=score_file) # 파일안에 값 입력
print("영어 : 50", file=score_file)
score_file.close() # 파일 닫기

# 새로운 score.txt 파일이 생성이 됐다
'''


'''
score_file  = open("score.txt", "a") # 내용이 존재하는 파일에 이어 쓸려면 a를 써야한다
score_file.write("과학 : 80") # write로 이어 쓸수 있다
score_file.close
'''

'''
score_file = open("score.txt", "r") # 파일을 읽어온다는 의미가 된다
print(score_file.read()) # 파일에 모든 내용을 읽는다
score_file.close()
'''


'''

score_file = open("score.txt", "r") # 파일을 읽어온다는 의미가 된다
print(score_file.readline()) #줄 별로 읽는다
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

'''

'''

score_file = open("score.txt", "r")
while True:
    line = score_file.readline()
    if not line: # 라인이 없으면 멈춘다
        break
    print(line)
score_file.close()

'''
