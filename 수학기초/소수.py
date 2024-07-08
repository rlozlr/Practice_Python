inputNum = int(input("0보다 큰 정수 입력: "))

for num in range(2, (inputNum + 1)):
    flag = True

    for n in range(2, num):
        if num % n == 0:
            flag = False
            break
    if flag:
        print('{} : 소수'.format(num))
    else:
        print('{} : 합성수'.format(num))