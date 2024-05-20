# 약수
inputNum = int(input('0보다 큰 정수 입력: '))

divisor = []
for num in range(1, (inputNum + 1)):
    if inputNum % num == 0:
        divisor.append(num)

if len(divisor) > 0:
    try:
        with open('C:/pythonEx/divisor.txt', 'a') as f:
            f.write(f'{inputNum}의 약수: ')
            f.write(f'{divisor}\n')
    except Exception as e:
        print(e)
    else:
        print('divisor write complete!!')

# 소수
inputNum2 = int(input('0보다 큰 정수 입력: '))
prime = []
for num2 in range(2, (inputNum2 + 1)):
    flag = True
    for n in range(2, num2):
        if num2 % n == 0:
            flag = False
            break
    if flag:
        prime.append(num2)

if len(prime) > 0:
    try:
        with open('C:/pythonEx/prime.txt', 'a') as f:
            f.write(f'{inputNum2}까지의 소수: ')
            f.write(f'{prime}\n')
    except Exception as e:
        print(e)
    else:
        print('prime write complete~!!')