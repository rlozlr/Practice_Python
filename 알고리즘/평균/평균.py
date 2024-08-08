# 다음은 어떤 체조선수의 점수이다.
'''
sco1  | 8.9
sco2  | 7.6
sco3  | 8.2
sco4  | 9.1
sco5  | 8.8
sco6  | 8.1
sco7  | 7.9
sco8  | 9.4
sco9  | 7.2
sco10 | 8.7
'''
# 평균을 구하고 순위를 정하는 Algorithm 만들기

class Top5Scores:

    def __init__(self, cs, ns):
        self.currentScores = cs
        self.newScore = ns

    def setAlignScore(self):
        nearIdx = 0
        # nearScore = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore -s)

            if absNum < minNum:
                minNum = absNum
                nearIdx = i
                nearScore = s

        if self.newScore >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores)-1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i-1]

            self.currentScores[nearIdx] = self.newScore

        else:
            for i in range(len(self.currentScores) - 1, nearIdx + 1, -1):
                self.currentScores[i] = self.currentScores[i -1]

            self.currentScores[nearIdx] = self.newScore

    def getFinalTopScores(self):
        return self.currentScores
