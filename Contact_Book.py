def display_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("\nEnter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"\nContact for {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nYour contact book is empty!")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(contacts):
    name = input("\nEnter the name of the contact to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"\nContact Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print(f"\nNo contact found with the name '{name}'.")

def delete_contact(contacts):
    name = input("\nEnter the name of the contact to delete: ")
    for index, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            deleted_contact = contacts.pop(index)
            print(f"\nContact for {deleted_contact['name']} has been deleted.")
            return
    print(f"\nNo contact found with the name '{name}' to delete.")

contacts = []
while True:
    display_menu()
    choice = input("\nChoose an option (1-5): ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a number between 1 and 5.")
