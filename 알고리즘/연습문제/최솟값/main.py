import random
import 최솟값01 as minMod01
import 최솟값02 as minMod02
import 최솟값03 as minMod03

def run_minMod01():
    nums = []

    for n in range(50):
        nums.append(random.randint(1, 50))

    print(f'nums: \n {nums}')
    ma = minMod01.minAlgorithm(nums)
    print(f'min num: {ma.getMinNum()}')
    print(f'min num count: {ma.getMinNumCnt()}')

def run_minMod02():
    scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]

    scores_avg = minMod02.getAvg(scores)
    scores_min = minMod02.getMaxOrMin(scores, maxFlag=False)
    deviation = minMod02.getDeviation(scores_avg, scores_min)

    print(f'scores_avg: {scores_avg}')
    print(f'scores_min: {scores_min}')
    print(f'deviation: {deviation}')

def run_minMod03():
    scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
    sm = minMod03.ScoreManagement(scores)
    print(f'score_avg: {sm.getAvgScore()}')
    print(f'score_min: {sm.getMinScore()}')
    print(f'score_max: {sm.getMaxScore()}')
    print(f'score_min_deviation: {sm.getMinDeviation()}')
    print(f'score_max_deviation: {sm.getMaxDeviation()}')

if __name__ == '__main__':
    choice = int(input('1 / 2 / 3: '))

    if choice == 1:
        run_minMod01()
    elif choice == 2:
        run_minMod02()
    elif choice == 3:
        run_minMod03()