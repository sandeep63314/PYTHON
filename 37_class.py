import datetime
class  library:
    issue = []
    def __init__(self,books):
        self.books = books
    def issuebook(self,bookname,issuedate):
        if bookname in self.books:
            self.books.remove(bookname)
            library.issue.append([bookname,issuedate,None])
        else:
            print('Sorry...I don\'t find your book')
    def returnbook(self,bookname,returndate):
        bookcheck = [(b[0],b[1][0]) for b in enumerate(library.issue) if b[1][2] == None and b[1][0] == bookname]
        if bookcheck == []:
            print('This book was not issued from this library')
        else:
            bookstatus = library.issue[bookcheck[0][0]]
            bookstatus[2] = returndate
            library.issue[bookcheck[0][0]] = bookstatus
            self.books.append(bookname)

bk = ['Harry Potter','Sherlock Holmes','3 mistakes of my life','Lord of the rings','Game of thrones']
lib = library(bk)
ch = 'Y'
while ch in ('Y','y'):
    ch = input('1.ISSUE A BOOK\n2.RETURN A BOOK\n3.CHECK STATUS OF ANY BOOKS\nEnter your choice of operation:')
    if int(ch) == 1:
        book = input('Enter the name of the book:')
        lib.issuebook(book,datetime.datetime.now())
    elif int(ch) == 2:
        book = input('Enter the name of the book:')
        lib.returnbook(book,datetime.datetime.now())
    elif int(ch) == 3:
        book = input('Enter the name of the book:')

        if book in [bk[0] for bk in library.issue]:
            booknames = [(b[0], b[1], b[2]) for b in library.issue if b[0] == book]
            for bookstatus in booknames:
                b,i,r = bookstatus
                print(f'BOOK NAME:{b}\tISSUE DATE:{i}\tRETURN DATE:{r}')
        else:
            if book in lib.books:
                print('This book is not issued yet')
            else:
                print('This book is not available in the library')
    print('List of books available in library are : -')
    for b in lib.books:
        print(b)
    ch = input('Do you want to continue...Press \'Y|y\'. Press any key to abort. ')