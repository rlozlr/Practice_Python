# 숫자로 이루어진 List를 선택정렬 Algorithm을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력
import copy

def sortSelectAlgorithm(ns, asc=True):
    c_ns = copy.copy(ns)

    for i in range(len(c_ns) - 1):
        minIdx = i

        for j in range(i + 1, len(c_ns)):

            if asc:
                if c_ns[minIdx] > c_ns[j]:
                    minIdx = j
            else:
                if c_ns[minIdx] < c_ns[j]:
                    minIdx = j

        c_ns[i], c_ns[minIdx] = c_ns[minIdx], c_ns[i]
        print(f'nums: {c_ns}')

    return c_ns