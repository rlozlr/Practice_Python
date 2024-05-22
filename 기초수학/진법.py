# 10진수를 X진수로 변환
dNum = 30   # 10진수
print('10진수를 X진수로 변환')
print('2진수: {}'.format(bin(dNum)))   # 0b는 해당 숫자가 2진수임을 나타냄
print('8진수: {}'.format(oct(dNum)))   # 0o는 해당 숫자가 8진수임을 나타냄
print('16진수: {}'.format(hex(dNum)))  # 0x는 해당 숫자가 16진수임을 나타냄
print('{0:#b}, {0:#o}, {0:#x}'.format(dNum))    # 다른 방법
# 반환결과는 모두 문자열이다.
print()
# X진수를 10진수로 변환
print('X진수를 10진수로 변환')
print('2진수(0b11110) -> 10진수({})'.format(int('0b11110', 2)))
print('8진수(0o36) -> 10진수({})'.format(int('0o36', 8)))
print('16진수(0x1e) -> 10진수({})'.format(int('0x1e', 16)))
print()
# 2진수를 X진수로 변환
print('2진수를 X진수로 변환')
print('2진수(0b11110) -> 8진수({})'.format(oct(0b11110)))
print('2진수(0b11110) -> 10진수({})'.format(int(0b11110)))
print('2진수(0b11110) -> 16진수({})'.format(hex(0b11110)))
print()

# 8진수를 X진수로 변환
print('8진수를 X진수로 변환')
print('8진수(0o36) -> 2진수({})'.format(bin(0o36)))
print('8진수(0o36) -> 10진수({})'.format(int(0o36)))
print('8진수(0o36) -> 16진수({})'.format(hex(0o36)))
print()

# 16진수를 X진수로 변환
print('16진수를 X진수로 변환')
print('16진수(0x1e) -> 2진수({})'.format(bin(0x1e)))
print('16진수(0x1e) -> 8진수({})'.format(oct(0x1e)))
print('16진수(0x1e) -> 10진수({})'.format(int(0x1e)))
print()