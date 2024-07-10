# 아래의 표와 리스트를 이용해서 학급 학생 수가 가장 작은 학급과 가장 많은 학급을 출력
'''
1학급 : 18명, 2학급 : 19명, 3학급 : 23명, 4학급 : 21명, 5학급 : 20명, 6학급 : 22명, 7학급 : 17명
'''
school = [
    [1, 18],
    [2, 19],
    [3, 23],
    [4, 21],
    [5, 20],
    [6, 22],
    [7, 17]
]

minInfo = min(school, key=lambda x: x[1])
maxInfo = max(school, key=lambda x: x[1])
print('학생 수가 가장 적은 학급은 {}명으로 {}반입니다.'.format(minInfo[1], minInfo[0]))
print('학생 수가 가장 많은 학급은 {}명으로 {}반입니다.'.format(maxInfo[1], maxInfo[0]))
