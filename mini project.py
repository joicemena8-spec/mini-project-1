class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def get_status(self):
        return "Available" if self.available else "Borrowed"

    def show_info(self):
        print("\n--- Book Info ---")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", self.get_status())
        print("---------------------")

# Global List
library = []

def add_book():
    print("\nAdd New Book")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = Book(title, author)
    library.append(book)
    print(f"\nBook '{title}' added successfully!")

def show_all_books():
    if len(library) == 0:
        print("\nNo books found.")
        return

    print("\n=== All Books ===")
    for book in library:
        book.show_info()

def find_book():
    title = input("\nEnter book title to search: ")
    found = False
    for book in library:
        if book.title.lower() == title.lower(): # Match template's exact search
            book.show_info()
            found = True
            break
    if not found:
        print(f"\nBook '{title}' not found.")

def delete_book():
    title = input("\nEnter book title to delete: ")
    for book in library:
        if book.title.lower() == title.lower():
            library.remove(book)
            print(f"\nBook '{title}' deleted successfully!")
            return
    print(f"\nBook '{title}' not found.")

# Lambda Example: Count Available Books
def show_stats():
    if not library:
        print("\nLibrary is empty.")
        return
    # Example of using a lambda to filter available books
    available_books = list(filter(lambda b: b.available == True, library))
    print(f"\nTotal books: {len(library)}")
    print(f"Available books: {len(available_books)}")

def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            find_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Try again.")

main()