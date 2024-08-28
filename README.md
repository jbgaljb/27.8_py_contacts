# Contact Management System

## Overview

This project is a simple contact management system implemented in Python. It allows users to perform various operations such as adding, deleting, viewing, loading, and saving contacts. Each contact has a unique ID, name, and phone number.

## Prerequisites

- Python 3.x installed on your system.
- A JSON file named `db.json` in the same directory as the script, which will be used to store and load contacts.

## Important Note

Before performing any operations, ensure that the contact list is loaded from the `db.json` file. This can be done by selecting the `LOAD` operation from the menu. If the file does not exist, the contact list will be initialized as empty.

## Usage

### Loading Contacts

You must load contacts from `db.json` before performing any other operations:

1. Run the script.
2. Choose the `LOAD` option from the menu to load contacts from the `db.json` file.

### Menu Operations

Once contacts are loaded, you can perform the following operations:

- **ADD**: Add a new contact to the list.
- **DELETE**: Delete a contact by ID.
- **VIEW_CONTACTS**: View all contacts in the list.
- **LOAD**: Reload contacts from `db.json`.
- **SAVE**: Save the current list of contacts to `db.json`.
- **EXIT_APP**: Exit the application.