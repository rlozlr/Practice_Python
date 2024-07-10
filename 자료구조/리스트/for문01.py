# 아래 표와 리스트를 이용해서 학급별 학생 수와 전체 학생 수 그리고 평균 학생수를 출력
'''
1학급 : 18명, 2학급 : 19명, 3학급 : 23명, 4학급 : 21명, 5학급 : 20명, 6학급 : 22명, 7학급 : 17명
'''
students = [1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]

SumStudent = 0
totalStudent = 0

for classNo, studentCnt in students:
    print('{}학급: {}명'.format(classNo, studentCnt))
    totalStudent += studentCnt

print('전체 학생 수: {}명'.format(totalStudent))
print('평균 학생 수: {}명'.format(totalStudent / len(students)))