# 사용자가 입력한 숫자에 대한 소수를 구하고 이를 파일에 작성
uri = 'C:/pythonEx/'

def writeNum(n):
    file = open(uri + 'num.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()

inputNum = int(input("0보다 큰 정수 입력 >>> "))
for num in range (2, (inputNum + 1)):
    flag = True
    for n in range(2, num):
        if num % n == 0:
            flag = False
            break

    if flag:
        writeNum(num)

