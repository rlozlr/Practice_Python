num = int(input('n 입력: '))

# 반복문 이용1 - for
result = 1
for n in range(1, num + 1):
    result *= n

print('for를 이용해 {} 팩토리얼 구하기: {}'.format(num, result))
print()

# 반복문 이용2 - while
result = 1
n = 1
while n <= num:
    result *= n
    n += 1

print('while을 이용해 {} 팩토리얼 구하기: {}'.format(num, result))
print()

# 재귀함수 이용
def factorialFun(n):
    if n == 1: return 1

    return n * factorialFun(n - 1)
print('재귀함수를 이용해 {} 팩토리얼 구하기: {}'.format(num, factorialFun(num)))
print()

# 모듈 사용 - math
import math
print('모듈을 이용해 {} 팩토리얼 구하기: {}'.format(num, math.factorial(num)))


