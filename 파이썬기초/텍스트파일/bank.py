import time

def getTime():
    lt = time.localtime()
    st =time.strftime('%Y-%m-%d %H:%M:%S')
    return st

while True:
    selectNum = int(input('1.입금 | 2.출금 | 3.종료 \t'))

    if selectNum == 1:
        money = int(input('입금액 입력: '))
        with open ('C:/pythonEx/bank/money.txt', 'r') as f:
            m = f.read()

        with open('C:/pythonEx/bank/money.txt', 'w') as f:
            f.write(str(int(m) + money))

        memo = input('입금 내역 입력: ')
        with open('C:/pythonEx/bank/poketMoneyRegister.txt', 'a') as f:
            f.write('-------------------------------------')
            f.write(f'{getTime()} \n')
            f.write(f'[입금] {memo} : {str(money)}원\n')
            f.write(f'[잔액] : {str(int(m) + money)}원\n')

        print('입금 완료~!!')
        print(f'기존 잔액: {m}')
        print(f'입금 후 잔액: {int(m) + money}')
    
    elif selectNum == 2:
        money = int(input('출금액 입력: '))
        with open ('C:/pythonEx/bank/money.txt', 'r') as f:
            m = f.read()

        with open('C:/pythonEx/bank/money.txt', 'w') as f:
            f.write(str(int(m) - money))

        memo = input('출금 내역 입력: ')
        with open('C:/pythonEx/bank/poketMoneyRegister.txt', 'a') as f:
            f.write('-------------------------------------')
            f.write(f'{getTime()} \n')
            f.write(f'[출금] {memo} : {str(money)}원\n')
            f.write(f'[잔액] : {str(int(m) - money)}원\n')

        print('츨금 완료~!!')
        print(f'기존 잔액: {m}')
        print(f'츨금 후 잔액: {int(m) - money}')

    elif selectNum == 3:
        print('bye~!!')
        break