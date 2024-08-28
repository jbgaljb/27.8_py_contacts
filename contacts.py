from enum import Enum
import uuid
import json

def save_contacts_to_file(file_path='db.json'):
    try:
        with open(file_path, 'w') as file:
            json.dump(contacts, file, indent=4)
            print(f"Contacts saved to {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving to {file_path}: {e}")

def load_contacts_from_file(file_path='db.json'):
    try:
        global contacts
        print("i am trying")
        with open(file_path, 'r') as file:
            contacts = json.load(file)
            print(f"Loaded {len(contacts)} contacts from {file_path}.")
            return contacts
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

class operations(Enum):
    ADD = 1
    DELETE = 2
    VIEW_CONTACTS = 3
    LOAD = 4
    SAVE = 5
    EXIT_APP = 6

def save():
    save_contacts_to_file()

def load():
    load_contacts_from_file()

def exit_app():
    exit()

def add():
    name = input("What is the name of the contact? ")
    phone_number = input("What is the phone number of the contact? ")
    
    # Generate a unique ID using uuid
    new_id = str(uuid.uuid4())
    
    # Append the new contact to the contacts list
    contacts.append({
        'id': new_id,
        'name': name,
        'phone_number': phone_number
    })
    
    print(f"Contact {name} added successfully with ID {new_id}!")

def delete():
    id_to_del = int(input("What is the ID of the contact you wish to delete? "))
    
    # Find the contact with the given ID
    for contact in contacts:
        if contact['id'] == id_to_del:
            contacts.remove(contact)
            print(f"Contact with ID {id_to_del} has been deleted.")
            break
    else:
        print(f"No contact found with ID {id_to_del}.")

def search():
    print("search")

def view_contacts():
    for contact in contacts:
        print(f"{contact['name']} - {contact['phone_number']}  | id: {contact['id']}")

def menu():
    for operation in operations:
        print(operation.name + " - " + str(operation.value))
    # through input number getting to Enum name, which in turn is used to
    # call the chosen function from globals
    globals()[(operations(int(input("choose a number "))).name).lower()]()

def main():
    while True:
        menu()

if __name__ == '__main__':
    main()