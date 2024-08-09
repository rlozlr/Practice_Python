# 숫자로 이루어진 List에서 아이템의 순위를 출력하고, 순위에 따라 아이템을 정렬하는 모듈 만들기
# List는 50부터 100까지의 난수 20개 이용

def rankAlgorithm(ns):
    ranks = [0 for i in range(len(ns))]

    for idx, n1 in enumerate(ns):
        for n2 in ns:
            if n1 < n2:
                ranks[idx] += 1

    print(f'nums: {ns}')
    print(f'ranks: {ranks}')

    for i, n in enumerate(ns):
        print(f'nums: {n} \t rank:{ranks[i] + 1}')

    sortedNums = [0 for n in range(len(ns))]

    for idx, rank in enumerate(ranks):
        sortedNums[rank] = ns[idx]

    return sortedNums