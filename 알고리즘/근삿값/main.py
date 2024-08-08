# 근삿값 Algorithm을 이용해서 시험 점수를 입력하면 학점 출력
# 평균 점수에 따른 학점 기준 점수
'''
95에 근삿값이면 A
85에 근삿값이면 B
75에 근삿값이면 C
65에 근삿값이면 D
55에 근삿값이면 F
'''

import 근삿값 as near

scores = []

kor = int(input('국어: '))
scores.append(kor)

eng = int(input('영어: '))
scores.append(eng)

mat = int(input('수학: '))
scores.append(mat)

sci = int(input('과학: '))
scores.append(sci)

totalScore = sum(scores)
print(f'totalScore : {totalScore}')

avgScore = totalScore / len(scores)
print(f'avgScore: {avgScore}')

grade = near.getNearNum(avgScore)
print(f'grade: {grade}')