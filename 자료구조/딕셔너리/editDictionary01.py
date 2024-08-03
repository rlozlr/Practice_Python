# 학생의 시험 점수가 60점 미만이면 'F(재시험)'으로 값을 변경
scores = {'kor' : 88, 'eng' : 55, 'mat' : 85, 'sci' : 57, 'his' : 82}
print(f'scores : {scores}')

minScore = 60
fLvl = 'F(재시험)'
pLvl = 'P(통과)'

for sub in scores:
    if scores.get(sub) < 60:
        scores[sub] = fLvl
    else:
        scores[sub] = pLvl

print(f'scores : {scores}')
