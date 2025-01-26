import json

DATA_FILE = "contacts.json"

def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("\nNo contacts file found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("\nError decoding the contacts file. Starting with an empty list.")
        return []

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("\nContacts saved successfully!")
