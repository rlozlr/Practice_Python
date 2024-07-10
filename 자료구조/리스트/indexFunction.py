# 1부터 10까지의 정수가 중복되지 않고 섞여 있을 때 행운의 숫자 7의 위치 찾기
import random
randomList = random.sample(range(1, 11), 10)
selectIdx = input('7의 위치: ')
it = randomList.index(7)

if it == selectIdx:
    print('정답~!!')
else:
    print('꽝~!!')

print(randomList)
print('7의 위치: {}'.format(it))