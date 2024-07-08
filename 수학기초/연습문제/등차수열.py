# 다음 수열의 일반 항을 구하고 n번째 항의 값과 합을 구하기
'''
{4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 62}
등차수열의 일반항 : a_n = a_1 + (n - 1) * d
등차수열의 합 : S_n = n(a_1 + a_n) / 2
'''

numA1 = int(input('a1 입력: '))
numD = int(input('공차 입력: '))
numN = int(input('n 입력: '))

valN = 0; sumN = 0
#
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
#     valN += numD
#     sumN += valN
#     print('{}번째 항의 값: {}'.format(n, valN))
#     print('{}번째 항까지의 합: {}'.format(n, sumN))
#     n += 1
#
# print()
# print('{}번째 항의 값: {}'.format(numN, valN))
# print('{}번째 항까지의 합: {}'.format(numN, sumN))

# a_n = a_1 + (n - 1) * d
valN = numA1 + (numN - 1) * numD
print('{}번째 항의 값: {}'.format(numN, valN))

# S_n = n(a_1 + a_n) / 2
sumN = numN * (numA1 + valN) / 2
print('{}번째 항까지의 합: {}'.format(numN, int(sumN)))