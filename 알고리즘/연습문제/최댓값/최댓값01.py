# 최댓값 Algorithm을 이용해서 숫자로 이루어진 List에서 최댓값과 최댓값의 개수를 찾는 모듈
# List는 1부터 50까지의 난수 30개를 이용하되, 중복이 허용되도록

class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumCnt = 0

    def setMaxNum(self):
        self.maxNum = 0

        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n

        return self.maxNum

    def getMaxNum(self):
        self.setMaxNum()
        return self.maxNum

    def setMaxNumCnt(self):
        self.setMaxNum()

        for n in self.nums:
            if self.maxNum == n:
                self.maxNumCnt += 1

    def getMaxNumCnt(self):
        self.setMaxNumCnt()
        return self.maxNumCnt
