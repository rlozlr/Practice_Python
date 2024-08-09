# 학급 전체 학생의 시험 점수에 대한 평균과 최댓값을 구하고 평균과 최댓값의 편차를 출력하는 프로그램을 최대한 Algorithm을 이용해서 만들기
'''
전체 학생 시험 점수
[100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
'''

def getAvg(ns):
    total = 0
    for n in ns:
        total += n

    return total / len(ns)

def getMax(ns):
    maxN = ns[0]
    for n in ns:
        if maxN < n:
            maxN = n

    return maxN

def getDeviation(n1, n2):
    return round(abs(n1 - n2), 2)

