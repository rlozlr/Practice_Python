# 1부터 10까지의 각각의 정수에 대한 약수를 저장하는 Dictionary를 만들고 출력

dic = {}

for n1 in range (2, 11):
     tempList = []
     for n2 in range(1, n1 + 1):
         if n1 % n2 == 0:
             tempList.append(n2)
     dic[n1] = tempList

print(dic)
