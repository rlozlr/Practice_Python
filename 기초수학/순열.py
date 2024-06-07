numN = int(input('numN : '))
numR= int(input('numR : '))
result = 1

for n in range(numN, (numN - numR), -1):
    print('n : {}'.format(n))
    result = result * n

print('result: {}'.format(result))