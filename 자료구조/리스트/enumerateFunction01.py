# 가장 좋아하는 스포츠가 몇 번째에 있는지 출력
sports = ['농구', '축구', '수영', '테니스', '복싱']
favoriteSport = input('가장 좋아하는 스포츠: ')

itIdx = 0
for idx, val in enumerate(sports):
    if val == favoriteSport:
        itIdx += idx + 1

print('{}(은/는) {} 번째에 있습니다.'.format(favoriteSport, itIdx))