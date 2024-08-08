# 최빈값 Algorithm을 이용해서 학생 100명의 점수 분포 나타내기

class MaxAlgorithm:
    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def setMaxNumIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx