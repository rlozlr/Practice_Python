# 다음 2개의 Tuple에 대해서 합집합(중복 없이)과 교집합 출력
tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

groupHap = list(tuple1 + tuple2)
groupGyo = list()

idx = 0
while True:
    if idx >= len(groupHap):
        break

    if groupHap.count(groupHap[idx]) >= 2:
        groupGyo.append(groupHap[idx])
        groupHap.remove(groupHap[idx])
        continue

    idx += 1

print(f'합집합 : {tuple(sorted(groupHap))}')
print(f'교집합 : {tuple(sorted(groupGyo))}')

