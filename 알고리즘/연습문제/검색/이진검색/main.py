# 숫자로 이루어진 List에서 사용자가 입력한 숫자를 검색하는 모듈
'''
1) 검색 모듈은 이진 검색 Algorithm 이용
2) 리스트는 [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]를 이용
3) 검색 과정을 로그로 출력
4) 검색에 성공하면 해당 정수의 Index를 출력하고, 검색 결과가 없다면 -1을 출력
'''

import 이진검색 as binaryMod

if __name__ == '__main__':

    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    searchNum = int(input('찾는 숫자: '))

    resultIdx = binaryMod.searchNumberByBinaryAlgorithm(nums, searchNum)
    print(f'nums: {nums}')

    if resultIdx == 1:
        print('No result found.')
        print(f'search result index: {resultIdx}')

    else:
        print(f'search result index: {resultIdx}')
        print(f'search result num: {nums[resultIdx]}')