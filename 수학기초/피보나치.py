numN = int(input('n 입력: '))

valN = 0
sumN = 0
valPreN2 = 0
valPreN1 = 0

n = 1
while n <= numN:
    if n == 1 or n == 2:
        valN = 1
        valPreN2 = valN
        valPreN1 = valN
        sumN += valN
        n += 1

    else:
        valN = valPreN2 + valPreN1
        valPreN2 = valPreN1
        valPreN1 = valN
        sumN += valN
        n += 1

print('{}번째 항의 값: {}'.format(numN, valN))
print('{}번째 항까지의 값: {}'.format(numN, sumN))
