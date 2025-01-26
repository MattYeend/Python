def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts available.")
    else:
        print("\nYour Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} ({contact['email']})")

def add_contact(contacts):
    """Add a new contact."""
    name = input("\nEnter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email})
        print(f"\nContact '{name}' added successfully!")
    else:
        print("\nName and phone number are required.")

def search_contact(contacts):
    """Search for a contact by name."""
    search_term = input("\nEnter the name to search for: ").strip().lower()
    results = [c for c in contacts if search_term in c["name"].lower()]

    if results:
        print("\nSearch Results:")
        for idx, contact in enumerate(results, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} ({contact['email']})")
    else:
        print("\nNo contacts found matching that name.")

def delete_contact(contacts):
    """Delete a contact by name."""
    view_contacts(contacts)
    name_to_delete = input("\nEnter the name of the contact to delete: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name_to_delete.lower():
            contacts.remove(contact)
            print(f"\nContact '{name_to_delete}' deleted successfully!")
            return

    print(f"\nContact '{name_to_delete}' not found.")
