#=============Import Libraries===========
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        """
        This is a constructor function that initializes attributes for a product object.
        
        :param country: a string representing the country where the product is sold
        :param code: a unique identifier for the product
        :param product: The name or description of the product being sold
        :param cost: The cost of the product in a specific currency
        :param quantity: The quantity parameter represents the number of units of a product that are
        being sold or purchased. It is an integer value
        """

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):

        """
        This function returns the cost attribute of an object.
        :return: The method `get_cost` is being defined for a class, and it returns the value of the
        `cost` attribute of an instance of that class.
        """
        
        return self.cost

    def get_quantity(self):

        '''
        Add the code to return the quantity of the shoes.
        '''

        return self.quantity
    
    def set_quantity(self, new_quantity):
        self.quantity += new_quantity

    def __str__(self):

        '''
        Add a code to returns a string representation of a class.
        '''

        return f"Product Country: {self.country}\n"\
               f"Product Code: {self.code}\n"\
               f"Product Name: {self.product}\n"\
               f"Product Cost: {self.cost}\n"\
               f"Product Quantity: {self.quantity}"
        

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:
        with open('inventory.txt', 'r') as f:
            next(f)
            for line in f:
                row = line.strip().split(',')
                my_shoe = Shoe(row[0], row[1], row[2], float(row[3]), int(row[4]))
                shoe_list.append(my_shoe)

    except IndexError:
        print("Error while reading data from file")

    except ValueError:
        print("Error while reading data from file")

    except FileNotFoundError:
        print("Error, File not found") 
    
def capture_shoes():

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    while True:
            try:
                while True:
                    try:
                        country = input("Enter country: ")
                        if not country.isalpha():
                            print("Only letters are allowed!")
                        else:
                            break
                    except ValueError:
                        print("Invalid Entry, please try again")
                        
                code = input("Enter code: ")
                product = input("Enter product: ")
                
                while True:
                    try:
                        cost = float(input("Enter cost: "))
                        break
                    except ValueError:
                            print(f"Invalid Entry, please try again")
                    
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        break
                    except ValueError:
                        print(f"Invalid Entry, please try again")
                
                shoe_list.append(Shoe(country, code, product, cost, quantity))
                print("\nNew shoe added successfully!")

                while True:
                    where_to_return = input(f"""\nSelect one of the following options:
    1 - Add another shoe
    2 - Return to main menu
    >:: """)
                    if where_to_return == "1":
                        capture_shoes()
                    elif where_to_return == "2":
                        return menu_
                    else:
                        print("Invalid Entry")
            except ValueError:
                print("Invalid Entry")


def view_all():

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''

    table = []
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"]))

def re_stock():

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    if len(shoe_list) >= 1:

        lowest_shoe = shoe_list[0]

        for shoe in shoe_list:
            if shoe.quantity <= lowest_shoe.quantity:
                lowest_shoe = shoe
        
        print("\nThe following is the lowest shoe:\n")
        print(lowest_shoe)

        will_restock = input("\nDo you want to add to the existing quantity? (Yes or No): ").lower()

        if will_restock == "yes":
            try:

                new_quantity = int(input(f"Enter the quantity that you want to add"\
                                         f"\n(e.g. Product Quantity is now = Current Quantity + Quantity entered): "))
                lowest_shoe.set_quantity(new_quantity)
                print(f"\nShoe has been restocked, new details are below\n{lowest_shoe}")

            except ValueError:
                print("You have entered an invalid input, going back to main menu")

        elif will_restock == "no":
            print("Going to main menu")
        else:
            print("Unknown value entered, returning to main menu")
    else:
        print("There are no shoes found")
    

def search_shoe():

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    while True:
        code_to_search = input("\nEnter code to search: ").upper()
        for s in shoe_list:
            if s.code.upper() == code_to_search:
                return s
        print(f'No shoe found with code {code_to_search}')
   
def value_per_item():

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    value = []
    for shoe in shoe_list:
        value.append([shoe.product, shoe.code, float(round(shoe.cost * shoe.quantity, 2))])
    print(tabulate(value, headers=["Product", "Code", "Total Value"]))


def highest_qty():

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    shoe_index = 0
    for i, s in enumerate(shoe_list):
        if s.quantity > shoe_list[shoe_index].quantity:
            shoe_index = i
    print("\nThe following shoe has the highest quantity and it's on sale:\n")
    print(shoe_list[shoe_index])

def write_to_file():

    '''
    This function writes a list of shoe objects to a file named 'inventory.txt' in a specific format.
    '''

    with open('inventory.txt', 'w') as write_file:
        write_file.write(f"Country,Code,Product,Cost,Quantity")
        for shoe in shoe_list:
            line = f"\n{shoe.country},{shoe.code},{shoe.product},{int(shoe.cost)},{int(shoe.quantity)}"
            write_file.write(line)

#==========Main Menu=============

'''
Creates a menu that executes each function above.
This menu is called inside the while loop.

'''
print("Welcome to the Nike Product Portal")
menu_ = '''\nSelect one of the following Options below:
    cs - Capture Shoe
    va - View All Shoes
    rs - Restock a Shoe
    ss - Search for a Shoe (By Stock Code)
    vp - Total Value Per Item
    hq - Shoe With Highest Quantity 
    e - Exit
    : '''


read_shoes_data()

while True:

    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input(menu_).lower()
    
    # `if menu == 'cs': capture_shoes()` is a conditional statement that checks if the user input is
    # 'cs' (for capture shoes) and if it is, it calls the `capture_shoes()` function which allows the
    # user to capture data about a shoe and use this data to create a shoe object and append this
    # object inside the shoe list.
    if menu == 'cs':
        capture_shoes()

    # `elif menu == 'va': view_all()` is a conditional statement that checks if the user input is 'va'
    # (for view all) and if it is, it calls the `view_all()` function which iterates over the
    # `shoe_list` and prints the details of the shoes returned from the `__str__` function. It uses
    # the `tabulate` module to organize the data in a table format.
    elif menu == 'va':
        view_all()

    # `elif menu == 'rs': re_stock()` is a conditional statement that checks if the user input is 'rs'
    # (for restock) and if it is, it calls the `re_stock()` function which finds the shoe object with
    # the lowest quantity, which is the shoes that need to be restocked. It then asks the user if they
    # want to add this quantity of shoes and then updates it. This quantity is updated on the file for
    # this shoe.
    elif menu == 'rs':
        re_stock()

    # `elif menu == 'ss': print(search_shoe())` is a conditional statement that checks if the user
    # input is 'ss' (for search shoe) and if it is, it calls the `search_shoe()` function which
    # searches for a shoe from the list using the shoe code and returns this object so that it will be
    # printed.
    elif menu == 'ss':
        print(search_shoe())

    # `elif menu == 'vp': value_per_item()` is a conditional statement that checks if the user input
    # is 'vp' (for value per item) and if it is, it calls the `value_per_item()` function which
    # calculates the total value for each item by multiplying the cost and quantity attributes of each
    # shoe object in the `shoe_list`. It then prints this information on the console for all the shoes
    # in a table format.
    elif menu == 'vp':
        value_per_item()

    # `elif menu == 'hq': highest_qty()` is a conditional statement that checks if the user input is
    # 'hq' (for highest quantity) and if it is, it calls the `highest_qty()` function which determines
    # the product with the highest quantity and prints this shoe as being for sale.
    elif menu == 'hq':
        highest_qty()

    elif menu == 'e':

        # This code block is checking if the user input is 'e' (for exit) and if it is, it prints the
        # message "Goodbye!!!" and exits the program using the `exit()` function.
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

    write_to_file()
    