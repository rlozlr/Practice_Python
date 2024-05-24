num = int(input('n항 입력: '))

flag = True
n = 1
cnt = 1
searchN = 0
while flag:
    # 군
    for i in range(1, (n + 1)):
        if i == n:
            print('{}'.format(i), end='')
        else:
            print('{}'.format(i), end='')

        cnt += 1
        if (cnt > num):
            searchN = i
            flag = False
            break

    print()
    n += 1

print('{}항: {}'.format(num, searchN))