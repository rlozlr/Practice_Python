# 1부터 100까지의 난수 100개를 생성하고, 다음의 요구사항을 만족하는 모듈
'''
1) 생성된 난수들을 오름차순 또는 내림차순으로 정렬하는 알고리즘 구현
2) 생성된 난수 중 최솟값, 최댓값을 반한하는 함수 구현
'''
import 삽입정렬 as sm
import random

nums = random.sample(range(1, 1000), 100)
print(f'not sorted numbers: {nums}')

# 객체 생성
sn = sm.SortNumbers(nums)

# 오름차순
sn.setSort()
sortedNumbers = sn.getsortedNumbers()
print(f'sortedNumbers by ASC: {sortedNumbers}')

# 내림차순
sn.isAscending(False)
sn.setSort()
sortedNumbers = sn.getsortedNumbers()
print(f'sortedNumbers by DESC: {sortedNumbers}')

# min & max
print(f'min: {sn.getMinNumber()}')
print(f'max : {sn.getMaxNumber()}')