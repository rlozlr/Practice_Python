# 숫자로 이루어진 List를 병합정렬 Algorithm을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
# 단, 정렬하는 과정도 출력

def mergeSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mergeSort(ns[0:midIdx], asc=asc)
    rightNums = mergeSort(ns[midIdx:len(ns)], asc=asc)

    mergeNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if asc:
            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

        else:
            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergeNums += leftNums[leftIdx:]
    mergeNums += rightNums[rightIdx:]

    print(f'mergeNums: {mergeNums}')
    return mergeNums