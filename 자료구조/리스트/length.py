# 좋아하는 운동 종목을 리스트에 저장하고 반복문을 이용해서 출력
sports = ['테니스', '농구', '복싱', '수영']

print('---- while ----')
n = 0
while n < len(sports):
    print(sports[n])
    n += 1

print('---- for 01 ----')
for i in range (len(sports)):
    print('sport list[{}] : {}'.format(i, sports[i]))

print('---- for 02 ----')
for item in sports:
    print(item)
