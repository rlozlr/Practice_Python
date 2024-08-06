# 학생 정보 테이블
'''
학생번호      이름      성구분     전공        연락처             메일                  취미
S21-0001      최성훈     M         디자인      010-1234-5678      hun@gmail.com         농구, 음악
S21-0002      탁영우     M         바리스트    010-5678-9012      yeong@gmail.com       축구
S21-0003      황진영     W         음악        010-9012-3456      jin@gmail.com         수영, 코딩
'''
# python에서 학생 정보를 가장 효율적으로 저장하고 관리할 수 있는 자료 구조를 선택해서 컨테이너 자료형으로 만들기
students = {
    'S21-001':{'이름':'최성훈',
               '성구분':'M',
               '전공':'디자인',
               '연락처':'010-1234-5678',
               '메일':'hun@gmail.com',
               '취미':'농구, 음악'},
    'S21-002': {'이름': '탁영우',
                '성구분': 'M',
                '전공': '바리스트',
                '연락처': '010-5678-9012',
                '메일': 'yeong@gmail.com',
                '취미': '축구'},
    'S21-003': {'이름': '황진영',
                '성구분': 'W',
                '전공': '음악',
                '연락처': '010-9012-3456',
                '메일': 'jin@gmail.com',
                '취미': '수영, 코딩'}
}

for key1 in students.keys():
    print('-' * 40)
    print('학생번호: {}'.format(key1))

    student = students[key1]
    for key2 in students.keys():
        print('{} :{}'.format(key2, students[key2]))

print('-' * 40)
stdNo = input('조회 학생 번호 입력: ')
print('{} : {}'.format(stdNo, students[stdNo]))