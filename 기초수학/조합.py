numN = int(input('numN : '))
numR= int(input('numR : '))
resultP = 1
resultR = 1
resultC = 1

for n in range(numN, (numN - numR), -1):
    print('n : {}'.format(n))
    resultP = resultP * n

print('resultP: {}'.format(resultP))

for n in range(numR, 0, -1):
    print('n : {}'.format(n))
    resultR = resultR * n

print('resultR: {}'.format(resultR))

resultC = int(resultP / resultR)
print('resultC: {}'.format(resultC))

result = (1/resultC * 100)
print('{}%'.format(round(result, 2)))