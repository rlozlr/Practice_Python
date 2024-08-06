# 시험 점수를 입력한 후, Tuple에 저장하고 과목별 학점 출력

kor = int(input('국어: '))
eng = int(input('영어: '))
mat = int(input('수학: '))
sci = int(input('과학: '))


scores = (
    {'국어':kor},
    {'영어':eng},
    {'수학':mat},
    {'과학':sci}
)
print(scores)

for sub in scores:
    for key in sub.keys():
        if sub[key] >= 90:
            sub[key] = 'A'
        elif sub[key] >= 80:
            sub[key] = 'B'
        elif sub[key] >= 70:
            sub[key] = 'C'
        elif sub[key] >= 60:
            sub[key] = 'D'
        else:
            sub[key] = 'F'

print(scores)
