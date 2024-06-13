# 100부터 1000사이의 난수를 소인수분해하고 각각의 소인수에 대한 지수를 출력하는 프로그램 만들기
'''
20의 소인수분해 -> 2 x 2 x 5 -> 2, 1
'''
import random

rNum = random.randint(100, 1000)
print(f'rNum: {rNum}')

soinsuList = []

n = 2
while n <= rNum:
    if rNum % n == 0:
        print(f'소인수: {n}')
        soinsuList.append(n)
        rNum /= n
    else:
        n += 1

print(f'soinsuList: {soinsuList}')

tempNum = 0
for s in soinsuList:
    if tempNum != s:
        print (f'{s}\'s count: {soinsuList.count(s)}')
        tempNum = s