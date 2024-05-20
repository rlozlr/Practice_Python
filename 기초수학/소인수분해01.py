inputNum = int(input('1보다 큰 정수 입력: '))

n = 2
while n <= inputNum:
    if inputNum % n == 0:
        print('소인수: {}'.format(n))
        inputNum /= n
    else:
        n += 1
