import random
import 선택정렬 as selectMod

if __name__ == '__main__':
    rNums = random.sample(range(1, 21), 10)

    print(f'not sorted nums: \t {rNums}')
    result = selectMod.sortSelectAlgorithm(rNums)
    print(f'sorted nums by ASC: {result}')

    print(f'not sorted nums: \t {rNums}')
    result = selectMod.sortSelectAlgorithm(rNums, asc=False)
    print(f'sorted nums by ASC: {result}')

