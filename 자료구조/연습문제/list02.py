# 1부터 100사이에 난수 10개를 생성한 후 짝수와 홀수를 구분해서 List에 저장하고 각각의 개수를 출력
import random
ranNumList = random.sample(range(1, 101), 10)
evens = []
odds = []

for num in ranNumList:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print('random number: {}'.format(ranNumList))
print('evens: {} >>> evens 개수: {}'.format(evens, len(evens)))
print('odds: {} >>> odds 개수: {}'.format(odds, len(odds)))
