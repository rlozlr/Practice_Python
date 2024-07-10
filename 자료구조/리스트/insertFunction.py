# 오름차순으로 정렬되어 있는 숫자들에 사용자가 입력한 정수를 추가
# (단, 추가 후에도 오름차순 정렬 유지)

numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
inputNum = int(input("숫자: "))
targetIdx = 0

for idx, num in enumerate(numbers):
    print(idx, num)

    if targetIdx == 0 and inputNum < num:
        targetIdx = idx

numbers.insert(targetIdx, inputNum)
print(numbers)
