# 100부터 1000 사이의 2개의 난수에 대해서 공약수와 최대공약수를 출력하고, 서로소인지 출력
'''
12의 약수 -> 1, 2, 3, 4, 6, 12
20의 약수 -> 1, 2, 4, 5, 10, 20
공약수 -> 1, 2, 4
최대공약수 -> 4
'''
import random

rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

print(f'rNum1: {rNum1}')
print(f'rNum2: {rNum2}')

maxNum = 0
for n in range(1, (min(rNum1, rNum2)+1)):
    if rNum1 % n == 0 and rNum2 % n == 0:
        print(f'공약수: {n}')
        maxNum = n

print(f'최대공약수: {maxNum}')

if maxNum == 1:
    print(f'{rNum1}과 {rNum2}는 서로소이다.')