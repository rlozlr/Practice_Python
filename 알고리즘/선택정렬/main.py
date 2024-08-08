# 선택정렬 알고리즘을 이용해서 학생 20명의 시험 점수를 오름차순과 내림차순으로 정렬하는 모듈 만들기
# 시험 점수는 50부터 100까지
import random
import 선택정렬 as sm
import copy

scores = random.sample(range(50, 101), 20)
# print(f'scores: {scores}')
# print(f'scores lengthL {len(scores)}')

print(f'scores: {scores}')
result = sm.sortNumber(copy.deepcopy(scores))
print(f'result: {result}')

print(f'scores: {scores}')
result = sm.sortNumber(copy.deepcopy(scores), asc=False)
print(f'result: {result}')