class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                print(f"წიგნი '{book.title}' უკვე არსებობს ბიბლიოთეკაში")
                return
        self.books.append(book)
        print(f"წიგნი '{book.title}' დაემატა")

    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                print(f"წიგნი '{title}' წაიშალა")
                return
        print(f"წიგნი '{title}' ვერ მოიძებნა")

    def list_books(self):
        if not self.books:
            print("ბიბლიოთეკა ცარიელია")
            return
        for b in self.books:
            print(f"{b.title} - {b.author} ({b.year})")