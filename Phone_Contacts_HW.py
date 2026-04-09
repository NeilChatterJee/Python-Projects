contact_list = {}

def add_contact(contact_list):
    for i in range(1000):  # Large enough to allow many additions
        name = input("Enter the contact as name(device): ")
        phone_number = input("Enter phone number: ")
        contact_list[name] = phone_number
        print("Contact added.")

        again = input("Add another contact? (yes/no): ").lower()
        if again != "yes":
            break

def search_contact(contact_list):
    for i in range(1000):
        search_name = input("Enter the name to search: ")
        if search_name in contact_list:
            print(f"{search_name}'s number is {contact_list[search_name]}")
        else:
            print("Contact not found.")

        again = input("Search another contact? (yes/no): ").lower()
        if again != "yes":
            break

def delete_contact(contact_list):
    for i in range(1000):
        delete_name = input("Enter the name to delete: ")
        if delete_name in contact_list:
            del contact_list[delete_name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

        again = input("Delete another contact? (yes/no): ").lower()
        if again != "yes":
            break

add_contact(contact_list)
search_contact(contact_list)
delete_contact(contact_list)
print(contact_list)