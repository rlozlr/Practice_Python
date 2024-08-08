import random
import 최빈값 as ms

scores = []

for i in range(100):
    rn = random.randint(71, 100)
    if rn != 100: rn = rn - (rn % 5)
    scores.append(rn)

print(f'scores: {scores}')
print(f'scores length: {len(scores)}')

# 최댓값 알고리즘
maxAlgo = ms.MaxAlgorithm(scores)
maxAlgo.setMaxNumIdxAndNum()
maxNum = maxAlgo.getMaxNum()
print(f'maxNum: {maxNum}')

# Index List 생성
idxs = [0 for i in range(maxNum + i)]
print(f'idxs: {idxs}')
print(f'idxs length: {len(idxs)}')

# Index List에 빈도 저장
for n in scores:
    idxs[n] = idxs[n] + 1

print(f'idxs: {idxs}')

n = 1
while True:
    maxAlgo = ms.MaxAlgorithm(idxs)
    maxAlgo.setMaxNumIdxAndNum()
    maxNum = maxAlgo.getMaxNum()
    maxNumIdx = maxAlgo.getMaxNumIdx()
    # print(f'maxNum : {maxNum}')
    # print(f'maxNumIdx: {maxNumIdx}')

    if maxNum == 0:
        break

    print(f'{n}. {maxNumIdx}빈도수: {maxNum}\t', end='')
    print('+' * maxNum)

    idxs[maxNumIdx] = 0

    n += 1

