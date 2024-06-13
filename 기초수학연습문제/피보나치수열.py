# 피보나치수열에서 n항의 값과 n항까지의 합 출력
'''
{1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...}
'''
num = int(input('n 입력: '))
val = 0; total = 0

valPreN2 = 0; valPreN1 = 0

n = 1
while n <= num:
    if n == 1 or n == 2:
        val = 1
        valPreN2 = val
        valPreN1 = val
        total += val
        n += 1

    else:
        val = valPreN2 + valPreN1
        valPreN2 = valPreN1
        valPreN1 = val
        total += val
        n += 1

print('{}번째 항의 값: {}'.format(num, val))
print('{}번째 항까지의 합: {}'.format(num, total))