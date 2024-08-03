# while문을 이용해서 사용자가 국어, 영어, 수학, 과학, 국사 점수를 입력하면 과락 과목과 점수를 출력
minScore = 60

korScore = int(input('국어: '))
engScore = int(input('영어: '))
mathScore = int(input('수학: '))
sciScore = int(input('과학: '))
hisScore = int(input('국사: '))

userScore = (
    ('국어', korScore),
    ('영어', engScore),
    ('수학:', mathScore),
    ('과학', sciScore),
    ('국사', hisScore)
)

n = 0
while n < len(userScore):
    if userScore[n][1] < minScore:
        print('{}과목 {}점으로 과락'.format(userScore[n][0], userScore[n][1]))
    n += 1