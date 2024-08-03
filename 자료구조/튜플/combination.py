# Tuple을 이용해서 나와 친구가 좋아하는 번호를 합치되, 번호가 중복되지 않게 하기
myFavoriteNum = (3, 4, 6, 100)
friendFavoriteNum = (3, 4, 13, 23)
favoriteNum = ()
for num in myFavoriteNum:
    if num not in favoriteNum:
        favoriteNum = favoriteNum + (num, )

for num in friendFavoriteNum:
    if num not in favoriteNum:
        favoriteNum = favoriteNum + (num, )

print(favoriteNum)
