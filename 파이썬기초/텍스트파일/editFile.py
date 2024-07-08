file = open('C:/pythonEx/about_python.txt', 'r', encoding='UTF8')
str = file.read()
print(f'파일 내용: {str}')
file.close()

str = str.replace('Python','파이썬', 2)  # 숫자는 앞에서 순서대로 진행
print(f'수정 내용 확인: {str}')

file = open('C:/pythonEx/about_python.txt', 'w')
file.write(str)
file.close()
