name_input = input("Enter Your Full Name/Names! Separate By Comma: ")
def initials():
    name_list = name_input.split(",")
    print(name_list)
    for name in name_list:
        name = name.strip()
        name = name.split()
        first_name = name[0]
        last_name = name[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        print(f"{first_initial}.{last_initial}.")
initials()