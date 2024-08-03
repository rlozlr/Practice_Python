# 컴퓨터가 1부터 10까지 5개의 난수를 생성한 후, 사용자가 입력한 숫자가 있는지 또는 없는지 출력
import random

randomNum = random.sample(range(1, 11), 5)
userNum = int(input('숫자 입력: '))

if userNum in randomNum:
    print('randomNum: {}'.format(randomNum))
    print('정답~!!')
else:
    print('randomNum: {}'.format(randomNum))
    print('꽝~!!')

