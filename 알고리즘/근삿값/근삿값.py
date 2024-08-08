# 근삿값 Algorithm을 이용해서 시험 점수를 입력하면 학점 출력
# 평균 점수에 따른 학점 기준 점수
'''
95에 근삿값이면 A
85에 근삿값이면 B
75에 근삿값이면 C
65에 근삿값이면 D
55에 근삿값이면 F
'''

def getNearNum(an):
    gradeScores = [95, 85, 75, 65, 55]
    nearNum = 0
    minNum = 100

    for n in gradeScores:
        absNum = abs(n - an)
        if absNum < minNum:
            minNum = absNum
            nearNum = n

    if nearNum == 95:
        return 'A'
    elif nearNum == 85:
        return 'B'
    elif nearNum == 75:
        return 'C'
    elif nearNum == 65:
        return 'D'
    elif nearNum <= 55:
        return 'F'
