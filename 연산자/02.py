'''
국어, 영어, 수학 점수 입력 후 총점, 평균, 최고점수 과목, 최저점수 과목
그리고 최고 점수와 최저 점수의 차이를 각각 출력
'''

kor = int(input('국어 점수: '))
maxScore, minScore = kor, kor
maxObject, minObject = '국어', '국어'

eng = int(input('영어 점수: '))
if(eng > maxScore):
    maxScore = eng
    maxObject = '영어'
else:
    minScore = eng
    minObject = '영어'

math = int(input('수학 점수: '))
if(math > maxScore):
    maxScore = math
    maxObject = '수학'
else:
    minScore = math
    minObject = '수학'

print('총점: {}'.format(kor + eng + math))
print('평균: %.2f' % ((kor + eng + math) / 3))
print('*' * 20)
print('최고 점수 과목(점수): {}({})'.format(maxObject, maxScore))
print('최저 점수 과목(점수): {}({})'.format(minObject, minScore))
print(f'최고, 최저 점수 차이: {maxScore - minScore}')
print('*' * 20)