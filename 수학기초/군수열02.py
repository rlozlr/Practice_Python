num = int(input('n항 입력: '))

flag = True
n = 1;
cnt = 1;
searchNc = 0
searchNp = 0
while flag:
    for i in range(1, (n + 1)):
        if i == n:
            print('{}/{} '.format(i, (n - i + 1)), end='')
        else:
            print('{}/{} '.format(i, (n - i + 1)), end='')

        cnt += 1
        if (cnt > num):
            searchNc = i
            searchNp = n - i + 1
            flag = False
            break

    print()
    n += 1

print('{}항: {}/{}'.format(num, searchNc, searchNp))