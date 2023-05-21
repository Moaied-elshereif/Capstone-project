import csv
from datetime import date

# Function to create a new contact
def create_contact():
    # Get contact details from the user
    username = input("Enter username: ")
    email = input("Enter email: ")
    phone_numbers = input("Enter phone numbers ").split(",")
    address = input("Enter address: ")
    insertion_date = date.today()

    # Create a list of contact details
    contact = [username, email, phone_numbers, address, insertion_date]

    # Open the CSV file in append mode and write the contact details
    with open(get_file_name(), 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)

    print("Contact created successfully!")

# Function to update an existing contact
def update_contact():
    # Get the contact ID and field to update from the user
    contact_id = input("Enter the contact ID to update: ")
    field = int(input("Enter the field to update (1-5):\n"
                      "1. Username\n"
                      "2. Email\n"
                      "3. Phone numbers\n"
                      "4. Address\n"
                      "5. Insertion date\n"))

    # Open the CSV file in read mode and read all contacts
    with open(get_file_name(), 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    # Check if the contact ID is valid
    if int(contact_id) in range(1, len(contacts)):
        contact = contacts[int(contact_id) - 1]

        # Update the selected field based on user input
        if field == 1:
            contact[0] = input("Enter new username: ")
        elif field == 2:
            contact[1] = input("Enter new email: ")
        elif field == 3:
            contact[2] = input("Enter new phone numbers: ").split(",")
        elif field == 4:
            contact[3] = input("Enter new address: ")
        elif field == 5:
            contact[4] = date.today()

        # Open the CSV file in write mode and write all contacts
        with open(get_file_name(), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact updated successfully!")
    else:
        print("Invalid contact ID.")

# Function to delete a contact
def delete_contact():
    # Get the contact ID to delete from the user
    contact_id = input("Enter the contact ID to delete: ")

    # Open the CSV file in read mode and read all contacts
    with open(get_file_name(), 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    # Check if the contact ID is valid
    if int(contact_id) in range(1, len(contacts)):
        # Remove the contact from the list
        contacts.pop(int(contact_id) - 1)

        # Open the CSV file in write mode and write the updated contacts
        with open(get_file_name(), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact deleted successfully!")
    else:
        print("Invalid contact ID.")

# Function to list all contacts
def list_contacts():
    # Open the CSV file in read mode and read all contacts
    with open(get_file_name(), 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    # Print the details of each contact
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact ID: {i}")
        print("Username:", contact[0])
        print("Email:", contact[1])
        print("Phone numbers:", ", ".join(contact[2]))
        print("Address:", contact[3])
        print("Insertion date:", contact[4])

# Function to generate the file name based on the current date
def get_file_name():
    today = date.today().strftime("%d%m%Y")
    return f"contactbook_{today}.csv"

# Main program loop
while True:
    print("\n--- Contact Book ---")
    print("1. Create contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. List contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")


