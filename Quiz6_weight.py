def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21
height = 180
gender = "남자"
weight = round(std_weight( height/ 100, gender), 2)
print("키", height, gender,"의 표준 중량은", weight,"입니다")

'''
if 첫 번째는 남자일 경우 공식으로 만들고
나머지 else 구문은 여자인 경우 공식으로 만들고
키 와 성별은 180, 남자로 지정한다
소숫점 2째 자리 까지 표기해야하니 round 로 만들고 height 에 100을 나눠 m 단위로 만들었다
'''