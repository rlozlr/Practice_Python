# 암호를 해독
'''
암호: 27156231
해독: 13326125157214
'''
screteNum = '27156231'
print(screteNum)

screteList = []
for charEle in screteNum:
    screteList.append(int(charEle))
screteList.reverse()
print(screteList)

screteList.insert(2, (screteList[0] * screteList[1]))
screteList.insert(5, (screteList[3] * screteList[4]))
screteList.insert(8, (screteList[6] * screteList[7]))
screteList.insert(11, (screteList[9] * screteList[10]))

decoded = str(screteList)
print("해독:", decoded)