# 하루에 몸무게(kg)와 신장(m)이 각각 -0.3kg, +0.001m씩 변한다고 할 때, 30일 후의 몸무게와 신장의 값을 저장하고 BMI 값도 출력
# (현재 신체정보는 아래의 딕셔너리에 저장)

bodyInfo = {'이름' : '루피', '몸무게' : 65.0, '신장' : 1.74}
myBMI = bodyInfo['몸무게'] / (bodyInfo['신장'] ** 2)
print(f'bodyInfo : {bodyInfo}')
print(f'myBMI : {round(myBMI, 2)}')

date = 0
while True:
    date += 1
    print('D + {}'.format(date))

    bodyInfo['몸무게'] = round((bodyInfo['몸무게'] - 0.3), 2)
    print('몸무게 : {}'.format(bodyInfo['몸무게']))

    bodyInfo['신장'] = round((bodyInfo['신장'] + 0.001), 3)
    print('신장 : {}'.format(bodyInfo['신장']))

    myBMI = bodyInfo['몸무게'] / (bodyInfo['신장'] ** 2)
    print()

    if date >= 30:
        break

print(f'bodyInfo : {bodyInfo}')
print(f'myBMI : {round(myBMI, 2)}')
