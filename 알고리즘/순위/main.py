# 학급 학생(20명)들의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고, 중간고사 대비 기말고사 순위 변화(편차)를 출력
# (시험 성적은 난수 이용)
import 순위 as rm
import random

midStdScos = random.sample(range(50, 101), 20)
endStdScos = random.sample(range(50, 101), 20)

rd = rm.RankDeviation(midStdScos, endStdScos)
rd.setMidRank()
print('-' * 40)
print(f'midStdScos : {midStdScos}')
print(f'midRank : {rd.getMidRank()}')
print('-' * 40)
rd.setEndRank()
print(f'endStdScos : {endStdScos}')
print(f'endRank : {rd.getEndRank()}')
print('-' * 40)
rd.printRankDeviation()


