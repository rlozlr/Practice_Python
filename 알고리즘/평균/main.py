# 다음은 어떤 체조선수의 점수이다.
'''
sco1  | 8.9
sco2  | 7.6
sco3  | 8.2
sco4  | 9.1
sco5  | 8.8
sco6  | 8.1
sco7  | 7.9
sco8  | 9.4
sco9  | 7.2
sco10 | 8.7
'''
# 평균을 구하고 순위를 정하는 Algorithm 만들기
import 평균 as near

scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
top5Scores = [9.12, 8.95, 8.12, 7.90, 7.88]

total = 0; avg =0
for n in scores:
    total += n

avg = round(total/len(scores), 2)

print(f'total: {total}')
print(f'avg: {avg}')

tp = near.Top5Scores(top5Scores, avg)
tp.setAlignScore()
top5Scores = tp.getFinalTopScores()
print(f'top5Scores: {top5Scores}')