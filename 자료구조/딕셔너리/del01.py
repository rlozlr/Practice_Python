# Dictionary에 저장된 점수 중 최저 및 최고 점수를 삭제
scores = {'save1' : 8.9, 'save2' : 8.1, 'save3' : 8.5, 'save4' : 9.8, 'save5': 8.9}
minScore = 10; minKey = ''
maxScore = 0; maxKey = ''
print(scores)

for key in scores.keys():
    if scores[key] < minScore:
        minScore = scores[key]
        minKey = key

    if scores[key] > maxScore:
        maxScore = scores[key]
        maxKey = key

print('최저 점수는 {} {}점'.format(minKey, scores.get(minKey)))
print('최고 점수는 {} {}점'.format(maxKey, scores.get(maxKey)))
del scores[minKey]
del scores[maxKey]
print(scores)