inputNum = int(input("0보다 큰 정수 입력: "))

for num in range(1, (inputNum + 1)):
    if inputNum % num == 0:
        print('{}의 약수: {}'.format(inputNum, num))
