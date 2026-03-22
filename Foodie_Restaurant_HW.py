Welcome_text = ("Welcome to Foodie’s Point!")
print(Welcome_text)
while(True):
    print("Enter 1 to look at menu")
    print("Enter 2 to start your order")
    print("Enter 3 to exit program")
    choice = int(input("Enter your choice: "))   
    break
menu = {
     "Pizza" : "$1.50",
     "Chicken" :  "$2.00",
     "Burger" : "$3.00", 
     "Salad" : "$2.50", 
     "Bread" : "$1", 
     "Paninis" : "$5.00", 
     "Chili Paneer" : "$3.50" 
    }

if choice == 1:
    def func_tion(i):
        for (key, value) in menu.items():
            print(key," : ",value)
    func_tion(menu)



    