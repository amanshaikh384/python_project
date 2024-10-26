# Contact Book
def contact_book():
    print("Welcome to your Contact Book!")
    contacts = {}
    
    while True:
        print("\n1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            name = input("Enter the name of the contact: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            
            contacts[name] = {"Phone": phone, "Email": email}
            print(f"Contact '{name}' added successfully.")
        
        elif choice == "2":
            if not contacts:
                print("Your Contact Book is empty.")
            else:
                print("\nYour Contacts:")
                for name, details in contacts.items():
                    print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
        
        elif choice == "3":
            search_name = input("Enter the name of the contact you want to search for: ")
            if search_name in contacts:
                print(f"Name: {search_name}, Phone: {contacts[search_name]['Phone']}, Email: {contacts[search_name]['Email']}")
            else:
                print("Contact not found.")
        
        elif choice == "4":
            delete_name = input("Enter the name of the contact you want to delete: ")
            if delete_name in contacts:
                del contacts[delete_name]
                print(f"Contact '{delete_name}' deleted successfully.")
            else:
                print("Contact not found.")
        
        elif choice == "5":
            print("Thank you for using your Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    contact_book()
