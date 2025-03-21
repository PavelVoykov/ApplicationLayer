class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added book: {title} by {author}")

    def register_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Registered new member: {name}")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title and not b.is_borrowed), None)

        if member and book:
            book.is_borrowed = True
            member.borrowed_books.append(book)
            print(f"{member_name} has borrowed {book_title}")
        else:
            print("Member or book not found, or book is already borrowed")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in member.borrowed_books if b.title == book_title), None)

        if member and book:
            book.is_borrowed = False
            member.borrowed_books.remove(book)
            print(f"{member_name} has returned {book_title}")
        else:
            print("Member or book not found")

def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            name = input("Enter member name: ")
            library.register_member(name)
        elif choice == '3':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            library.borrow_book(member_name, book_title)
        elif choice == '4':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            library.return_book(member_name, book_title)
        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
