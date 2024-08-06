# 1부터 사용자가 입력한 숫자까지의 약수와 소수를 List에 각각 저장하고 출력

userNum = int(input('숫자 입력: '))
listA = []  # 약수
listB = []  # 소수

for num in range(1, (userNum + 1)):
    if num == 1:
        listA.append(num)
    else:
        if userNum % num == 0:
            listA.append(num)

for num in range(1, (userNum + 1)):
    flag = True
    for n in range(2, num):
        if num % n == 0:
            flag = False
            break
    if flag:
        listB.append(num)

print('listA: {}'.format(listA))
print('listB: {}'.format(listB))