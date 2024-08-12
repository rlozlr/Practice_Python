import 최빈값01 as modeMode01
import 최빈값02 as modeMode02
import maxMod

def run_01():
    ages = [25, 27, 27, 24, 31, 34, 33, 31, 29, 25,
            45, 37, 38, 46, 47, 22, 24, 29, 33, 35,
            27, 34, 37, 40, 42, 29, 27, 25, 26, 27,
            31, 31, 32, 38, 25, 27, 28, 40, 41, 34]
    
    print(f'employee cnt: {len(ages)}명')

    maxAlgo = maxMod.MaxAlgorithm(ages)
    maxAlgo.setMaxIdxAndNum()
    maxAge = maxAlgo.getMaxNum()
    print(f'maxAge: {maxAge}세')

    modeAlgo = modeMode01.ModeAlgorithm(ages, maxAge)
    modeAlgo.setIndexList()
    print(f'indexList: {modeAlgo.getIndexList()}')

    modeAlgo.printAges()

def run_02():
    lottoNums = [
        [13, 23, 15, 5, 6, 39], [36, 13, 5, 3, 30, 16], [43, 1, 15, 9, 3, 38],
        [32, 42, 24, 45, 8, 31], [18, 39, 41, 11, 4, 9], [12, 39, 11, 38, 32, 5],
        [29, 25, 13, 6, 14, 8], [21, 33, 19, 20, 42, 7], [6, 28, 3, 45, 41, 39],
        [42, 15, 8, 5, 35, 4], [14, 4, 35, 24, 29, 3], [15, 20, 6, 37, 34, 39],
        [27, 5, 32, 15, 25, 19], [45, 25, 2, 8, 30, 43], [4, 19, 33, 10, 6, 24],
        [25, 26, 45, 23, 24, 16], [33, 28, 45, 21, 38, 24], [4, 30, 29, 28, 32, 38],
        [11, 28, 12, 2, 42, 3], [40, 29, 16, 8, 9, 28], [6, 9, 37, 30, 3, 35],
        [29, 18, 41, 28, 38, 15], [9, 31, 13, 44, 1, 36], [36, 1, 37, 32, 15, 12],
        [41, 32, 16, 6, 26, 33], [12, 43, 10, 29, 39, 9], [41, 9, 23, 35, 18, 17],
        [35, 38, 3, 28, 36, 31], [21, 44, 4, 29, 18, 7], [20, 23, 6, 2, 34, 44]
    ]

    ln = modeMode02.lottoMode(lottoNums)
    nList = ln.getLottoNumMode()
    # print(f'nList: {nList}')
    ln.printModeList()

if __name__ == '__main__':
    choice = int(input('1 or 2: '))

    if choice == 1:
        run_01()
    elif choice == 2:
        run_02()