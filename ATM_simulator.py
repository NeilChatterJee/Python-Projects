User_Information = {
    "Neil" : {"password" : "ILoveEating2025!", "balance" : 1000},
    "Aum"  : {"password" : "Cheesicorn", "balance" : 850},
    "Sid"  : {"password" : "IPlayValorant", "balance": 900}
}

print("  Welcome to the ATM  ")
user_name = input("Please input your exact user_name: ")

if user_name in User_Information:
    password = (input("Please input your exact password: "))
    if password == User_Information[user_name]["password"]:
        print(f"You have successfully logged in to {user_name}'s account")
    else:
        print("Incorrect Password")    
    
else: 
    print("That user is not in our ATM's data logs")

def withdraw_money(user):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= User_Information[user]["balance"]:
            User_Information[user]["balance"] -= amount
            print(f"Withdrawal successful. New balance: ${User_Information[user]['balance']}")
        else:
            print("Insufficient funds.")

def deposit_money(user):
        amount = float(input("Enter amount to deposit: "))
        User_Information[user]["balance"] += amount
        print(f"Deposit successful. New balance: ${User_Information[user]['balance']}")

if password == User_Information[user_name]["password"]:
        while True:
            print("Choose an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print(f"Your current balance is: ${User_Information[user_name]['balance']}")
            elif choice == "2":
                deposit_money(user_name)
            elif choice == "3":
                withdraw_money(user_name)
            elif choice == "4":
                print("ATM Transactions Complete")
                break
            else:
                print("Invalid choice. Please try again.")


    

