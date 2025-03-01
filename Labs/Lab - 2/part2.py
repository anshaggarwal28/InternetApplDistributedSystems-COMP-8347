'''
TEAM DETAILS:-
my_name of Student - Student Id
Manjinder Singh - 110097177
Harbhajan Singh - 110100089
Karan Vishavjit - 110099867
Khyati Shah     - 110090234
'''

# File my_name where details will be appended
address_text_file = "my_address_book.txt"

# Declaring and defining functionality to load address book data 
# from a text file into a dictionary.
def loading_address_details():
    try:
        with open(address_text_file, "r") as file:
            my_address_book = {}
            for line in file:
                my_name, my_email = line.strip().split(',')
                my_address_book[my_name] = my_email
        return my_address_book
    except FileNotFoundError:
        return {}

# Function to save address book data from dictionary to file
def saving_address(my_address_book):
    with open(address_text_file, "w") as file:
        for my_name, my_email in my_address_book.items():
            file.write(f"{my_name},{my_email}\n")

# Function to add a new information to the address book.
def add_contact(my_address_book):
    my_name = input("Enter the Name:- ")
    my_email = input("Enter the Email ID:- ")
    my_address_book[my_name] = my_email
    saving_address(my_address_book)
    print("Contact Information was added successfully.")

# Function to search for a information by Name.
def my_contact_search(my_address_book):
    my_name = input("Please enter name to search:- ")
    my_email = my_address_book.get(my_name)
    if my_email:
        print(f"Email ID for {my_name}: {my_email}")
    else:
        print(f"Information of '{my_name}' is not found.")

# Function to list all information from a file.
def enlisting_contacts(my_address_book):
    print("Name and Email ID Information:- ")
    for my_name, my_email in my_address_book.items():
        print(f"{my_name} - {my_email}")

# Main Function
def main():
    print("Part 2 of Lab 2:- ")
    my_address_book = loading_address_details()

    while True:
        print("\n Options Available:-\n1. Add a new contact\n2. Search for a contact\n3. List all contacts\n4. Quit")
        choice = input("Please enter your choice:- ")

        # conditions to enter all the choices
        if choice == "1":
            add_contact(my_address_book)
        elif choice == "2":
            my_contact_search(my_address_book)
        elif choice == "3":
            enlisting_contacts(my_address_book)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
