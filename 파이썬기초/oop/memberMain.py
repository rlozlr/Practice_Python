import member as mb

mems = mb.MemberRepository()

for i in range(3):
    userId = input('아이디 >>> ')
    userPw = input('비밀번호 >>> ')
    mem = mb.Member(userId, userPw)
    mems.addMember(mem)

mems.printMember()
mems.loginMember('abcd@abcd.com', '1234')
mems.loginMember('qwer@qwer.com', '1234')
mems.loginMember('zxcv@zxcv.com', '1234')

mems.removeMember('abcd@abcd.com', '1234')
mems.printMember()