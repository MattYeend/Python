from library.book_manager import display_books

from datetime import datetime

def borrow_book(library):
    """Borrow a book from the library."""
    if not library["books"]:
        print("\nNo books available to borrow.")
        return

    display_books(library)
    book_title = input("\nEnter the title of the book you want to borrow: ").strip()

    for book in library["books"]:
        if book["title"].lower() == book_title.lower():
            if book["borrowed"]:
                print(f"The book '{book['title']}' is already borrowed.")
            else:
                borrower = input("Enter your name: ").strip()
                book["borrowed"] = True
                book["borrower"] = borrower
                book["borrow_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"You have borrowed '{book['title']}'!")
            return
    
    print(f"Book '{book_title}' not found in the library.")

def return_book(library):
    """Return a borrowed book to the library."""
    book_title = input("\nEnter the title of the book you want to return: ").strip()

    for book in library["books"]:
        if book["title"].lower() == book_title.lower():
            if book["borrowed"]:
                book["borrowed"] = False
                book["borrower"] = None
                book["borrow_date"] = None
                print(f"Thank you for returning '{book['title']}'!")
            else:
                print(f"The book '{book['title']}' was not borrowed.")
            return
    
    print(f"Book '{book_title}' not found in the library.")
