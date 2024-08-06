# 사용자의 아이디, 비밀번호를 이용해서 로그인 프로그램 만들기

members = {
    'qwer':'1234',
    'asdf':'123#$@#@',
    'zxcv':'4567()*&^%',
    'wasd':'1@#$!23!@34'
}
userId = input('ID 입력: ')
userPwd = input('PW 입력: ')

if userId in members:
    if members[userId] == userPwd:
        print('로그인 성공~!!')
    else:
        print('비밀번호 불일치')
else:
    print('존재하지 않는 ID')
