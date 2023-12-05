# main.py

rented_books = []  # Shared list to keep track of rented books

def display_menu():
    print("\n==== Library Management System ====")
    print("1. Add New Book")
    print("2. Display Books")
    print("3. Search for a Book")
    print("4. Delete a Book")
    print("5. Display Rented Books")
    print("6. Exit")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    price = input("Enter the price: ")

    with open("library.txt", "a") as file:
        file.write(f"{title},{author},{price}\n")

    print("Book added successfully!")

def display_books():
    print("\n==== List of Books ====")
    try:
        with open("library.txt", "r") as file:
            for line in file:
                title, author, price = line.strip().split(',')
                print(f"Title: {title}, Author: {author}, Price: {price}")
    except FileNotFoundError:
        print("No books in the library yet.")

def search_book():
    title_to_search = input("Enter the title of the book to search: ")
    found = False

    try:
        with open("library.txt", "r") as file:
            for line in file:
                title, author, price = line.strip().split(',')
                if title.lower() == title_to_search.lower():
                    print(f"Book Found!\nTitle: {title}, Author: {author}, Price: {price}")
                    found = True
                    break
        if not found:
            print("Book not found.")
    except FileNotFoundError:
        print("No books in the library yet.")

def delete_book():
    title_to_delete = input("Enter the title of the book to delete: ")
    found = False

    try:
        with open("library.txt", "r") as file:
            lines = file.readlines()
        with open("library.txt", "w") as file:
            for line in lines:
                title, _, _ = line.strip().split(',')
                if title.lower() != title_to_delete.lower():
                    file.write(line)
                else:
                    print(f"Book '{title}' deleted successfully.")
                    found = True
        if not found:
            print("Book not found.")
    except FileNotFoundError:
        print("No books in the library yet.")

def display_rented_books():
    if rented_books:
        print("\n==== Rented Books ====")
        for book_title in rented_books:
            print(f"- {book_title}")
    else:
        print("No books rented.")

def staff_operations():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            display_rented_books()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    staff_operations()
