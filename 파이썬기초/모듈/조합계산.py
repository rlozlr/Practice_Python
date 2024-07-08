import 조합모듈 as ct

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

print(f'{numN}C{numR}: {ct.getCombinationCnt(numN, numR, logPrint=False)}')

listVar = [1, 2, 3, 4, 5, 6, 7, 8]
rVar = 3
ct.getCombinations(listVar, rVar)