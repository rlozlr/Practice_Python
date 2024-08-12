class MinAlgorithm:

    def __init__(self, ss):
        self.scores = ss
        self.minScore =0
        self.minIdx = 0

    def removeMinScore(self):
        self.minScore = self.scores[0]

        for i, s in enumerate(self.scores):
            if self.minScore > s:
                self.minScore = s
                self.minIdx = i

        print(f'self.minScore: {self.minScore}')
        print(f'self.minIdx: {self.minIdx}')

        self.scores.pop(self.minIdx)
        print(f'scores: {self.scores}')