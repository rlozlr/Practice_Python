# 최솟값 Algorithm을 이용해서 숫자로 이루어진 List에서 최솟값과 최솟값의 개수를 찾는 모듈
# List는 1부터 50까지의 난수 30개를 이용하되, 중복 허용
class minAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0
        self.minNumCnt = 0

    def setMinNum(self):
        self.minNum = 51

        for n in self.nums:
            if self.minNum > n:
                self.minNum = n

    def getMinNum(self):
        self.setMinNum()
        return self.minNum

    def setMinNumCnt(self):
        self.setMinNum()

        for n in self.nums:
            if self.minNum == n:
                self.minNumCnt += 1

    def getMinNumCnt(self):
        self.setMinNumCnt()
        return self.minNumCnt
