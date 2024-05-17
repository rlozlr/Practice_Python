'''
국어, 영어, 수학, 과학, 국사 점수를 입력하면 총점을 비롯한 각종 데이터가 출력되는 프로그램

    - 과목별 점수를 입력하면 총점, 평균, 편차를 출력
        평균은 다음과 같다.
        (국어: 85, 영어: 82, 수학: 89, 과학: 75, 국사: 94)
    - 각종 편차 데이터는 막대그래프로 시각화
'''
avgKor = 85; avgEng = 82; avgMath = 89; avgSciece = 75; avgHistory = 94
sum = avgKor + avgEng + avgMath + avgSciece + avgHistory
avg = sum / 5

kor = int(input('국어: '))
eng = int(input('영어: '))
math = int(input('수학: '))
science = int(input('과학: '))
history = int(input('국사: '))
userSum = kor + eng + math + science + history
userAvg = userSum / 5
gapKor = kor-avgKor
gapEng = eng-avgEng
gapMath = math-avgMath
gapScience = science-avgSciece
gapHistory = history-avgHistory

print('*' * 50)
print('총점: {}({}), 평균: {:.0f}({:.0f})'.format(userSum, userSum - sum, userAvg, userAvg - avg))
print('국어: {}({}), 영어: {}({}), 수학: {}({}), 과학: {}({}), 국사: {}({})'
      .format(kor, gapKor,
              eng, gapEng,
              math, gapMath,
              science, gapScience,
              history, gapHistory))
print('*' * 50)
op = '+' if gapKor > 0 else '-'
print('국어 편차: {}({})'.format(op * abs(gapKor), gapKor))
op = '+' if gapEng > 0 else '-'
print('영어 편차: {}({})'.format(op * abs(gapEng), gapEng))
op = '+' if gapMath > 0 else '-'
print('수학 편차: {}({})'.format(op * abs(gapMath), gapMath))
op = '+' if gapScience > 0 else '-'
print('과학 편차: {}({})'.format(op * abs(gapScience), gapScience))
op = '+' if gapHistory > 0 else '-'
print('국사 편차: {}({})'.format(op * abs(gapHistory), gapHistory))
print('*' * 50)