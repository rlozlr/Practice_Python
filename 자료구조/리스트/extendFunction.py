# 나와 친구가 좋아하는 번호를 합치되 번호가 중복되지 않도록
'''
나: 1, 3, 5, 6, 7
친구: 2, 3, 5, 8, 10
'''
meNum = [1, 3, 5, 6, 7]
friendNum = [2, 3, 5, 8, 10]
print('나: {}'.format(meNum))
print('친구: {}'.format(friendNum))
addList = set(meNum + friendNum)
print('나 + 친구 (중복제외): {}'.format(addList))
