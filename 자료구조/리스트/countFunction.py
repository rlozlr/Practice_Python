# 하루 동안 헌혈을 진행한 후 혈액형 별 개수를 파악
import random

bloodType = ['A', 'B', 'O', 'AB']
visitor = []
typeCnt = []

for i in range(100) :
    type = bloodType[random.randrange(len(bloodType))]
    visitor.append(type)

print('visitor: {}'.format(visitor))
print('visitor length: {}'.format(len(visitor)))

for type in bloodType:
    print('{}형 \t : {}개'.format(type, visitor.count(type)))
