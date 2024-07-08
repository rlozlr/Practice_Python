'''
국어, 영어, 수학 점수를 입력받아 리스트에 저장하고 원본을 유지한 상태로,
복사본을 만들어 과목별 점수를 10% 올렸을 경우에 평균을 출력
'''

scoreList = [int(input('국어: ')),
             int(input('영어: ')),
             int(input('수학: '))]

print(scoreList)
print()

copyScore = scoreList.copy()

# enumerate() : 순회 가능한(iterable) 객체(예: 리스트, 튜플, 문자열 등)를 입력으로 받아 인덱스와 해당 요소를 순회하는 데 사용
for idx, score in enumerate(copyScore):
    result = score * 1.1
    copyScore[idx] = 100 if result > 100 else result

print(f'원본 평균: {round(sum(scoreList) / len(scoreList), 2)}')
print(f'10% 상승 평균: {round(sum(copyScore) / len(copyScore), 2)}')