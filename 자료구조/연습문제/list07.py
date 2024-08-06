# 4개의 숫자 중 서로 다른 숫자 3개를 선택해서 만들 수 있는 모든 경우의 수를 출력
numbers = [4, 6, 7, 9]
result = []

for num1 in numbers:
    for num2 in numbers:
        if num1 == num2:
            continue

        for num3 in numbers:
            if num1 == num3 or num2 == num3:
                continue

            result.append([num1, num2, num3])

print(f'result : {result}')
print(f'result length : {len(result)}')

# n! / (n-r)!
import math
pernutation = math.factorial(len(numbers)) / math.factorial(len(numbers) - 3)
print(f'pernutation : {pernutation}')