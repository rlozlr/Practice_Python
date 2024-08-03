# Tuple을 이용한 점수표에서 최저, 최고 점수를 삭제한 후 총점과 평균을 출력
'''
점수 1: 9.5,
점수 2: 8.9,
점수 3: 9.2,
점수 4: 9.8,
점수 5: 8.8,
점수 6: 9.0
'''

scoreTuple = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print(type(scoreTuple))
print(scoreTuple)
print('--- Tuple에서 List로 형 변환 ---')
scoreList = list(scoreTuple)
print(type(scoreList))
print(scoreList)
print()

scoreList.sort()
print('최저 점수: {}'.format(scoreList.pop(0)))
print('최고 점수: {}'.format(scoreList.pop(len(scoreList) - 1)))
print('최저/최고 점수 제거 후: {}'.format(scoreList))
print()

print('총점: {}, 평균: {:.2f}'.format(sum(scoreList), (sum(scoreList)/len(scoreList))))