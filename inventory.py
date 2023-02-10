# create a new class named 'Shoe'
class Shoe:
    # initialise constructor for Shoe with five variables 'country', 'code', 'product', 'cost', and 'quantity'
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # define method 'get_cost' that returns the cost value of a particular Shoe object
    def get_cost(self):
        return self.cost

    # define method 'get_quantity' that returns the quantity value of a particular Shoe object
    def get_quantity(self):
        return self.quantity

    # in Shoe class define method that returns the below string as the string representation of each Shoe object
    def __str__(self):
        output = f"Product:    {self.product}\n"
        output += f"Cost:       {self.cost}\n"
        output += f"Quantity:   {self.quantity}\n"
        output += f"Country:    {self.country}\n"
        output += f"Code:       {self.code}\n"
        return output

# The list 'shoe_list' will be used to store a list of objects of shoes.
shoe_list = []
#==========Functions outside the class==============
'''
    Define new function 'read_shoes_data' that opens the file inventory.txt and reads the data from this file, then creates a Shoe object with this data
    and appends this object into shoe_list. 
'''
def read_shoes_data():
    file = open("inventory.txt", "r")
    shoes = file.readlines()
    temp_shoe_list = []
    for shoe in shoes:
        temp_shoe_list.append(shoe)
    temp_shoe_list.pop(0)
    for shoe in temp_shoe_list:
        temp = shoe.strip()
        temp = temp.split(",")
        try:
            shoe_list.append(Shoe(temp[0],temp[1],temp[2],int(temp[3]),int(temp[4])))
        except:
            print(temp)
            print("The above line could not be turned into a Shoe object because either the cost or quantity value was not valid")
    file.close()

'''
    Define new function 'capture_shoes' requests the user input the relevant information to create a new Shoe object and creates a new Shoe object
    with this date and appends this object to shoe_list. It then appends a new line into inventory.txt with the inforomation
    of the new Shoe object.
'''
def capture_shoes():
    product = input("Enter name of shoe:       ")
    code = input("Enter code of shoe:       ")
    country = input("Enter country of shoe: ")
    while True:
        cost = input("Enter cost of shoe:   ")
        try:
            cost = float(cost)
            break
        except:
            print("Please enter a valid cost.\n")
    while True:
        quantity = input("Enter quantity of shoe:   ")
        try:
            quantity = int(quantity)
            break
        except:
            print("Please enter a valid quantity.\n")
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    file = open ("inventory.txt", "a")
    file.write("\n" + country + "," + code + "," + product + "," + str(cost) + "," + str(quantity))
    file.close()
   
'''
    Define new function 'view_all' that runs through each object in shoe_list and prints the string value from the __str__ function
    for each object. 
'''
def view_all():
    print()
    counter = -1
    for shoe in shoe_list:
        print(f"{shoe}\n")
        counter += 1
    if counter == -1:
        print("There currently are no shoes in the inventory list.")
   
'''
    Define new function 're_stock' that checks the quantity of each Shoe object in shoe_list. It then returns the shoe with the 
    lowest quantity value and asks if user would like to add more stock or not. If the user would like to add more stock, they enter
    how much they would like to add and then the quantity in that Shoe object is updated to include the new addition of stock. 
    The quantity figure for this Shoe object is also then updated in the file inventory.txt. 
'''
def re_stock():
    print()
    if len(shoe_list) > 0:
        low_count = shoe_list[0].quantity
        list_place = -1
        for shoe in shoe_list:
            list_place += 1
            if shoe.quantity < low_count:
                low_count = shoe.quantity
                low_shoe = list_place
                low_shoe_code = shoe.code
        while True:
            add_shoes = input(f"You are low on the following shoe:\n\n{shoe_list[low_shoe]}\n\nWould you like to add to this quantity of shoes, y or n? ")
            print()
            if add_shoes == "y":
                while True:
                    shoes_to_add = input("How many shoes would you like to add: ")
                    try:
                        shoes_to_add = int(shoes_to_add)
                        break
                    except:
                        print()
                        print("Please enter a valid quantity of shoes to add.\n")
                shoe_list[low_shoe].quantity = shoe_list[low_shoe].quantity + shoes_to_add
                file = open("inventory.txt", "r")
                shoes = file.readlines()
                file.close()
                counter = -1
                for shoe in shoes:
                    counter += 1
                    temp = shoe.strip()
                    temp = temp.split(",")
                    if temp[1] == low_shoe_code:
                        temp[4] = int(temp[4]) + shoes_to_add
                        temp[4] = str(temp[4])
                    shoes[counter] = temp
                file = open("inventory.txt", "w")
                counter1 = -1
                for shoe in shoes:
                    counter1 += 1
                    if counter1 < len(shoes) -1:
                        file.writelines(shoe[0] + "," + shoe[1] + "," + shoe[2] + "," + shoe[3] + "," + shoe[4] + "\n")
                    elif counter1 == len(shoes) - 1:
                        file.writelines(shoe[0] + "," + shoe[1] + "," + shoe[2] + "," + shoe[3] + "," + shoe[4])
                file.close()
                print()
                print(shoe_list[low_shoe])
                break
            elif add_shoes == "n":
                print("You have choosen to not add any more shoes.")
                break
            else:
                print("Please provide a valid entry.\n")
        
    else:
        print("There are currently no shoes in inventory list.")

