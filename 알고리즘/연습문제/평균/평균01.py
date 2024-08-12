# 다음은 어떤 체조선수의 경기 점수이다.
'''
6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8
'''
# 최댓값과 최솟값을 제외한 나머지 점수에 대한 평균을 구하고 순위를 정하는 Algorithm 만들기
class Top5Players:

    def __init__(self, cts, ns):
        self.currentScores = cts
        self.newScore = ns

    def setAlignScore(self):
        nearIdx = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore - s)
            if absNum < minNum:
                minNum = absNum
                nearIdx = i

            if self.newScore >= self.currentScores[nearIdx]:
                for i in range(len(self.currentScores) - 1, nearIdx, -1):
                    self.currentScores[i] = self.currentScores[i - 1]
                self.currentScores[nearIdx] = self.newScore

            else:
                for i in range(len(self.currentScores) - 1, nearIdx, -1):
                    self.currentScores[i] = self.currentScores[i - 1]
                self.currentScores[nearIdx + 1] = self.newScore

    def getFinalTop5Scores(self):
        return self.currentScores