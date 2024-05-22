numA = int(input('a1 입력: '))
dNum = int(input('공차 입력: '))
numN = int(input('n 입력: '))

valN = 0
sumN = 0
n = 1
while n <= numN:
    if n == 1:
        valN = numA
        sumN += valN
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valN += dNum
    sumN += valN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print()
print('{}번째 항까지의 합: {}'.format(numN, sumN))
print()

# 간단한 방법
valueN = numA + (numN - 1) * dNum
totalN = numN * (numA + valueN) / 2
print('{}번째 항까지의 합: {}'.format(numN, int(totalN)))