
# 다음 순열들의 값 구하기
'''
_9P_4, _6P_2
'''
numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))
result = 1

for n in range(numN, (numN - numR), -1):
    print('n: {}'.format(n))
    result = result * n

print('result: {}'.format(result))