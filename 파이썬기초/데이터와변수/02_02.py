pwd = input('비밀번호 입력: ')
privateNum = input('주민번호 입력(xxxxxx-xxxxxxx): ')
pwdStar = '*' * len(pwd)

print(f'비밀번호 출력: {pwdStar}')
print(f'주민번호 출력: ', end='')

for i in range(len(privateNum)):
    if(i > 7):
        print('*', end='')
    else:
        print(privateNum[i], end='')

