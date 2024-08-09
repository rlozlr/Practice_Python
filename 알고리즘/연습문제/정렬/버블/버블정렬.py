# 숫자로 이루어진 List를 버블정렬 Algorithm을 이용해서 오름차순과 내림차순으로 정렬하는 모듈 만들기
# 단, 정렬하는 과정도 출력
import copy

def sortByBubbleAlgorithm(ns, asc=True):
    c_ns = copy.copy(ns)

    length = len(c_ns) - 1
    for i in range(length):
        for j in range(length - 1):

            if asc :
                if c_ns[j] > c_ns[j + 1]:
                    c_ns[j], c_ns[j + 1] = c_ns[j + 1], c_ns[j]
            else:
                if c_ns[j] < c_ns[j + 1]:
                    c_ns[j], c_ns[j + 1] = c_ns[j + 1], c_ns[j]

            print(f'ns: {c_ns}')
        print()

    return c_ns