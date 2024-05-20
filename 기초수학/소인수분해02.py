inputNum = int(input('1보다 큰 정수 입력: '))

n = 2
searchNum = []
while n <= inputNum:
    if inputNum % n == 0:
        print('소인수: {}'.format(n))
        if searchNum.count(n) == 0:
            searchNum.append(n)
        elif searchNum.count(n) == 1:
            searchNum.remove(n)
        inputNum /= n
    else:
        n += 1

print('searchNum: {}'.format(searchNum))
