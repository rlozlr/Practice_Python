import math

radius = float(input('반지름(cm) 입력 : '))

circleArea = math.pi * radius ** 2
circleLenth = 2 * math.pi * radius

print('원의 넓이: %d' % circleArea)
print('원의 둘레길이: %d' % circleLenth)
print('원의 넓이: %.1f' % circleArea)
print('원의 둘레길이: %.1f' % circleLenth)

