import random
import 순위01 as rankMod01

if __name__ == '__main__':
    rNums = random.sample(range(50, 101), 20)
    sNums = rankMod01.rankAlgorithm(rNums)
    print(f'sNums: {sNums}')