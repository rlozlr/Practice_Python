# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들기
'''
1) 검색 모듈은 선형 검색 Algorithm 이용
2) List는 1부터 20까지의 정수 중에서 난수 10개 이용
3) 검색 과정을 로그로 출력
4) 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력
'''

def searchNumberByLineAlgorithm(ns, sn):
    searchResultIdx = -1

    print(f'Number: {ns}')

    for i, n in enumerate(ns):
        if n == sn:
            searchResultIdx = i
            print(f'[{sn}]은/는 [{searchResultIdx +1}]번째에 위치하고 있습니다.')
            print(f'Index는 {searchResultIdx}입니다.')
            break

    if searchResultIdx == -1:
        print(f'[{sn}]은/는 찾을 수 없습니다.')
        print(f'searchResultIdx: {searchResultIdx}')

    # print(f'Search Numbers: {sn}')
