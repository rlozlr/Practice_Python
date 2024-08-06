# 친구 이름 다섯 명을 List에 저장하고 오름차순과 내림차순으로 정렬
friendList = []
for i in range(5):
    friendList.append(input('친구 이름: '))

print('친구리스트: {}'.format(friendList))

friendList.sort()
print('오름차순: {}'.format(friendList))

friendList.sort(reverse = True)
print('내림차순: {}'.format(friendList))
