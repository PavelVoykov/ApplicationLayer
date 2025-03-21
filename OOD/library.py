class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Magazine(Book):
    def __init__(self, title, issue_number, isbn):
        super().__init__(title, "N/A", isbn)
        self.issue_number = issue_number
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []

    def borrow_item(self, item):
        if not item.is_borrowed:
            self.borrowed_items.append(item)
            item.is_borrowed = True
            return True
        return False

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            item.is_borrowed = False
            return True
        return False
class Library:
    def __init__(self):
        self.books = []
        self.magazines = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_magazine(self, magazine):
        self.magazines.append(magazine)

    def register_member(self, name):
        member_id = len(self.members) + 1
        new_member = Member(name, member_id)
        self.members.append(new_member)
        return new_member

    def find_member(self, member_id):
        return next((member for member in self.members if member.member_id == member_id), None)

    def find_item(self, isbn):
        for item in self.books + self.magazines:
            if item.isbn == isbn:
                return item
        return None

    def borrow_item(self, member_id, isbn):
        member = self.find_member(member_id)
        item = self.find_item(isbn)
        if member and item:
            return member.borrow_item(item)
        return False

    def return_item(self, member_id, isbn):
        member = self.find_member(member_id)
        item = self.find_item(isbn)
        if member and item:
            return member.return_item(item)
        return False
def main():
    library = Library()

    while True:
        print("\nLibrary Administration System")
        print("1. Register new member")
        print("2. Add book")
        print("3. Add magazine")
        print("4. Borrow item")
        print("5. Return item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter member name: ")
            member = library.register_member(name)
            print(f"Member registered with ID: {member.member_id}")

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("Book added successfully")

        elif choice == "3":
            title = input("Enter magazine title: ")
            issue_number = input("Enter magazine issue number: ")
            isbn = input("Enter magazine ISBN: ")
            library.add_magazine(Magazine(title, issue_number, isbn))
            print("Magazine added successfully")

        elif choice == "4":
            member_id = int(input("Enter member ID: "))
            isbn = input("Enter item ISBN: ")
            if library.borrow_item(member_id, isbn):
                print("Item borrowed successfully")
            else:
                print("Failed to borrow item")

        elif choice == "5":
            member_id = int(input("Enter member ID: "))
            isbn = input("Enter item ISBN: ")
            if library.return_item(member_id, isbn):
                print("Item returned successfully")
            else:
                print("Failed to return item")

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

