num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
num3 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        maxNum = i

minNum = (num1 * num2)  // maxNum
newMin = minNum
for i in range(1, (newMin + 1)):
    if newMin % i == 0 and num3 % i == 0:
        maxNum = i

minNum = (newMin * num3) // maxNum
print('{}, {}, {}의 최소공배수: {}'.format(num1, num2, num3, minNum))