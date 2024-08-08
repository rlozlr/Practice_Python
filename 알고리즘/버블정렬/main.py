# 새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서로 줄 세워 보자.
# 학생들의 키는 random  모듈을 이용해서 170 ~ 185 사이로 생성
import random
import 버블정렬 as bubble

students = []

for i in range(20):
    students.append(random.randint(170, 185))

print(f'students: {students}')

sortedStudents = bubble.bubbleSort(students, deepCopy=False)

print(f'students: {students}')
print(f'sortedStudents: {sortedStudents}')