# 학급 학생(20명)들의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고, 중간고사 대비 기말고사 순위 변화(편차)를 출력
# (시험 성적은 난수 이용)
class RankDeviation:

    def __init__(self, mss, ess):
        self.midStdScos = mss
        self.endStdScos = ess
        self.midRanks = [0 for i in range(len(mss))]
        self.endRanks = [0 for i in range(len(mss))]
        self.rankDeviation = [0 for i in range(len(mss))]

    def setRank(self, ss, rs):
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1

    def setMidRank(self):
        self.setRank(self.midStdScos, self.midRanks)

    def getMidRank(self):
        return self.midRanks

    def setEndRank(self):
        self.setRank(self.endStdScos, self.endRanks)

    def getEndRank(self):
        return self.endRanks

    def printRankDeviation(self):
        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.endRanks[idx]

            if deviation > 0:
                deviation = '↑' +  str(abs(deviation))
            elif deviation < 0:
                deviation = '↓' + str(abs(deviation))
            else:
                deviation = '=' + str(abs(deviation))

            print(f'midRank: {mRank} \t endRank : {self.endRanks[idx]} \t Deviation: {deviation}')

