# 삼각형부터 십각형까지의 내각의 합과 내각을 Dictionary에 저장
# n각형의 내각의 합 : 180 * (n - 2)
dic = {}

for n in range (3, 11):
    hap = 180 * (n - 2)
    ang = int(hap / n)
    dic[n] = [hap, ang]

print(dic)