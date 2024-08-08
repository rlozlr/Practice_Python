# 선택정렬 알고리즘을 이용해서 학생 20명의 시험 점수를 오름차순과 내림차순으로 정렬하는 모듈 만들기
# 시험 점수는 50부터 100까지
def sortNumber(ns, asc=True):
    if asc:
        for i in range(len(ns) - 1):
            minIdx = i

            for j in range(i+1, len(ns)):
                if ns[minIdx] > ns[j]:
                    minIdx = j
            ns[i], ns[minIdx] = ns[minIdx], ns[i]

    else:
        for i in range(len(ns) - 1):
            minIdx = i

            for j in range(i + 1, len(ns)):
                if ns[minIdx] < ns[j]:
                    minIdx = j
            ns[i], ns[minIdx] = ns[minIdx], ns[i]

    return ns