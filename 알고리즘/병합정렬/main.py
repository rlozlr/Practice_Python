# 1부터 100까지의 난수 10개를 생성하고, 다음의 요구사항을 만족하는 모듈 만들기
'''
1) 병합 정렬 Algorithm을 이용한 난수 정렬 모듈 구현
2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가
'''

import random
import 병합정렬 as sm

rNums = random.sample(range(1, 101), 10)
print(f'not sorted rNums: {rNums}')
print(f'sorted rNums ASC: {sm.mSort(rNums)}')
print(f'sorted rNums DESC: {sm.mSort(rNums, asc=False)}')