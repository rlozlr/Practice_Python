import diary

members = {}
uri = 'C:/pythonEx/'

def printMembers():
    for m in members.keys():
        print(f'ID: {m} \t PW: {members[m]}')

while True:
    selectNum = int(input('1. 회원가입 | 2. 한줄일기쓰기 | 3.일기보기 | 4.종료'))

    if selectNum == 1:
        mId = input('input ID: ')
        mPw = input('input PW: ')
        members[mId] = mPw
        printMembers()

    elif selectNum == 2:
        mId = input('input ID: ')
        mPw = input('input PW: ')

        if mId in members and members[mId] == mPw:
            print('login success~!!')
            failName = 'myDairy_'+ mId + '.txt'
            data = input('오늘 하루 인상 깊은 일을 기록하세요. ')
            diary.writeDiary(uri, failName, data)

        else:
            print('login Fail~!!')
            printMembers()

    elif selectNum == 3:
        mId = input('input ID: ')
        mPw = input('input PW: ')

        if mId in members and members[mId] == mPw:
            print('login success~!!')
            failName = 'myDairy_'+ mId + '.txt'
            datas = diary.readDiary(uri, failName)
            for d in datas:
                print(d, end='')

        else:
            print('login Fail~!!')
            printMembers()

    elif selectNum == 4:
        print('Bye~!!')
        break
