class MaxAlgorithm:

    def __init__(self, ss):
        self.scores = ss
        self.maxScore =0
        self.maxIdx = 0

    def removeMaxScore(self):
        self.maxScore = self.scores[0]

        for i, s in enumerate(self.scores):
            if self.maxScore < s:
                self.maxScore = s
                self.maxIdx = i

        print(f'self.maxScore: {self.maxScore}')
        print(f'self.maxIdx: {self.maxIdx}')

        self.scores.pop(self.maxIdx)
        print(f'scores: {self.scores}')