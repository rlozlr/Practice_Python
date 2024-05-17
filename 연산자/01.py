'''
상품 가격과 지불 금액을 입력하면 거스름 돈을 계산하는 프로그램
단, 거스름 돈은 지폐와 동전의 개수를 최소로 하고, 1원단위 절사한다.
'''

cnt50000, cnt10000, cnt5000, cnt1000, cnt500, cnt100, cnt10 = 0, 0, 0, 0, 0, 0, 0

price = int(input('상품 가격 입력: '))
pay = int(input('지불 금액: '))

if pay > price:
    changeMoney = pay - price
    changeMoney = (changeMoney // 10) * 10
    print('거스름 돈: {}(원단위 절사)'.format(changeMoney))
    print('*' * 20)

if changeMoney > 50000:
    cnt50000 = changeMoney // 50000
    changeMoney %= 50000

if changeMoney > 10000:
    cnt10000 = changeMoney // 10000
    changeMoney %= 10000

if changeMoney > 5000:
    cnt5000 = changeMoney // 5000
    changeMoney %= 5000

if changeMoney > 1000:
    cnt1000 = changeMoney // 1000
    changeMoney %= 1000

if changeMoney > 500:
    cnt500 = changeMoney // 500
    changeMoney %= 500

if changeMoney > 100:
    cnt100 = changeMoney // 100
    changeMoney %= 100

if changeMoney > 10:
    cnt10 = changeMoney // 10
    changeMoney %= 10

print('50,000 {}장'.format(cnt50000))
print('10,000 {}장'.format(cnt10000))
print('5,000 {}장'.format(cnt5000))
print('1,000 {}장'.format(cnt1000))
print('500 {}장'.format(cnt500))
print('100 {}장'.format(cnt100))
print('10 {}장'.format(cnt10))
print('*' * 20)