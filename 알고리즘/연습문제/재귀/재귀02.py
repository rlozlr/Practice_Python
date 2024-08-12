# 사용자가 정수 두 개를 입력하면 작은 정수와 큰 정수 사이의 모든 정수의 합을 구하는 프로그램을 재귀 Algorithm을 이용해서 만들기
class NumsSum:

    def __init__(self, n1, n2):
        self.bigNum = 0
        self.smallNum = 0
        self.setN1n2(n1, n2)

    def setN1n2(self, n1, n2):
        self.bigNum = n1
        self.smallNum = n2

        if n1 < n2:
            self.bigNum = n2
            self.smallNum = n1

    def addNum(self, n):
        if n <= 1:
            return n

        return n + self.addNum(n-1)

    def sumBetweenNums(self):
        return self.addNum(self.bigNum - 1) - self.addNum(self.smallNum)
