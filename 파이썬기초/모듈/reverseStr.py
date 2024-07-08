# 문자열을 거꾸로 반환하는 모듈
def reverseStr(str):
    revStr = ''
    for c in str:
        revStr = c + revStr

    return revStr
