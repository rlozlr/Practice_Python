'''
집 앞 버스 정류장에서 학교까지 가는 버스 A, B, C의 운행정보가 다음과 같을 때,
2대 이상의 버스가 정차하는 시간대를 출력

1. 버스 A, B 운행 정보
    - 오전 6시 첫 차: 오후 23시 운행 종료
    - 버스A : 15분 간격 운행
    - 버스B : 13분 간격 운행
    
2. 버스 c 운행 정보
    - 6시 20분 첫 차: 오후 22시 운행 종료
    - 버스C : 8분 간격 운행
'''

busA = 15
busB = 13
busC = 8

totalMin = 60 * 17 # 총 17시간 운행
for i in range(totalMin + 1):
    if i < 20 or i > (totalMin - 60):
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차 : ', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour,min))
    else:
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차 : ', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour,min))
        elif i % busA == 0 and i % busC == 0:
            print('busA와 busC 동시 정차 : ', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour,min))
        elif i % busB == 0 and i % busC == 0:
            print('busB와 busC 동시 정차 : ', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour,min))