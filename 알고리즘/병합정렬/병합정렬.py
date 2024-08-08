# 1부터 100까지의 난수 10개를 생성하고, 다음의 요구사항을 만족하는 모듈 만들기
'''
1) 병합 정렬 Algorithm을 이용한 난수 정렬 모듈 구현
2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가
'''

def mSort(ns, asc=True):
        if len(ns) < 2:
            return ns

        midIdx = len(ns) // 2
        leftNums = mSort(ns[0:midIdx], asc=asc)
        rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

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

        mergeNums = mergeNums + leftNums[leftIdx:]
        mergeNums = mergeNums + rightNums[rightIdx:]

        return mergeNums

