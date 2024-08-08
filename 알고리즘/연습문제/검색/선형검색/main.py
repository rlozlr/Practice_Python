# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
'''
1) 검색 모듈은 선형 검색 Algorithm 이용
2) List는 1부터 20까지의 정수 중에서 난수 10개 이용
3) 검색 과정을 로그로 출력
4) 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력
'''
import 선형검색 as lineMod
import random

if __name__ == '__main__':
    rNums = random.sample(range(1, 21), 10)
    searchNum = int(input('찾는 숫자: '))

    resultIdx = lineMod.searchNumberByLineAlgorithm(rNums, searchNum)