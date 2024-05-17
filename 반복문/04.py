'''
톱니가 각각 n1개와 n2개의 톱니바퀴가 서로 맞물려 회전할 때, 
회전을 시작한 후 처음 맞물린 톱니가 최초로 다시 만나게 될 때까지의 톱니의 수와 각각의 바퀴 회전수를 출력
(단, n2는 n1보다 크다.)

> 최소 공배수 문제
'''

gearA_cnt = int(input('GearA 톱니수 입력: '))
gearB_cnt = int(input('GearB 톱니수 입력: '))

gearA_circle, gearB_circle, num = 0, 0, 0
flag = True

while flag:

    if gearA_circle != 0:
        if gearA_circle != num:
            gearA_circle += gearA_cnt
        else:
            flag = False
    else:
        gearA_circle += gearA_cnt

    if gearB_circle != 0 and gearB_circle % gearA_cnt == 0:
        num = gearB_circle
    else:
        gearB_circle += gearB_cnt

print('최초로 다시 만나게 될 때: {}톱니'.format(num))
print('GearA 회전수: {}회전'.format(int(num / gearA_cnt)))
print('GearB 회전수: {}회전'.format(int(num / gearB_cnt)))
