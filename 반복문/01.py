'''
1부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합 그리고 팩토리얼을 출력하는 프로그램
'''
num = int(input('정수 입력: '))
allSum, oddSum, evenSum, factorial = 0, 0, 0, 1

for i in range (1, num+1):
    allSum += i

    if (i % 2 == 1):
       oddSum += i
    else:
       evenSum += i

    factorial *= i

print('합 결과 : {}'.format(allSum))
print('홀수 합 결과 : {}'.format(oddSum))
print('짝수 합 결과 : {}'.format(evenSum))
print('팩토리얼 결과 : {:,}'.format(factorial))   # factorialFormed = format(factorial, ',')과 같음ㅁ

