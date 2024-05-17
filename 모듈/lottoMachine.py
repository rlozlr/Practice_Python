# 로또 번호(6개)를 출력하는 모듈
import random

def getLottoNumber():
    num = random.sample(range(1, 45), 6)
    return num