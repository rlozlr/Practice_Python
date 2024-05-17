'''
선수의 원본 점수를 이용해서 평균을 출력하고, 최고값과 최저값을 제외한 평균을 출력하는 프로그램
'''

originScore = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
copyScore = originScore.copy()
originScore.sort()  # 오름차순 정렬

copyScore.sort()
copyScore.pop(0)    # 리스트에서 첫 번째 요소를 제거하고 반환
copyScore.pop()     # 리스트에서 마지막 요소를 제거하고 반환

print(f'origin: {originScore}')
print(f'copy: {copyScore}')
print()

originSum = round(sum(originScore), 2)
originAvg = round(originSum / len(originScore), 2)
print(f'origin sum : {originSum}')
print(f'origin avg : {originAvg}')
print()

copySum = round(sum(copyScore), 2)
copyAvg = round(copySum / len(copyScore), 2)
print(f'copy sum : {copySum}')
print(f'copy avg : {copyAvg}')
print()

print(f'originAvg - copyAvg : {originAvg - copyAvg:.2f}')