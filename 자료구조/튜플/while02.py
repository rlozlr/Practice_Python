# while문과 if문을 이용해서 과락 과목 출력
minScore = 60
score = (
    ('국어', 58),
    ('영어', 77),
    ('수학:', 89),
    ('과학', 99),
    ('국사', 50)
)

n = 0
while n < len(score):
    if (score[n][1] < minScore):
        print('{}과목은 {}점으로 과락입니다.'.format(score[n][0], score[n][1]))
    n += 1