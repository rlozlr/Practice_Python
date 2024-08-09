# 알파벳 문자들과 정수들에 대한 순위를 정하는 프로그램을 순위 Algorithm을 이용해서 만들기.
# 단, 알파벳은 ASCII코드 값을 이용.
'''
[32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
'''
datas = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
print(f'datas: {datas}')

asciiDatas = []
for data in datas:
    if str(data).isalpha():
        asciiDatas.append(ord(data))
        continue

    asciiDatas.append(data)

print(f'ASCII: {asciiDatas}')

ranks = [0 for i in range(len(asciiDatas))]
print(f'ranks before: {ranks}')

for idx, data1 in enumerate(asciiDatas):
    for data2 in asciiDatas:
        if data1 < data2:
            ranks[idx] += 1

print(f'ranks after: {ranks}')

for i, d in enumerate(datas):
    print(f'data:{d:>2} \t rank: {ranks[i] + 1}')