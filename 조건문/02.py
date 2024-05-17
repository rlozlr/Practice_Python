# 난수를 이용해서 가위, 바위, 보 게임

import random

comNum = random.randint(1, 3)
userNum = int(input('1. 가위 | 2. 바위 | 3. 보 (숫자입력) >>> '))

if ((comNum == 1 and userNum == 2) or
        (comNum == 2 and userNum == 3) or
        (comNum == 3 and userNum == 1)):
    print('컴퓨터는 {}번! '.format(comNum), end='')
    print('컴퓨터 패!')
elif comNum == userNum:
    print('컴퓨터는 {}번! '.format(comNum), end='')
    print('무승부!!')
else:
    print('컴퓨터는 {}번! '.format(comNum), end='')
    print('컴퓨터 승!')