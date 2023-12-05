# customer_main.py

def display_customer_menu():
    print("\n==== Customer Operations ====")
    print("1. Check Balance")
    print("2. Buy a Book")
    print("3. Rent a Book")
    print("4. Return a Rented Book")
    print("5. Show Rented Books")
    print("6. Logout")

def customer_operations(customer_username):
    balance = 100  # Initial balance for demonstration purposes
    rented_books = []

    while True:
        display_customer_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print(f"Current Balance: ${balance}")
        elif choice == "2":
            # Display available books
            display_available_books()
            # Buy a book
            buy_book(balance)
        elif choice == "3":
            book_rent_price = 5  # Price for renting a book
            if balance >= book_rent_price:
                balance -= book_rent_price
                rented_book_title = input("Enter the title of the book to rent: ")
                rented_books.append(rented_book_title)
                print("Book rented successfully!")
            else:
                print("Insufficient balance to rent the book.")
        elif choice == "4":
            # Return a rented book
            return_rented_book(rented_books)
        elif choice == "5":
            if rented_books:
                print("Rented Books:")
                for book_title in rented_books:
                    print(f"- {book_title}")
            else:
                print("No books rented.")
        elif choice == "6":
            print("Logging out. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def display_available_books():
    print("\n==== Available Books ====")
    try:
        with open("library.txt", "r") as file:
            for line in file:
                title, _, _ = line.strip().split(',')
                print(f"- {title}")
    except FileNotFoundError:
        print("No books in the library yet.")

def buy_book(balance):
    book_title = input("Enter the title of the book to buy: ")
    book_price = 10  # Price for buying a book

    try:
        with open("library.txt", "r") as file:
            found = False
            for line in file:
                title, _, _ = line.strip().split(',')
                if title.lower() == book_title.lower():
                    found = True
                    break

            if found:
                if balance >= book_price:
                    balance -= book_price
                    print(f"Book '{book_title}' bought successfully!")
                else:
                    print("Insufficient balance to buy the book.")
            else:
                print("Book not found in the library.")
    except FileNotFoundError:
        print("No books in the library yet.")

def return_rented_book(rented_books):
    if rented_books:
        print("Rented Books:")
        for i, book_title in enumerate(rented_books, start=1):
            print(f"{i}. {book_title}")

        choice = input("Enter the number of the book to return (0 to cancel): ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(rented_books):
                returned_book = rented_books.pop(index)
                print(f"Book '{returned_book}' returned successfully!")
            elif index == -1:
                print("Returning canceled.")
            else:
                print("Invalid book number.")
        else:
            print("Invalid input. Please enter a number.")
    else:
        print("No books rented.")
