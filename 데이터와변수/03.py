import datetime

today = datetime.datetime.today()
age = input('나이: ')
if age.isdigit():
    afterYear = 100 - int(age)
    beHundred = today.year + afterYear

    print('{}년 ({}년 후에) 100살이 됩니다.'.format(beHundred, afterYear))
else:
    print('잘못된 입력입니다.')