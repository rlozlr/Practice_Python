# 다음 표는 수심에 따른 수온을 나타내고 있다.
'''
수심 | 0 | 5 | 10 | 15 | 20 | 25 | 30
수온 | 24 | 22 | 20 | 16 | 13 | 10 | 6
'''
# 근사값 Algorithm을 이용해서 수심을 입력ㅎ면 수온을 출력하는 모듈
class NearAlgorithm:

    def __init__(self, d):
        self.temps = {0:24 , 5:22, 10:20, 15:16, 20:13, 25:10, 30:6}
        self.depth = d
        self.nearNum = 0
        self.minNum = 24

    def getNearNumbers(self):
        for n in self.temps.keys():
            absNum = abs(n - self.depth)
            if absNum < self.minNum:
                self.minNum = absNum
                self.nearNum = n

        return self.temps[self.nearNum]


