import random
import 병합정렬 as mergeMod

if __name__ == '__main__':
    rNums = random.sample(range(1, 101), 20)
    print(f'rNums: {rNums}')
    print(f'mergeAlgorithm.mergeSort(rNums): {mergeMod.mergeSort(rNums)}')
    print(f'mergeAlgorithm.mergeSort(rNums): {mergeMod.mergeSort(rNums, asc=False)}')
