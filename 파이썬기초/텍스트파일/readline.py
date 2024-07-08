# 파일에 저장된 과목별 점수를 파이썬에서 읽어, scoreDic에 저장하는 코드 만들기
scoreDic = {}
uri = 'C:/pythonEx/'

with open (uri + 'scoreDic.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tmpList = line.split(":")
        scoreDic[tmpList[0]] = int(tmpList[1].strip('\n'))  # strip()은 ()안에 있는 것을 잘라버린다.
        line = f.readline()
print(f'점수:" {scoreDic}')
