# 로또 번호 생성기 프로그램을 만들고 파일에 번호를 출력
import random

uri = 'C:/pythonEx/'

def writeNum(nums) :
    for idx, num in enumerate(nums):
        with open(uri + 'lotto.txt', 'a') as f:
            if idx < (len(nums) -2 ):
                f.write(str(num) + ', ')
            elif idx == (len(nums) - 2):
                f.write(str(num))
            elif idx == (len(nums) - 1):
                f.write('\n')
                f.write('bonus: ' + str(num))
                f.write('\n')

randNum = random.sample(range(1, 46), 7)
print(f'랜덤번호: {randNum}')
writeNum(randNum)