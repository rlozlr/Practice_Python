# 다음 수열의 일반항을 구하고, n항의 값 출력
'''
{2, 5, 11, 20, 32, 47, 65, 86, 110, 137, 167, ...}
'''
# a_n = (3n^2 - 2n + 4) / 2
numA1 = int(input('a1입력: '))
numN = int(input('an입력: '))

valN = ((3 * numN ** 2) - (3 * numN) + 4) / 2
print('an의 {}번째 항의 값: {}'.format(numN, int(valN)))