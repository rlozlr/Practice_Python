# calculator() 함수를 선언하고 calculator() 안에 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 선언

def calculator(num1, num2, op):

    def add():
        print(f'sum: {num1 + num2}')

    def sub():
        print(f'sub: {num1 - num2}')
    def mul():
        print(f'mul: {num1 * num2}')
    def div():
        print(f'div: {num1 / num2}')

    if op == 1:
        add()
    elif op == 2:
        sub()
    elif op == 3:
        mul()
    elif op == 4:
        div()

while True:
    num1 = float(input('실수(n) 입력: '))
    num2 = float(input('실수(n) 입력: '))
    op = int(input('1. 덧셈 \t 2. 뺄셈 \t 3. 곱셈 \t 4. 나눗셈 \t 5. 종료 >>> '))

    if op == 5:
        print('****프로그램을 종료합니다.****')
        break

    calculator(num1, num2, op)