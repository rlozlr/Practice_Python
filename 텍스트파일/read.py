file = open('C:/pythonEx/test.txt', 'r')
str = file.read()
print(f'파일 내용: {str}')
file.close()