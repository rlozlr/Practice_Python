# 나의 정보(이름, 전공, 메일, 주소 등)를 Dictionary에 저장하고 '[]'와 'get()' 함수를 이용해서 조회하고 출력

myInfo = {"이름" : "파이",
          "전공" : "컴퓨터공학",
          "메일" : "python@python.py",
          "주소" : "pyCharm",
          "취미" : ["버그 잡기", "들여쓰기"]}

print('---- 나의 정보 ----')
for key in myInfo:
    print('{} : {}'.format(key, myInfo.get(key)))