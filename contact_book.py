import json


def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)


def is_email_valid(email):
    if '@' and '.' in email:
        return True
    return False


def add_contact(name, phone_number, email=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"The name: {name} already exists!")

        if contact['phone_number'].lower() == name.lower():
            print(f'The phone: {phone_number} already exists!')

            if email:
                for contact in contacts:
                    if contact.get('email') and contact['email'].lower() == email.lower():
                        print(f"The email: {email} already exists!")
            break

    new_contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"{name} was added successfully")


def list_contacts():
    if not contacts:
        print("No contacts in the book.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact.get('email', 'N/A')}")


contacts = load_contacts()


def search_contact(name):
    found = False
    for contact in contacts:
        if name.lower() in contact['name'].lower():
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact.get('email', 'N/A')}")
            found = True

    if not found:
        print(f"No contacts found matching the name '{name}'.")


def delete_contact(name):
    global contacts
    found = False

    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            save_contacts(contacts)
            print(f"Contact '{name}' deleted successfully.")
            found = True
            break

    if not found:
        print(f"Contact '{name}' not found.")


def main_menu():

    while True:
        print('1. Add Contact.')
        print('2. Search Contact.')
        print('3. Delete Contact.')
        print('4. List Contacts.')
        print('5. Exit.')

        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            name = input('Enter contact name: ')
            phone_number = input('Enter the phone number: ')
            email = input('Enter an optional email: ')
            add_contact(name, phone_number, email if email.strip() != '' else None)
        elif choice == '2':
            name = input('Enter a name to search: ')
            search_contact(name)
        elif choice == '3':
            name = input('Enter a contact to delete: ')
            delete_contact(name)
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print('See you again!')
            break
        else:
            print("Invalid choice, please choose a number between 1-5.")


if __name__ == '__main__':
    main_menu()