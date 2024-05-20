num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

tmp1 = num1
tmp2 = num2

# y, (x % y)
while tmp2 > 0:
    tmp = tmp2
    tmp2 = tmp1 % tmp2
    tmp1 = tmp

print('{}, {}의 최대공약수: {}'.format(num1, num2, tmp1))

for n in range(1, (tmp1 + 1)):
    if tmp1 % n == 0:
        print('{}, {}의 공약수: {}'.format(num1, num2, n))
