def staff_login():
    staff_username = input("Enter staff username: ")
    staff_password = input("Enter staff password: ")

    if staff_username == "mrlx" and staff_password == "123":
        print("Staff login successful.")
        # Connect to main.py or perform staff-related actions
        import main
        main.staff_operations()
    else:
        print("Incorrect staff credentials.")

def customer_login():
    customer_username = input("Enter customer username: ")
    customer_password = input("Enter customer password: ")

    if customer_username == "car" and customer_password == "123":
        print("Customer login successful.")
        # Connect to customer_main.py for customer operations
        import customer_main
        customer_main.customer_operations(customer_username)
    else:
        print("Incorrect customer credentials.")

if __name__ == "__main__":
    print("==== Login System ====")
    print("1. Staff Login")
    print("2. Customer Login")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        staff_login()
    elif choice == "2":
        customer_login()
    else:
        print("Invalid choice. Please enter 1 or 2.")
