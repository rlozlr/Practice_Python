numA1 = int(input('a1 입력: '))
numAn = int(input('an 입력: '))
numB1 = int(input('b1 입력: '))
numBd = int(input('bn 공차 입력: '))

valA = 0
valB = 0

n = 1
while n <= numAn:

    if n == 1:
        valA = numA1
        valB = numB1
        print('an의 {}번째 항의 값: {}'.format(n, valA))
        print('bn의 {}번째 항의 값: {}'.format(n, valB))
        n += 1
        continue

    valA = valA + valB
    valB = valB + numBd
    print('an의 {}번째 항의 값: {}'.format(n, valA))
    print('bn의 {}번째 항의 값: {}'.format(n, valB))
    n += 1

print()
print('an의 {}번째 항의 값: {}'.format(numAn, valA))
print('bn의 {}번째 항의 값: {}'.format(numAn, valB))
print()

# 간단한 방법
valueAn = numAn ** 2 + numAn + 1
print('an의 {}번째 항의 값: {}'.format(numAn, valueAn))

