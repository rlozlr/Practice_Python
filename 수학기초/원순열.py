n = int(input('인원 : '))
result = 1
for i in range(1, n):
    result *= i

print('result : {}'.format(result))