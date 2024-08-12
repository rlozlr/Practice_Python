import 재귀02 as mod

num1 = int(input(f'첫번째 숫자 입력:'))
num2 = int(input(f'두번째 숫자 입력:'))

ns = mod.NumsSum(num1, num2)
result = ns.sumBetweenNums()
print(f'result: {result}')