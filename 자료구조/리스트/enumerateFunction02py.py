# 사용자가 입력한 문자열에서 공백의 개수 출력
message = input('입력: ')
cnt = 0
for idx, val in enumerate(message):
    if val == ' ':
        cnt += 1

print('공백의 개수 : {}개'.format(cnt))