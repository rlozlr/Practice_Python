# 1부터 100까지의 난수 10개를 생성하고, 다음의 요구사항을 만족하는 모듈 만들기
'''
1) 퀵 정렬 Algorithm을 이용한 난수 정렬 모듈 구현
2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가
'''

def qSort(ns, asc=True):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallNums = []; sameNums = []; bigNums = []

    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    if asc:
        return qSort(smallNums, asc=asc) + sameNums + qSort(bigNums, asc=asc)
    else:
        return qSort(bigNums, asc=asc) + sameNums + qSort(smallNums, asc=asc)
