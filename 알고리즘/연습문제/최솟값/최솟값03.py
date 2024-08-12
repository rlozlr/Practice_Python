class ScoreManagement:
    def __init__(self, ss):
        self.scores = ss
        self.score_tot = 0
        self.score_avg = 0
        self.score_min = 0
        self.score_max = 0

    def getMinScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_min = self.scores[0]
        for score in self.scores:
            if self.score_min > score:
                self.score_min = score

        return self.score_min

    def getMaxScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_max = self.scores[0]
        for score in self.scores:
            if self.score_max < score:
                self.score_max = score

        return self.score_max

    def getTotScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_tot = 0
        for score in self.scores:
            self.score_tot += score

        return self.score_tot

    def getAvgScore(self):
        if self.scores == None or len(self.scores) == 0:
            return None

        self.score_avg = round(self.getTotScore() / len(self.scores), 2)
        return self.score_avg

    def getMaxDeviation(self):
        result = abs(self.getAvgScore() - self.getMaxScore())
        return round(result, 2)

    def getMinDeviation(self):
        result = abs(self.getAvgScore() - self.getMinScore())
        return round(result, 2)

