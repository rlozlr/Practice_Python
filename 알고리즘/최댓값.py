# List에서 ASCII코드가 가장 큰 값을 찾는 Algorithm 만들기
class MaxAlgorithm:

    def __init__(self, cs):
        self.chars = cs
        self.maxChar = 0

    def getMaxChar(self):
        self.maxChar = self.chars[0]

        for c in self.chars:
            if ord(self.maxChar) < ord(c):
                self.maxChar = c
        return self.maxChar

chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
mc = MaxAlgorithm(chars)
maxChar = mc.getMaxChar()
print(f'maxChar: {maxChar}')
