# List를 오름차순으로 정렬한 후 '7'을 검색하고 위치(Index)를 출력
nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
print(nums)

nums.sort()
print(f'오름차순: {nums}')

searchData = int(input('숫자: '))
searchResultIdx = -1
staIdx = 0
endIdx = len(nums) -1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

while searchData <= nums[len(nums) - 1] and searchData >= nums[0]:
    if searchData == nums[len(nums) - 1]:
        searchResultIdx = len(nums) - 1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]

    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: {searchResultIdx}')
