# 다음 Tuple 요구사항에 맞춰 아이템을 슬라이스
'''
idx 0 ~ 3 / 2 ~ 4 / 3 ~ / 2 ~ -2 / 0 ~ (+3)
'''
numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)

print(f'numbers[:4] : {numbers[:4]}')
print(f'numbers[2:5] : {numbers[2:5]}')
print(f'numbers[3:] : {numbers[3:]}')
print(f'numbers[2:-1] : {numbers[2:-1]}')
print(f'numbers[::3] : {numbers[::3]}')

# 최솟값 / 최댓값
print(f'최솟값 : {min(numbers)}')
print(f'최솟값 idx : {numbers.index(min(numbers))}')

print(f'최댓값 : {max(numbers)}')
print(f'최댓값 idx : {numbers.index(max(numbers))}')

