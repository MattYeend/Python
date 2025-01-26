from contact_manager.contact_manager import view_contacts, add_contact, search_contact, delete_contact
from contact_manager.data_manager import load_contacts, save_contacts

def main():
    contacts = load_contacts()

    print("Welcome to the Contact Management System!")
    while True:
        print("\nMenu:")
        print("1. View Contacts")
        print("2. Add a Contact")
        print("3. Search for a Contact")
        print("4. Delete a Contact")
        print("5. Save & Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
