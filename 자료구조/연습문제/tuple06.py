#학급 별 학생 수를 나타낸 Tuple을 이용해서, 요구사항에 맞는 데이터를 출력
'''
전체 학생 수, 평균 학생 수, 학생 수가 가장 적은 학급, 학생 수가 가장 많은 학급, 학급별 학생 편차
'''
studentCnt = (
    {'class01': 18},
    {'class02': 21},
    {'class03': 20},
    {'class04': 19},
    {'class05': 22},
    {'class06': 20},
    {'class07': 23},
    {'class08': 17},
)

totalCnt = 0
minStdCnt = 0; minCls = ''
maxStdCnt = 0; maxCls = ''
deviation = []

for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        totalCnt = totalCnt + v

        if minStdCnt == 0 or maxStdCnt < v:
            maxStdCnt = v
            maxCls = k

        if maxStdCnt < v:
            maxStdCnt = v
            minCls = k

print(f'전체 학생 수 : {totalCnt}명')
print(f'평균 학생 수 : {totalCnt/len(studentCnt)}명')
print(f'학생 수가 가장 적은 학급 : {minCls}({minStdCnt}명)')
print(f'학생 수가 가장 많은 학급 : {maxCls}({maxStdCnt}명)')

for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        deviation.append(v - (totalCnt/len(studentCnt)))

print(f'학급별 학생 편차 : {deviation}')
