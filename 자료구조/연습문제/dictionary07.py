# Dictionary를 이용해서 5명의 회원을 가입 받고 전체 회원 정보를 출력 및 특정 회원 계정 삭제

members = {}

n = 1
while  n < 6:
    mail = input('email: ')
    pw = input('pw: ')

    if mail in members:
        print('사용중인 메일!!!')
        continue
    else:
        members[mail] = pw
        n += 1

for key in members.keys():
    print(f'{key} : {members[key]}')

while True:
    delMail = input('삭제할 메일:')
    
    if delMail in members:
        delPw = input('pw: ')
        if members[delMail] == delPw:
            del members[delMail]
            print('계정 삭제~!!')
            break
        else:
            print('비번 불일치')
    else:
        print('이메일 불일치')

for key in members.keys():
    print(f'{key} : {members[key]}')