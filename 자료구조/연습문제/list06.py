# 4개의 숫자 중 서로 다른 숫자 2개를 선택해서 만들 수 있는 모든 경우의 수를 출력

numbers = [4, 6, 7, 9]
result1 = []

for num1 in numbers:
    for num2 in numbers:
        if num1 == num2:
            continue

        result1.append([num1, num2])

print(f'result : {result1}')
print(f'result length : {len(result1)}')

# n! / (n-r)!
import math
pernutation = math.factorial(len(numbers)) / math.factorial(len(numbers) - 2)
print(f'pernutation : {pernutation}')