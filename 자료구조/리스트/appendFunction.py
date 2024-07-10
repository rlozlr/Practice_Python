# 가족 구성원의 나이가 아래와 같을 때 새로 태어난 동생을 리스트에 추가
'''
아빠 : 40세, 엄마 : 38세, 나 : 9세
'''
family = [
    ['아빠', 40],
    ['엄마', 38],
    ['나', 9]
]
newMember = ['동생', 1]
family.append(newMember)

for name, age in family:
    print('{} : {}세'.format(name, age))