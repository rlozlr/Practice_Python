
# 다음 수열의 일반항을 구하고 n번째 항의 값과 합을 구하기
'''
{2, 6, 18, 54, 162, 486, 1458, 4374, 13122, ...}
등차수열의 일반항 : a_n = a_1 *  r^(n - 1)
등차수열의 합 : S_n = a_1 * (1 - r^n) / (1 - r)
'''
numA1 = int(input('a1 입력: '))
numR = int(input('공차 입력: '))
numN = int(input('n 입력: '))

valN = 0; sumN = 0

# n = 1
# while n <= numN:
#
#     if n == 1:
#         valN = numA1
#         sumN += valN
#         print('{}번째 항의 값: {}'.format(n, valN))
#         print('{}번째 항까지의 합: {}'.format(n, sumN))
#         n += 1
#         continue
#
#     valN *= numR
#     sumN += valN
#     print('{}번째 항의 값: {}'.format(n, valN))
#     print('{}번째 항까지의 합: {}'.format(n, sumN))
#     n += 1
#
# print('{}번째 항의 값: {}'.format(numN, valN))
# print('{}번째 항까지의 합: {}'.format(numN, sumN))

# a_n = a_1 *  r^(n - 1)
valN = numA1 * (numR ** (numN - 1))
print('{}번째 항의 값: {}'.format(numN, valN))

# S_n = a_1 * (1 - r^n) / (1 - r)
sumN = numA1 * (1 - (numR ** numN)) / (1 - numN)
print('{}번째 항까지의 합: {}'.format(numN, int(sumN)))