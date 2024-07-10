# 점수표에서 최저 및 최고 점수를 삭제한 후 총점과 평균 출력
'''
점수 1: 9.5,
점수 2: 8.9,
점수 3: 9.2,
점수 4: 9.8,
점수 5: 8.8,
점수 6: 9.0
'''
scoreList = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print(scoreList)
print()

print('최저 점수: {}'.format(min(scoreList)))
scoreList.remove(min(scoreList))
print(scoreList)
print()

print('최고 점수: {}'.format(max(scoreList)))
scoreList.remove(max(scoreList))
print(scoreList)
print()

print('총점: {}, 평균: {:.2f}'.format(sum(scoreList), (sum(scoreList)/len(scoreList))))