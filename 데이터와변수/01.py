width = float(input('가로 길이: '))
height = float(input('세로 길이: '))

triangle = width * height /2
square = width * height
print ('-' * 20)
print('삼각형 넓이 : %f' % triangle)
print('사각형 넓이 : %f' % square)
print('삼각형 넓이 : %2f' % triangle)
print('사각형 넓이 : %2f' % square)
print ('-' * 20)