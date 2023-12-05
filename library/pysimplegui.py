import PySimpleGUI as sg

def main_menu():
    layout = [
        [sg.Text("Library Management System", size=(30, 1), font=("Helvetica", 20), justification='center')],
        [sg.Button("Staff Login", size=(20, 2))],
        [sg.Button("Customer Login", size=(20, 2))],
        [sg.Button("Exit", size=(20, 2))]
    ]

    window = sg.Window("Main Menu", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Staff Login":
            staff_login()
        elif event == "Customer Login":
            customer_login()

    window.close()

def staff_login():
    layout = [
        [sg.Text("Staff Login", size=(30, 1), font=("Helvetica", 20), justification='center')],
        [sg.Text("Username:"), sg.InputText(key="username")],
        [sg.Text("Password:"), sg.InputText(key="password", password_char="*")],
        [sg.Button("Login"), sg.Button("Back")]
    ]

    window = sg.Window("Staff Login", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Back":
            break
        elif event == "Login":
            if values["username"] == "mrlx" and values["password"] == "123":
                sg.popup("Staff login successful", title="Success")
                staff_menu()

    window.close()

def staff_menu():
    layout = [
        [sg.Text("Staff Menu", size=(30, 1), font=("Helvetica", 20), justification='center')],
        [sg.Button("Add New Book", size=(20, 2))],
        [sg.Button("Display Books", size=(20, 2))],
        [sg.Button("Search for a Book", size=(20, 2))],
        [sg.Button("Delete a Book", size=(20, 2))],
        [sg.Button("Display Rented Books", size=(20, 2))],
        [sg.Button("Logout", size=(20, 2))]
    ]

    window = sg.Window("Staff Menu", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Logout":
            break
        elif event == "Add New Book":
            sg.popup("Add New Book functionality", title="Functionality")
        elif event == "Display Books":
            sg.popup("Display Books functionality", title="Functionality")
        elif event == "Search for a Book":
            sg.popup("Search for a Book functionality", title="Functionality")
        elif event == "Delete a Book":
            sg.popup("Delete a Book functionality", title="Functionality")
        elif event == "Display Rented Books":
            sg.popup("Display Rented Books functionality", title="Functionality")

    window.close()

def customer_login():
    layout = [
        [sg.Text("Customer Login", size=(30, 1), font=("Helvetica", 20), justification='center')],
        [sg.Text("Username:"), sg.InputText(key="username")],
        [sg.Text("Password:"), sg.InputText(key="password", password_char="*")],
        [sg.Button("Login"), sg.Button("Back")]
    ]

    window = sg.Window("Customer Login", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Back":
            break
        elif event == "Login":
            if values["username"] == "car" and values["password"] == "123":
                sg.popup("Customer login successful", title="Success")
                customer_menu()

    window.close()

def customer_menu():
    layout = [
        [sg.Text("Customer Menu", size=(30, 1), font=("Helvetica", 20), justification='center')],
        [sg.Button("Check Balance", size=(20, 2))],
        [sg.Button("Buy a Book", size=(20, 2))],
        [sg.Button("Rent a Book", size=(20, 2))],
        [sg.Button("Return a Rented Book", size=(20, 2))],
        [sg.Button("Show Rented Books", size=(20, 2))],
        [sg.Button("Logout", size=(20, 2))]
    ]

    window = sg.Window("Customer Menu", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Logout":
            break
        elif event == "Check Balance":
            sg.popup("Check Balance functionality", title="Functionality")
        elif event == "Buy a Book":
            sg.popup("Buy a Book functionality", title="Functionality")
        elif event == "Rent a Book":
            sg.popup("Rent a Book functionality", title="Functionality")
        elif event == "Return a Rented Book":
            sg.popup("Return a Rented Book functionality", title="Functionality")
        elif event == "Show Rented Books":
            sg.popup("Show Rented Books functionality", title="Functionality")

    window.close()

if __name__ == "__main__":
    main_menu()
