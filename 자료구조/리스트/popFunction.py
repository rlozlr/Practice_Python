# 어떤 체조 선수의 점수표를 보고, 점수표에서 최저, 최고 점수를 삭제
'''
점수1 : 9.5
점수2 : 8.9
점수3 : 9.2
점수4 : 9.8
점수5 : 8.8
점수6 : 9.0
'''

playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
minScore = min(playerScore)
minIdx = playerScore.index(minScore)
maxScore = max(playerScore)
maxIdx = playerScore.index(maxScore)
print('---min pop---')
print(playerScore)
print('minScore: {}, minScoreIdx: {}'.format(minScore, minIdx))
playerScore.pop(minIdx)
print(playerScore)
print()
print('---max pop---')
print('maxScore: {}, maxScoreIdx: {}'.format(maxScore, maxIdx))
playerScore.pop(maxIdx)
print(playerScore)