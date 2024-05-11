'''
    - PC가 난수(1 ~ 1000)를 발생하면 사용자가 숫자(정수)를 입력한다
    - 사용자가 난수를 맞추면 게임이 종료된다.
    - 만약, 못 맞추게 되면 난수와 사용자 숫자의 크고 작음을 출력한 후 사용자한테 다시 기회를 준다.
    - 최종적으로 사용자가 시도한 횟수를 출력한다.
'''

import random

randomNum = random.randint(1, 1000)
tryCnt = 0
gameFlag = True

while gameFlag:
    tryCnt += 1
    userNum =int(input('1에서 1,000까지의 정수 입력: '))

    if randomNum == userNum:
        print('정답!')
        gameFlag = False
    else:
        if(randomNum > userNum):
            print('UP!')
        else:
            print('DOWN!')

print('난수: {}, 시도 횟수: {}'.format(randomNum, tryCnt))