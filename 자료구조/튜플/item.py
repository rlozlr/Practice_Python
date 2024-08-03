# 5명의 학생 이름을 튜플에 저장하고 인덱스가 홀수인 학생과 짝수(0포함)인 학생을 구분해서 인덱스와 학생 이름을 출력
students = ('짱구', '철수', '유리', '맹구', '훈이')

for i in range (len(students)):
    if i % 2 == 0:
        print('짝수 인덱스: Index[{}] : {}'.format(i, students[i]))
    else :
        print('홀수 인덱스: Index[{}] : {}'.format(i, students[i]))
