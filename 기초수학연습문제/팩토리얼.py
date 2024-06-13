# 팩토리얼 프로그램을 만들되, 
# 반복문을 이용한 함수와 재귀 함수를 이용해서 구현해보고, 
# python에서 제공하는 모듈도 사용

# 반복문
def facFunFor(n):

    fac = 1
    for n in range (1, (n + 1)):
        fac *= n

    return fac

num = int(input('num: '))
print(f'(반복문) {num}!: {facFunFor(num)}')

# 재귀 함수
def facFunIf(n):

    if n == 1:
        return n

    return n * facFunIf(n - 1)

print(f'(재귀함수) {num}!: {facFunIf(num)}')

import math

math.factorial(num)
print(f'(math모듈) {num}!: {math.factorial(num)}')