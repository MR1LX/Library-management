import tkinter as tk
from tkinter import messagebox

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")

        self.username_label = tk.Label(master, text="Username:")
        self.username_entry = tk.Entry(master)
        self.password_label = tk.Label(master, text="Password:")
        self.password_entry = tk.Entry(master, show="*")
        self.login_button = tk.Button(master, text="Login", command=self.login)

        self.username_label.pack(pady=5)
        self.username_entry.pack(pady=5)
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "mrlx" and password == "123":
            self.show_staff_menu()
        elif username == "car" and password == "123":
            self.show_customer_menu()
        else:
            messagebox.showerror("Login Error", "Incorrect credentials")

    def show_staff_menu(self):
        staff_menu = tk.Toplevel(self.master)
        staff_menu.title("Staff Menu")

        add_book_button = tk.Button(staff_menu, text="Add New Book", command=self.dummy_function)
        display_books_button = tk.Button(staff_menu, text="Display Books", command=self.dummy_function)
        search_book_button = tk.Button(staff_menu, text="Search for a Book", command=self.dummy_function)
        delete_book_button = tk.Button(staff_menu, text="Delete a Book", command=self.dummy_function)
        display_rented_books_button = tk.Button(staff_menu, text="Display Rented Books", command=self.dummy_function)
        logout_button = tk.Button(staff_menu, text="Logout", command=staff_menu.destroy)

        add_book_button.pack(pady=5)
        display_books_button.pack(pady=5)
        search_book_button.pack(pady=5)
        delete_book_button.pack(pady=5)
        display_rented_books_button.pack(pady=5)
        logout_button.pack(pady=10)

    def show_customer_menu(self):
        customer_menu = tk.Toplevel(self.master)
        customer_menu.title("Customer Menu")

        check_balance_button = tk.Button(customer_menu, text="Check Balance", command=self.dummy_function)
        buy_book_button = tk.Button(customer_menu, text="Buy a Book", command=self.dummy_function)
        rent_book_button = tk.Button(customer_menu, text="Rent a Book", command=self.dummy_function)
        return_rented_book_button = tk.Button(customer_menu, text="Return a Rented Book", command=self.dummy_function)
        show_rented_books_button = tk.Button(customer_menu, text="Show Rented Books", command=self.dummy_function)
        logout_button = tk.Button(customer_menu, text="Logout", command=customer_menu.destroy)

        check_balance_button.pack(pady=5)
        buy_book_button.pack(pady=5)
        rent_book_button.pack(pady=5)
        return_rented_book_button.pack(pady=5)
        show_rented_books_button.pack(pady=5)
        logout_button.pack(pady=10)

    def dummy_function(self):
        messagebox.showinfo("Functionality", "This functionality will be implemented later.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
