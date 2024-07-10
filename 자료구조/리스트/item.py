# 5명의 학생 이름을 리스트에 저장하고 인덱스가 홀수인 학생과 짝수(0 포함)인 학생을 구분해서 인덱스와 학생 이름 출력
students = ['해리', '헤르미온느', '론', '지니', '루나']
for i in range(5):
    idx = '[홀수] 인덱스' if ( i % 2 == 1) else '[짝수] 인덱스'
    print('{}: student [{}] : {}'.format(idx, i, students[i]))