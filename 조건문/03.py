'''
미세먼지 비상저감조치로 차량 운행제한 프로그램 만들기

    - 미세먼지 측정 수치가 150이하면 차량 5부제 실시
    - 미세먼지 측정 수치가 150을 초과하면 차량 2부제 실시
    - 차량 2부제를 실시하더라도 영업용차량은 5부제 실시
    - 미세먼지 수치, 차량 종류, 차량 번호를 입력하면 운행 가능 여부 출력
'''

import datetime

today = datetime.datetime.today()
day = today.day
limitDust = 150
dustNum = int(input('미세먼지 수치 입력: '))
carType = int(input('1.승용자 | 2. 영업용차 >>> '))
carNum = int(input('차량 번호 입력: '))

print('*' * 50)
print(today)
print('*' * 50)
if dustNum > limitDust and carType == 1:
    if (day % 2) == (carNum % 2):
        print('차랑 2부제 적용')
        print('차랑 2부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dustNum > limitDust and carType == 2:
    if (day % 5) == (carNum % 5):
        print('차랑 5부제 적용')
        print('차랑 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dustNum <= limitDust:
    if (day % 5) == (carNum % 5):
        print('차랑 5부제 적용')
        print('차랑 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')
print('*' * 50)