class Book:

    def __init__(self, name, price, isbn):
        self.bName = name
        self.bPrice = price
        self.bIsbn = isbn

class BookRepository:
    def __init__(self):
        self.bookDic = {}

    def registBook(self, b):
        self.bookDic[b.bIsbn] = b

    def removeBook(self, isbn):
        del self.bookDic[isbn]

    def printBooksInfo(self):
        for isbn in self.bookDic.keys():
            b = self.bookDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
            
    def printBookInfo(self, isbn):
        if isbn in self.bookDic:
            b = self.bookDic[isbn]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
        else:
            print('존재하지 않음')
