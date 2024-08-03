# 학생의 시험 점수가 60점 미만이면 'F(재시험)'으로 값을 변경하는 코드를 keys()를 이용하여 작성
scores = {'kor' : 88, 'eng' : 55, 'mat' : 85, 'sci' : 57, 'his' : 82}
print(f'scores : {scores}')

minScore = 60
fLvl = 'F(재시험)'
pLvl = 'P(통과)'
fSub = {}

for sub in scores.keys():
    if scores.get(sub) < 60:
        scores[sub] = fLvl
        fSub[sub]  = fLvl;
    else:
        scores[sub] = pLvl


print(f'scores : {scores}')
print(f'fSub : {fSub}')
