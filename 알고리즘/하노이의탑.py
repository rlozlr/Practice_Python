# Python을 이용해서 하노이의 탑 게임 진행 과정을 출력
'''
* 한 번에 한 개의 원판만 옮길 수 있다.
* 큰 원판이 작은 원판 위에 있어서는 안 된다.
'''

#원판개수, 출발기둥, 도착기둥, 경유기둥
def moveDisk(diskNo, startBar, endBar, tempBar):
    if diskNo == 1:
        print(f'{diskNo}disk {startBar}에서 {endBar}(으)로 이동~!!')

    else:
        # (diskNo - 1)개들을 경유 기둥으로 이동
        moveDisk(diskNo-1, startBar, tempBar, endBar)

        # diskNo를 목적 기둥으로 이동
        print(f'{diskNo}disck를 {startBar}에서 {endBar}(으)로 이동~!!')

        # (diskNo - 1)개들을 도착 기둥으로 이동
        moveDisk(diskNo-1, tempBar, endBar, startBar)

moveDisk(3, 1, 3, 2)
