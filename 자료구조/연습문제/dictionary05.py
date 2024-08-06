# 다음 문구를 공백으로 구분하여 List에 저장한 후, Index와 단어를 이용해서 Dictionary에 저장

aboutPython = '파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다.'

wordList = aboutPython.split()
print(wordList)

dic = {}

for idx, word in enumerate(wordList):
    dic[idx] = word

print(dic)