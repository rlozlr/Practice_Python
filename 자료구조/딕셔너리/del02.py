# 개인 정보에 '연락처'와 '주민등록번호'가 있다면 삭제
myInfo = {"이름" : "파이",
          "전공" : "컴퓨터공학",
          "연락처" : "111-0000-1010",
          "주민등록번호" : "111111-0000000",
          "메일" : "python@python.py",
          "주소" : "pyCharm",
          "취미" : ["버그 잡기", "들여쓰기"]}

print(myInfo)

delKeyWords = ['연락처', '주민등록번호']

for key in delKeyWords:
    if (key in myInfo):
        del myInfo[key]

print(myInfo)