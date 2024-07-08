# 1일 차에 쌀 두 톨을 받고, 2일 차부터는 하루 전의 2배에 해당하는 쌀을 받는다고 할 때,
# 30일 째 되는 날 받게 되는 쌀의 개수를 수열과 시그마로 나타내고 이를 출력
'''
{2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...}
'''
numA1 = int(input('a1 입력: '))
numR = int(input('공비 입력: '))
numN = int(input('n 입력: '))

valN = 0; sumN = 0
# n = 1
# while n <= numN:
#
#     if n == 1:
#         valN = numA1
#         sumN += valN
#         print('{}번째 항까지의 합: {}'.format(n, sumN))
#         n += 1
#         continue
#
#     valN *= numR
#     sumN += valN
#     print('{}번째 항까지의 합: {}'.format(n, sumN))
#     n += 1
#
# print('{}번째 항까지의 합: {}'.format(numN, format(sumN, ',')))

# S_n = a_1 * (1 - r^n) / (1 - r)
sumN = numA1 * (1 - (numR ** numN)) / (1 - numR)
print('{}번째 항까지의 합: {}'.format(numN, format(sumN, ',')))