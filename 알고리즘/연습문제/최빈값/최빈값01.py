# 다음은 어떤 회사의 전직원 나이를 나타내는 List
'''
    ages = [25, 27, 27, 24, 31, 34, 33, 31, 29, 25,
            45, 37, 38, 46, 47, 22, 24, 29, 33, 35,
            27, 34, 37, 40, 42, 29, 27, 25, 26, 27,
            31, 31, 32, 38, 25, 27, 28, 40, 41, 34]
'''
# 최빈값 Algorithm을 이용해서 나이 분포를 간단한 그래프로 출력하는 모듈
import maxMod

class ModeAlgorithm:
    def __init__(self, ns, mn):
        self.nums = ns
        self.maxNum = mn
        self.indexes = []

    def setIndexList(self):
        self.indexes = [0 for i in range(self.maxNum + 1)]

        for n in self.nums:
            self.indexes[n] = self.indexes[n] + 1

    def getIndexList(self):
        if sum(self.indexes) == 0:
            return None

        else:
            return self.indexes

    def printAges(self):

        n = 1
        while True:

            maxAlgo = maxMod.MaxAlgorithm(self.indexes)
            maxAlgo.setMaxIdxAndNum()
            maxNum = maxAlgo.getMaxNum()
            maxNumIdx = maxAlgo.getMaxIdx()

            if maxNum == 0:
                break

            print(f'[{n:0>3}] {maxNumIdx}세 빈도수: {maxNum} \t', end='')
            print('+' * maxNum)
            self.indexes[maxNumIdx] = 0

            n += 1

