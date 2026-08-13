from datetime import datetime

class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.issued_to = None
        self.issued_date = None

    def issue(self, borrower):
        self.issued_to = borrower
        self.issued_date = datetime.today().date()

books = {}
def add_books(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    isbn = input("Enter isbn: ")
    b = Book(title, author, genre, isbn)
    books[isbn] = b
    print("Book added successfully!")

def view_books(books):
    if not books:
        print("No books in the library")
        return
    for isbn, book in books.items():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}")


def status_book(books):
    isbn = input("Enter ISBN of the book: ")
    book = books[isbn]
    if not book.issued_to:
        print(f"The book - {book.title} is available")
        return
    else:
        print(f"'{book.title}' is currently issued by - {book.issued_to}")
        print(f"Issued on (date) - {book.issued_date}")

    days_passed = (datetime.today().date() - book.issued_date).days
    if days_passed > 15:
        overdue_days = days_passed - 15
        fine = overdue_days*50
        print(f"OVERDUE by {overdue_days}. Fine : Rs. {fine}")
    else: 
        days_left = 15 - days_passed
        print(f" Due in {days_left} days. No fine yet.")

def return_book(books):
    isbn = input("Enter ISBN of the book to be returned: ")
    
    if isbn not in books:
        print("Book not found!")
        return
    book = books[isbn]
    if not book.issued_to:
        print(f"The '{book.title}' is available.")
        return

    days_passed = (datetime.today().date() - book.issued_date).days
    if days_passed > 15:
        overdue_days = days_passed - 15
        fine = overdue_days*50
        print(f"OVERDUE by {overdue_days}. Fine : Rs. {fine}")
    else: 
        print("No fine to be paid")

    book.issued_to = None
    book.issued_date = None

    print("BOOK RETURNED SUCCESSFULLY!")

        
while True: 
    print("\n----- MENU -----")
    print("1. Add a new Book")
    print("2. View all book details")
    print("3. Book status")
    print("4. Issue Book")
    print("5. Return book")
    print("6. Exit")

    ch = int(input("Enter your choice: (1-6):"))

    if ch == 1:
        add_books(books)
    elif ch == 2:
        view_books(books)
    elif ch == 3:
        status_book(books)
    elif ch == 4:
        isbn = input("Enter ISBN of the book to be issued: ")
        borrower =  input("Enter the name of the borrower: ")
        books[isbn].issue(borrower)
        print("Book isssued successfully!!")
    elif ch == 5:
        return_book(books)
    elif ch == 6:
        print("---- THE END ----")
        break
    else:
        print("Invalid")
        