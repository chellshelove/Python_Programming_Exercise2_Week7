# Initial phonebook dictionary
phonebook = {}

while True:
    # Display menu and get user input
    menu = input("Enter a command (input, search, delete, quit): ").lower()

    if menu == "input":
        # Get name and phone number to store
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(f"{name} has been added to the phonebook.")

    elif menu == "search":
        # Get name to search
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"{name}'s phone number is: {phonebook[name]}")
        else:
            print(f"Error: {name} not found in the phonebook.")

    elif menu == "delete":
        # Get name to delete
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"{name} has been deleted from the phonebook.")
        else:
            print(f"Error: {name} not found in the phonebook.")

    elif menu == "quit":
        # Exit the loop
        print("Exiting the program.")
        break

    else:
        print("Invalid command. Please enter input, search, delete, or quit.")