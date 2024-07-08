# 사전에 저장된 과목별 점수를 파일에 저장하는 코드
dic = {'kor': 85, 'eng':90, 'mat':92, 'sci':79, 'his':82}
uri = 'C:/pythonEx/'

# for key in dic.keys():
#     with open(uri + 'dic.txt', 'a') as f:
#         f.write(key + '\t: ' + str(dic[key]) + '\n')

scoreList = [85, 90, 92, 79, 82]
with open(uri + 'scoreList.txt', 'a') as f:
    print(scoreList, file=f)


