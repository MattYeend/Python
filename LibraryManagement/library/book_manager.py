def display_books(library):
    """Display all books in the library."""
    if not library["books"]:
        print("\nNo books available in the library.")
    else:
        print("\nAvailable Books:")
        for book in library["books"]:
            status = "Borrowed" if book["borrowed"] else "Available"
            print(f"- {book['title']} by {book['author']} [{status}]")

def add_book(library):
    """Add a new book to the library."""
    title = input("\nEnter the book title: ").strip()
    author = input("Enter the author: ").strip()

    if title and author:
        library["books"].append({"title": title, "author": author, "borrowed": False})
        print(f"Book '{title}' by {author} added to the library!")
    else:
        print("Both title and author are required.")
