# 다음 수열을 보고 수열의 합이 최초 100을 초과하는 n번째 항의 값과 n을 출력
'''
1/1, 1/2, 2/1, 1/3, 2/2, 3/1, 1/4, 2/3, 3/2, 4/1, 1/5, 2/4, ...
'''

flag = True
n = 1
nCnt = 1;
searchNC = 0;
searchNP = 0
total = 0
while flag:

    for i in range(1, (n + 1)):
        print('{}/{}'.format(i, (n - i + 1)), end=' ')

        total += i / (n - i + 1)
        nCnt += 1

        if total > 100:
            searchNC = i
            searchNP = n - i + 1
            flag = False
            break

    print()
    n += 1

print()
print('수열의 합이 최초 100을 초과: \n'
      '항: {}항\n값: {}/{}\n합: {}'.format(nCnt, searchNC, searchNP, total))
