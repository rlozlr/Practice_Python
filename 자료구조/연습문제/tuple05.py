# Tuple 과일 개수에 대해서 오름차순 및 내림차순으로 정렬
fruits = ({'수박':8}, {'포도':13}, {'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
print(fruits)

fruits = list(fruits)

curIdx = 0; nextIdx = 1
endIdx = len(fruits) - 1

flag = True
while flag:
    curDic = fruits[curIdx]
    nextDic = fruits[nextIdx]

    curDicCnt = list(curDic.values())[0]
    nextDicCnt = list(nextDic.values())[0]

    if nextDicCnt < curDicCnt:
        fruits.insert(curIdx, fruits.pop(nextIdx))
        nextIdx = curIdx + 1
        continue

    nextIdx += 1
    if nextIdx > endIdx:
        curIdx += 1
        nextIdx = curIdx + 1

        if curIdx == 5:
            flag = False

print(f'오름차순 : {tuple(fruits)}')

fruits = sorted(fruits, key=lambda x: list(x.values())[0], reverse=True)
print(f'내림차순 : {tuple(fruits)}')
