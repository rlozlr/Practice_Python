numA = int(input('a1 입력: '))
numD = int(input('공차 입력: '))
numN = int(input('n 입력: '))

val = 0
sum = 0

val = numA + (numN - 1) * numD
sum = numN * (numA + val) / 2
print('{}번째 항까지의 합: {}'.format(numN, int(sum)))
