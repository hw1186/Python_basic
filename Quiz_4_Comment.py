from random import *

Comment = ['id1', 'id2', 'id3', 'id4', 'id5', 'id6', 'id7', 'id8', 'id9', 'id10', 'id11', 'id12', 'id13', 'id14',
           'id15', 'id16', 'id17', 'id18', 'id19', 'id20']

print("참가자는?")
print(Comment)

print("-----당첨자 발표-----")
shuffle(Comment)
winner = sample(Comment, 4)
print("치킨 당첨자")
print(winner[0])
# print(sample(Comment, 1))
print("커피 당첨자")
print(winner[1:4])
# print(sample(Comment, 3))

print("-----축하합니다-----")

'''

        <정답>
        
90% 맞음 (총 1시간 이상...?분 소요....)

*** 몇가지 코드 단순화르르 위한 팁
range = 1~20 까지 다 정리하기 너무 힘드니까 
변수 = range(n, n) 하면 생성해준다

중복 당첨이 불가능 하니 다시 풀겠다.

winner 변수를 하나 더 만들어서 풀었다

winner = sample(Comment, 4)


'''


