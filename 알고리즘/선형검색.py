nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
# 1. List에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(Index)를 출력
searchData = int(input('숫자: '))
searchResultIdx = -1

n = 0
while True:
    if nums[n] == searchData:
        if n != len(nums) -1:
            searchResultIdx = n
        break

    n += 1

print('---------- #1 ----------')
print(f'nums : {nums}')
print(f'nums length: {len(nums)}')
print(f'searchResultIdx : {searchResultIdx}')

# 2. List에서 숫자 '7'을 모두 검색하고 각각의 위치(Index)와 검색 개수를 출력
searchResultIdxs = []

nums.append(searchData)

n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdxs.append(n)
        else:
            break
    n += 1

print('---------- #2 ----------')
print(f'nums : {nums}')
print(f'nums length: {len(nums)}')
print(f'searchResultIdx : {searchResultIdxs}')
print(f'searchResultIdx count : {len(searchResultIdxs)}')
