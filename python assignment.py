# Function to add a new book to the library
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    book = {
        'title': title,
        'author': author,
        'year': year
    }
    library.append(book)
    print(f"Book '{title}' by {author} added to the library.\n")

# Function to display all books in the library
def view_books(library):
    if not library:
        print("The library is currently empty.\n")
    else:
        print("Listing all books in the library:")
        for index, book in enumerate(library, start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']})")
        print()

# Function to search for a book by title
def search_book(library):
    title = input("Enter the title of the book you want to search for: ")
    found = False
    for book in library:
        if book['title'].lower() == title.lower():
            print(f"Book '{book['title']}' by {book['author']} ({book['year']}) is found in the library.\n")
            found = True
            break
    if not found:
        print(f"Book '{title}' is not found in the library.\n")

# Function to count the total number of books in the library
def count_books(library):
    print(f"Total number of books in the library: {len(library)}\n")

# Function to list all books by a specific author
def list_books_by_author(library):
    author = input("Enter the name of the author to list their books: ")
    found = False
    print(f"Books by {author}:")
    for book in library:
        if book['author'].lower() == author.lower():
            print(f"- {book['title']} ({book['year']})")
            found = True
    if not found:
        print(f"No books found by {author} in the library.\n")
    else:
        print()

# Main program
def main():
    library = []
    while True:
        print("Welcome to the Library Management System")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book by title")
        print("4. Count the total number of books")
        print("5. List all books by an author")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            count_books(library)
        elif choice == '5':
            list_books_by_author(library)
        elif choice == '6':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
