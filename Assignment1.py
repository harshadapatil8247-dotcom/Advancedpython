class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed = ""


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book Added")

    def register_patron(self, name):
        self.patrons.append(Patron(name))
        print("Patron Registered")

    def issue_book(self, title, name):
        for book in self.books:
            if book.title == title and book.available:
                for patron in self.patrons:
                    if patron.name == name:
                        book.available = False
                        patron.borrowed = title
                        print("Book Issued")
                        return
        print("Book Not Available")

    def return_book(self, title, name):
        for book in self.books:
            if book.title == title:
                book.available = True
        for patron in self.patrons:
            if patron.name == name:
                patron.borrowed = ""
        print("Book Returned")

    def display(self):
        print("\nBooks:")
        for book in self.books:
            print(book.title, "-", book.author, "-", book.available)

        print("\nPatrons:")
        for patron in self.patrons:
            print(patron.name, "-", patron.borrowed)


lib = Library()

lib.add_book("Python", "Guido")
lib.add_book("Java", "James")

lib.register_patron("Rahul")
lib.register_patron("Priya")

lib.issue_book("Python", "Rahul")
lib.display()

lib.return_book("Python", "Rahul")
lib.display()