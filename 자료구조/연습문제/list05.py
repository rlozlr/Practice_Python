# 다음 List에서 중복 아이템(숫자)을 제거
numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print('numbers: {}'.format(numbers))

idx = 0
while True:
    if idx >= len(numbers):
        break

    if numbers.count(numbers[idx]) >= 2:
        numbers.remove(numbers[idx])
        continue

    idx += 1

print('numbers : {}'.format(numbers))