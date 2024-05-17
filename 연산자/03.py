'''
금액, 이율, 거치기간을 입력하면 복리계산하는 복리계산기 프로그램
'''

money = int(input('금액 입력: '))
rate = float(input('이율 입력: '))
term = int(input('기간 입력: '))

targetMoney = money

for i in range(term):
    targetMoney += (targetMoney * rate * 0.01)

targetMoneyFormated = format(int(targetMoney), ',')     #format(숫자, ',') => 숫자를 천 단위로 쉼표(,)를 포함하여 포맷

print('*' * 20)
print('이율: {}원'.format(rate))
print('원금: {:,}'.format(money))     # {:,} => 숫자를 천 단위로 쉼표(,)를 포함하여 포맷
print('{}년 후 금액: {}원'.format(term, targetMoneyFormated))
print('*' * 20)