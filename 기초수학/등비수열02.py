numA = int(input('a1 입력: '))
numR = int(input('공비 입력: '))
numN = int(input('n 입력: '))

valN = 0
sumN = 0
n = 1
while n <= numN:
    if n == 1:
        valN = numA
        sumN += valN
        print('{}번째 항의 값: {}'.format(n, sumN))
        n += 1
        continue

    valN *= numR
    sumN += valN
    print('{}번째 항의 값: {}'.format(n, sumN))
    n += 1

print()
print('{}번째 항의 값: {}'.format(numN, sumN))
print()

# 간단한 방법
totalN = numA * (1 - (numR ** numN)) / (1 - numR)
print('{}번째 항까지의 합: {}'.format(numN, int(totalN)))