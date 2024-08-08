# 숫자로 이루어진 List에서 사용자가 입력한 숫자를 검색하는 모듈
'''
1) 검색 모듈은 이진 검색 Algorithm 이용
2) 리스트는 [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]를 이용
3) 검색 과정을 로그로 출력
4) 검색에 성공하면 해당 정수의 Index를 출력하고, 검색 결과가 없다면 -1을 출력
'''

def searchNumberByBinaryAlgorithm(ns, sn):

    searchResultIdx = -1

    startIdx = 0
    endIdx = len(ns) - 1
    midIdx = (startIdx + endIdx) // 2
    midVal = ns[midIdx]

    while sn >= ns[0] and sn <= ns[len(ns) - 1]:
        if sn == ns[len(ns) - 1]:
            searchResultIdx = len(ns) - 1
            break

        if startIdx + 1 == endIdx:
            if ns[startIdx] != sn and ns[endIdx] != sn:
                break

        if sn > midVal:
            startIdx = midIdx
            midIdx = (startIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'+startIdx: {startIdx}, endIdx: {endIdx}')
            print(f'+midIdx: {midIdx}, midVal: {midVal}')

        elif sn < midVal:
            endIdx = midIdx
            midIdx = (startIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'-startIdx: {startIdx}, endIdx: {endIdx}')
            print(f'-midIdx: {midIdx}, midVal: {midVal}')

        elif sn == midVal:
            searchResultIdx = midIdx
            break

    return searchResultIdx