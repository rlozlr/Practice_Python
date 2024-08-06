# 과목별 점수를 Dictionary에 저장하고 출력

sub = ['국어', '영어', '수학', '과학']
scores = {}

for subject in sub:
    score = input(subject + ' 점수 : ')
    scores[subject] = score

print(f'과목 점수 : {scores}')