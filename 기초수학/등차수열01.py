numA = int(input('a1 입력: '))
dNum = int(input('공차 입력: '))
numN = int(input('n 입력: '))

valN = 0
n = 1
while n <= numN:
    if n == 1:
        valN = numA
        print('{}번째 항의 값: {}'.format(n, valN))
        n += 1
        continue

    valN += dNum
    print('{}번째 항의 값: {}'.format(n, valN))
    n += 1

print()
print('{}번째 항의 값: {}'.format(numN, valN))
print()

# 간단한 방법
valueN = numA + (numN - 1) * dNum
print('{}번째 항의 값: {}'.format(numN, valueN))