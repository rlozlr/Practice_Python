# 카드 7장을 일렬로 나열하되 2, 4, 7번 카드가 서로 이웃하도록 나열하는 모든 경우의 수
'''
1, 2, 3, 4, 5, 6, 7
'''

# factorialNum1 = int(input('factorial1 입력: '))
# result1 = 1
#
# for n in range(factorialNum1, 0 , -1):
#     result1 *= n
# print('result1: {}'.format(result1))
#
# factorialNum2 = int(input('factorial2 입력: '))
# result2 = 1
#
# for n in range(factorialNum2, 0 , -1):
#     result2 *= n
# print('result2: {}'.format(result2))
#
# print('모든 경우의 수 : {}'.format(result1 * result2))

import math

num1 = int(input('num1 입력: '))
print('{}의 factorial: {}'.format(num1, math.factorial(num1)))
num2 = int(input('num2 입력: '))
print('{}의 factorial: {}'.format(num2, math.factorial(num2)))
print('모든 경우의 수 : {}'.format(math.factorial(num1) * math.factorial(num2)))
