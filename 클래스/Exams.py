'''
중간고사 클래스와 기말고사 클래스를 상속관계로 만들고 각각의 점수를 초기화.
총점 및 평균을 반환하는 기능도 만들기.
'''
class midExam:

    def __init__(self, num1, num2, num3):
        self.mid_kor = num1
        self.mid_eng = num2
        self.mid_math = num3

    def printScores(self):
        print(f'국어: {self.mid_kor}점')
        print(f'영어: {self.mid_eng}점')
        print(f'수학: {self.mid_math}점')

class finalExam(midExam):

    def __init__(self, num1, num2, num3, num4):
        super().__init__(num1, num2, num3)
        self.mid_science = num4

    def printScores(self):
        super().printScores()
        print(f'과학: {self.mid_science}점')

    def totalSum(self):
        sum = self.mid_kor + self.mid_eng + self.mid_math + self.mid_science
        return sum

    def totalAvg(self):
        return self.totalSum() /4

exam = finalExam(80, 71, 100, 100)
exam.printScores()

print(f'총점: {exam.totalSum()}')
print(f'평균: {exam.totalAvg()}')
