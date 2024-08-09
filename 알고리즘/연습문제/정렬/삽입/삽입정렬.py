# 숫자로 이루어진 List를 삽입정렬 Algorithm을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력
import copy

def sortInsertAlgorithm(ns, asc=True):
    c_ns = copy.copy(ns)

    for i1 in range(1, len(c_ns)):
        i2 = i1 - 1
        c_Num = c_ns[i1]

        if asc:
            while c_ns[i2] < c_Num and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        else:
            while c_ns[i2] <= c_Num and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        c_ns[i2 + 1] = c_Num
        print(f'c_ns: {c_ns}')

    return c_ns