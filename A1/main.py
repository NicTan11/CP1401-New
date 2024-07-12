"""
Replace the contents of this module docstring with your own details
Name: Nickson Tanjodi
Date started: 20/6/2024
GitHub URL: https://github.com/NicTan11/CP1401-New
"""


import csv

# Constants
BOOKS_FILE = 'books.csv'
STATUS_COMPLETED = 'c'
STATUS_UNREAD = 'u'
MENU_CHOICES = ['D', 'A', 'C', 'Q']

def main():
    """Main function to run the book list program."""
    print("Books to Read 1.0 by [Nickson Tanjodi]")
    
    books = load_books(BOOKS_FILE)
    print(f"{len(books)} books loaded.")
    
    while True:
        display_menu()
        choice = input(">>> ").upper()
        if choice == 'D':
            display_books(books)
        elif choice == 'A':
            add_book(books)
        elif choice == 'C':
            complete_book(books)
        elif choice == 'Q':
            save_books(BOOKS_FILE, books)
            print(f"{len(books)} books saved to {BOOKS_FILE}")
            print('"So many books, so little time." - Frank Zappa')
            break
        else:
            print("Invalid menu choice")

def load_books(filename):
    """Load books from a CSV file into a list of lists."""
    books = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty book list.")
    return books

def save_books(filename, books):
    """Save books from a list of lists to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)

def display_menu():
    """Display the menu options to the user."""
    print("\nMenu:")
    print("D - Display books")
    print("A - Add new book")
    print("C - Complete a book")
    print("Q - Quit")

def display_books(books):
    """Display the list of books, sorted by author then by title, with unread books marked."""
    if not books:
        print("No books in the list.")
        return
    
    books.sort(key=lambda x: (x[1], x[0]))
    unread_count = 0
    unread_pages = 0
    print("\nBooks:")
    for i, book in enumerate(books, start=1):
        status = '*' if book[3] == STATUS_UNREAD else ''
        print(f"{status}{i}. {book[0]:<30} by {book[1]:<20} {book[2]:>3} pages")
        if book[3] == STATUS_UNREAD:
            unread_count += 1
            unread_pages += int(book[2])
    
    if unread_count > 0:
        print(f"You still need to read {unread_pages} pages in {unread_count} books.")
    else:
        print("No books left to read. Why not add a new book?")

def add_book(books):
    """Prompt the user to add a new book to the list."""
    title = get_non_empty_string("Title: ")
    author = get_non_empty_string("Author: ")
    pages = get_positive_int("Number of Pages: ")
    
    new_book = [title, author, pages, STATUS_UNREAD]
    books.append(new_book)
    print(f"{title} by {author} ({pages} pages) added.")

def complete_book(books):
    """Prompt the user to mark a book as completed."""
    unread_books = [book for book in books if book[3] == STATUS_UNREAD]
    if not unread_books:
        print("No unread books - well done!")
        return
    
    display_books(unread_books)
    
    while True:
        try:
            book_number = int(input("Enter the number of a book to mark as completed\n>>> "))
            if book_number <= 0:
                print("Number must be > 0")
                continue
            if book_number > len(unread_books):
                print("Invalid book number")
                continue
            
            book_to_complete = unread_books[book_number - 1]
            for book in books:
                if book[0] == book_to_complete[0] and book[1] == book_to_complete[1]:
                    book[3] = STATUS_COMPLETED
                    print(f"{book[0]} by {book[1]} completed!")
                    return
        except ValueError:
            print("Invalid input - please enter a valid number")

def get_non_empty_string(prompt):
    """Prompt the user for a non-empty string."""
    while True:
        result = input(prompt).strip()
        if result:
            return result
        print("Input can not be blank")

def get_positive_int(prompt):
    """Prompt the user for a positive integer."""
    while True:
        try:
            result = int(input(prompt))
            if result > 0:
                return result
            print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")

main()
