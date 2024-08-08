# 1부터 100까지의 난수 100개를 생성하고, 다음의 요구사항을 만족하는 모듈
'''
1) 생성된 난수들을 오름차순 또는 내림차순으로 정렬하는 알고리즘 구현
2) 생성된 난수 중 최솟값, 최댓값을 반한하는 함수 구현
'''
class SortNumbers:

    def __init__(self, ns, asc=True):
        self.nums = ns
        self.isAsc = asc

    def isAscending(self, flag):
        self.isAsc = flag

    def setSort(self):
        for num1 in range(1, len(self.nums)):
            num2 = num1 - 1
            cNum = self.nums[num1]

            if self.isAsc:
                while self.nums[num2] > cNum and num2 >= 0:
                    self.nums[num2 + 1] = self.nums[num2]
                    num2 -= 1

            else:
                while self.nums[num2] < cNum and num2 >= 0:
                    self.nums[num2 + 1] = self.nums[num2]
                    num2 -= 1

            self.nums[num2 + 1] = cNum

    def getsortedNumbers(self):
        return self.nums

    def getMinNumber(self):
        if self.isAsc:
            return self.nums[0]
        else:
            return self.nums[len(self.nums) -1]

    def getMaxNumber(self):
        if self.isAsc:
            return self.nums[len(self.nums) -1]
        else:
            return self.nums[0]