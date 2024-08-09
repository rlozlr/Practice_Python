import random
import 삽입정렬 as insertMod

if __name__ == '__main__':
    rNums = random.sample(range(1, 21), 10)

    print(f'not sorted nums:\n{rNums}')
    result = insertMod.sortInsertAlgorithm(rNums)
    print(f'sorted nums by ASC: \n{result}')

    print(f'not sorted nums:\n{rNums}')
    result = insertMod.sortInsertAlgorithm(rNums, asc=False)
    print(f'sorted nums by DESC: \n{result}')