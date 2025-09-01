import json

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts_data):
    print("\n")
    fname=input("Enter first name: ")
    lname=input("Enter last name: ")
    countrycode=input("Enter country code: ")
    phone=input("Enter phone number: ")
    email=input("Enter email: ")
    new_contact={"firstName": fname, "lastName": lname, "phoneNumber": phone, "countryCode": countrycode, "email": email}
    contacts_data["contacts"].append(new_contact)
    save_contacts('contacts.json', contacts_data)
    print("Contact added.")

def remove_contact(contacts_data):
    print("\n")
    phone=input("Enter phone number of the contact to remove: ")
    for contact in contacts_data["contacts"]:
        if contact["phoneNumber"]==phone:
            contacts_data["contacts"].remove(contact)
            save_contacts('contacts.json', contacts_data)
            print("Contact removed.")
            return
    print("Contact not found.")

def search_contact(contacts_data):
    print("\n")
    phone=input("Enter phone number to search: ")
    for contact in contacts_data["contacts"]:
        if contact["phoneNumber"]==phone:
            fname=contact["firstName"]
            lname=contact["lastName"]
            phoneNo=contact["phoneNumber"]
            countryCode=contact["countryCode"]
            email=contact["email"]
            print(f"Contact found:  ")
            print("\n")
            print(f"First Name: {fname}")
            print(f"Last Name: {lname}")
            print(f"Country Code: {countryCode}")
            print(f"Phone Number: {phoneNo}")
            print(f"Email: {email}")
            print("\n")
            return
    print("Contact not found.")

def display_contacts(contacts_data):
    if not contacts_data["contacts"]:
        print("No contacts available.")
        return
    for contact in contacts_data["contacts"]:
        print("\n")
        fname=contact["firstName"]
        lname=contact["lastName"]
        phoneNo=contact["phoneNumber"]
        countryCode=contact["countryCode"]
        email=contact["email"]
        print(f"First Name: {fname}")
        print(f"Last Name: {lname}")
        print(f"Country Code: {countryCode}")
        print(f"Phone Number: {phoneNo}")
        print(f"Email: {email}")
        print("\n")

def main():
    contacts_data=load_contacts('./contacts.json')
    if not contacts_data:
        contacts_data={"contacts": []}
    while True:
        print("\n")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice=input("Enter your choice: ")
        match choice:
            case '1':
                add_contact(contacts_data)
            case '2':
                remove_contact(contacts_data)
            case '3':
                search_contact(contacts_data)
            case '4':
                display_contacts(contacts_data)
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")

main()