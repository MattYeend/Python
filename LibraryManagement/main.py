from Python.LibraryManagement.library.book_manager import display_books, add_book
from Python.LibraryManagement.library.user_manager import borrow_book, return_book
from Python.LibraryManagement.library.data_manager import load_library_data, save_library_data

def main():
    library = load_library_data()

    print("Welcome to the Library Management System!")
    while True:
        print("\nMenu:")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a new book (Admin)")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            display_books(library)
        elif choice == "2":
            borrow_book(library)
        elif choice == "3":
            return_book(library)
        elif choice == "4":
            add_book(library)
        elif choice == "5":
            save_library_data(library)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
