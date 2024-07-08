import book as bk

myBookRepository = bk.BookRepository()
myBookRepository.registBook(bk.Book('python', 20000, '123456789'))
myBookRepository.registBook(bk.Book('java', 20000, '65787795'))
myBookRepository.registBook(bk.Book('cpp', 20000, '4758869'))

myBookRepository.printBooksInfo()
print()
myBookRepository.printBookInfo('123456789')
myBookRepository.printBookInfo('65787795')
myBookRepository.printBookInfo('4758869')
print()
myBookRepository.removeBook('65787795')
myBookRepository.printBooksInfo()