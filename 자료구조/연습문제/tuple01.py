# 대학생 길동이의 1, 2, 3학년의 성적
'''
1학년 : 3.7, 4.2
2학년 : 2.9, 4.3
3학년 : 4.1, 4.2
'''
# 졸업할 때 4.0이상의 학점을 받기 위해 길동이가 받아야 하는 4학년 1, 2학기의 최소 학점 구하기

scores = (3.7, 4.2), (2.9, 4.3), (4.1, 4.2)
total = 0

for semester1 in scores:
    for semester2 in semester1:
        total += semester2

print(f'3학년 총학점: {round(total, 1)}')
print(f'3학년 평균: {round((total / 6), 1)}')
print('---------------------')
targetScore = round((4.0 * 8 - total), 1)
print(f'4학년 목표 총학점 : {targetScore}')

minScore = round((targetScore / 2), 1)
print(f'4학년 한 학기 최소 학점: {minScore}')
print('---------------------')

scores = list(scores)
scores.append((minScore, minScore))
scores = tuple(scores)
print(f'scores: {scores}')