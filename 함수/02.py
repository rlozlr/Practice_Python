# 삼각형, 사각형, 원의 넓이를 반환하는 lambda 함수 만들기

triangleArea = lambda num1, num2: num1 * num2 / 2
squareArea = lambda num1, num2 : num1 * num2
circleArea = lambda r: r * r * 3.14

width = int(input('가로: '))
height = int(input('세로: '))
radius = int(input('반지름: '))

triangle = triangleArea(width, height)
square = squareArea(width, height)
circle = circleArea(radius)

print(f'삼각형 넓이: {triangle}')
print(f'사각형 넓이: {square}')
print(f'원 넓이: {circle}')