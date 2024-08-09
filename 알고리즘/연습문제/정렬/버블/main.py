import random
import 버블정렬 as bubbleMod

if __name__ == '__main__':
    rNums = random.sample(range(1, 21), 10)
    print(f'not sorted nums: {rNums}')

    result = bubbleMod.sortByBubbleAlgorithm(rNums)
    print(f'sorted nums by ASC: {result}')

    result = bubbleMod.sortByBubbleAlgorithm(rNums, asc=False)
    print(f'sorted nums by DESC: {result}')