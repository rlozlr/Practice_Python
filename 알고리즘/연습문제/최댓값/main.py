import random
import 최댓값01 as maxMod01
import 최댓값02 as maxMod02

def run_maxMod01():

    nums = []
    for n in range(30):
        nums.append(random.randint(1, 50))

    print(f'nums: \n {nums}')
    na = maxMod01.MaxAlgorithm(nums)
    print(f'max num: {na.getMaxNum()}')
    print((f'max num count: {na.getMaxNumCnt()}'))

def run_maxMod02():
    scores =  [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
    scores_avg = maxMod02.getAvg(scores)
    scores_max = maxMod02.getMax(scores)
    deviation = maxMod02.getDeviation(scores_avg, scores_max)

    print(f'scores_avg: {scores_avg}')
    print(f'scores_max: {scores_max}')
    print(f'deviation: {deviation}')

if __name__ == '__main__':
    choice = int(input('1 or 2: '))

    if choice == 1:
        run_maxMod01()
    elif choice == 2:
        run_maxMod02()
