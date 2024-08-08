# 새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서로 줄 세워 보자.
# 학생들의 키는 random  모듈을 이용해서 170 ~ 185 사이로 생성
import copy

def bubbleSort(cns, deepCopy=True):
    if deepCopy:
        cns = copy.copy(cns)
    else:
        cns = cns
    length = len(cns) - 1

    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                cns[j], cns[j + 1] = cns[j + 1], cns[j]

    return cns