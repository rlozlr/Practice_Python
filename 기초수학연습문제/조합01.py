# python을 이용해서 9C4, 6C2 조합들의 값 구하기
numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

resultP = 1
resultR = 1
resultC = 1

for n in range(numN, (numN - numR), -1):
    resultP = resultP * n
print('resultP: {}'.format(resultP))

for n in range(numR, 0, -1):
    resultR = resultR * n
print('resultR: {}'.format(resultR))

resultC = int(resultP / resultR)
print('resultC: {}'.format(resultC))