'''
    Define new function 'search_shoe'. In this function, the user is asked to input the code of the Shoe object they would like to see
    the details of. If that code is found in shoe_list, the __str__ value of that object is then returned. If that code is not found
    tell user that the code is not in the inventory. The search will be case sensitive.  
'''
def search_shoe():
    print()
    if len(shoe_list) > 0:
        req_shoe = input("Enter code of desired shoe: ")
        print()
        instance = 0
        for shoe in shoe_list:
            if shoe.code == req_shoe:
                print(shoe)
                instance += 1
        if instance == 0:
            print("That code does not exist in inventory")
    else:
        print("There are currently no shoes in inventory list.")

'''
    Define new function 'value_per_item'. Run through each object in shoe_list and for each object, multiply the result of the
    get_cost method with the result of the get_quantity method. That total is then printed out with the product value of that object.
'''
def value_per_item():
    print()
    if len(shoe_list) > 0:
        for shoe in shoe_list:
            value = shoe.get_cost() * shoe.get_quantity()
            print(f"The current value of {shoe.product} is R{value}.")
    else:
        print("There are currently no items in inventory list.")

'''
    Define new function 'highest_qty' that checks each object in shoe_list and prints the __str__ value for the object that has
    the highest quantity value. 
'''
def highest_qty():
    print()
    most_shoe = 0
    shoe_index = -1
    for shoe in shoe_list:
        shoe_index += 1
        if shoe.quantity > most_shoe:
            most_shoe = shoe.quantity
            high_index = shoe_index
    if shoe_index == -1:
        print("There are no shoes currently in the inventory list.")
    elif shoe_index > -1:
        print(f"{shoe_list[high_index].product} has the highest quantity with {shoe_list[high_index].quantity} and is now on sale.")

#==========Main Menu=============
'''
    Print below menu in an infinite while loop. Save user choice as variable 'choice' and then convert that value to all lowercase.
    This will make it so user's entry is not case sensitive.  
'''
while True:
    print("Select frome the menu below - \n")
    print("import -      import information from inventory file")
    print("create -      create information for a new shoe")
    print("view -        view all shoes")
    print("search -      search for a shoe by code")
    print("stock -       search for shoe with lowest quantity")
    print("value -       print value of each shoe")
    print("most -        search for shoe with highest quantity")
    print("exit -        exit the program\n")
    choice = input("")
    choice = choice.lower()

    # if choice is equal to import, run function read_shoes_data
    if choice == "import":
        read_shoes_data()
        print()

    # else if choice is equal to create, run function capture_shoes
    elif choice == "create":
        capture_shoes()
        print()
    
    # else if choice is equal to view, run function view_all
    elif choice == "view":
        view_all()
        print()
    
    # else if choice is equal to search, run function search_shoe
    elif choice == "search":
        search_shoe()
        print()

    # else if choice is equal to stock, run function re_stock
    elif choice == "stock":
        re_stock()
        print()
    
    # else if choice is equal to value, run function value_per_item
    elif choice == "value":
        value_per_item()
        print()

    # else if choice is equal to most, run function highest_qty
    elif choice == "most":
        highest_qty()
        print()
    
    # else if choice is equal to exit, break while loop and end program
    elif choice == "exit":
        print("Goodbye!")
        break

    # else, print that the user has not made a valid choice
    else:
        print()
        print("You have not made a valid choice. Try again.")
        print()