from Library import Library

def main():
    # Create a library object
    library = Library()

    # Adding books to the library
    print("Adding books to the library:")
    library.add_book("1984", 1, "George Orwell")
    library.add_book("Brave New World", 2, "Aldous Huxley")
    library.add_book("To Kill a Mockingbird", 3, "Harper Lee")
    print("\n")

    # Adding members to the library
    print("Adding members to the library:")
    print(library.add_member("Alice", 101, "123 Street Name"))
    print(library.add_member("Bob", 102, "456 Avenue Name"))
    print("\n")

    # Display current library status
    print("Library status:")
    print(library)
    print("\n")

    # Borrowing a book
    print("Borrowing a book:")
    member = library.find_member(101)  # Find member Alice by ID
    book = library.find_book(1)       # Find book "1984" by serial number
    if member and book:
        member.borrow_books(book)
    print("\n")

    # Display library status after borrowing
    print("Library status after borrowing:")
    print(library)
    print("\n")

    # Returning a book
    print("Returning a book:")
    if member and book:
        member.return_book(book)
    print("\n")

    # Display library status after returning
    print("Library status after returning:")
    print(library)
    print("\n")

    # Removing a book
    print("Removing a book:")
    library.remove_book(1)  # Remove book "1984" by serial number
    print("\n")

    # Removing a member
    print("Removing a member:")
    library.remove_member("Alice", 101)
    print("\n")

    # Display final library status
    print("Final library status:")
    print(library)
    


if __name__ == "__main__":
    main()

