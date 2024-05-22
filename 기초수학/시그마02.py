numA = int(input('a1 입력: '))
numR = int(input('공차 입력: '))
numN = int(input('n 입력: '))

val = 0
sum = 0

sum = numA * (1 - (numR ** numN)) / (1 - numR)
print('{}번째 항까지의 합: {}'.format(numN, int(sum)))
