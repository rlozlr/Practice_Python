# 공원 입장료를 나타낸 표
'''
구분      영유아     어린이     청소년     성인       어르신
나이      0~7세      8~13세     14~19세    20~64세    65세 이상
요금      무료       200        300        500        무료
'''
# 1일 총 입장객이 100명이라고 할 때, 1일 전체 입장 요금을 구하기
# 단, 입장 고객의 나이는 난수를 이용 (0~100)
import random

visitors = []

for i in range(100):
    visitors.append(random.randint(0, 100))

baby, child, teenager, adult, senior = 0, 0, 0, 0, 0

for age in visitors:
    if age > 0 and age <= 7:
        baby += 1
    elif age > 7 and age < 14:
        child += 1
    elif age > 13 and age < 20:
        teenager += 1
    elif age > 19 and age < 65:
        adult += 1
    else:
        senior += 1

babyPrice, seniorPrice = 0, 0
childPrice = child * 200
teenagerPrice = teenager * 300
adultPrice = adult * 500
print('----     1일 전체 입장 요금     ----')
print('영유아 {}명 : {}원'.format(baby, babyPrice))
print('어린이 {}명 : {}원'.format(child, childPrice))
print('청소년 {}명 : {}원'.format(teenager, teenagerPrice))
print('어  른 {}명 : {}원'.format(adult, adultPrice))
print('어르신 {}명 : {}원'.format(senior, seniorPrice))
print('-----------------------------------')
print('Total Visitor : {}명'.format(baby + child + teenager + adult + senior))
print('Total Price : {}원'.format(childPrice + teenagerPrice + adultPrice + seniorPrice))


