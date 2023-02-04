
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost


    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.code


    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return self.product


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
    with open("inventory.txt","r")as f:

        for line_index,line in enumerate(f):
            
            try:
                line = line.split(",")
                country = line[0]
                code = line[1]
                product =line[2]
                cost = float(line[3])
                quantity =int(line[4])
                shoe = Shoe(country,code,product,cost,quantity,)
                shoe_list.append(shoe)

            # Value error exception to track down if anything gone wrong in specific line    
            except ValueError:
                print(f"Skipped line {line_index+1}")
                continue


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
   '''
    country = input("Enter country: ")
    code = input("Enter product code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter product price: "))
    quantity =int(input("Enter quantity: "))
    shoe = Shoe(country,code,product,cost,quantity,)
    shoe_list.append(shoe)

# Additional function to print details of single item
def view_item(shoe):

    print("="*50)
    print(f"Product code: {shoe.code}\t Name: {shoe.product}")
    print(f"Counttry:{shoe.country}\t Quantity:{shoe.quantity}")
    print(f"Price:{shoe.cost}")
    print("="*50)


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        # object will be printed from class __str__ method 
        print(shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # listto store objects withlow quantity
    low_stock = []

    for shoe in shoe_list:
        # if quantity is less than 5 
        if shoe.quantity < 5 :
            low_stock.append(shoe)

    # if no items less than 5
    if len(low_stock) == 0:
        print("All items quantity above 5")
    
    else:
        # Printing items with low amount
        print("This items are low stock:")
        for shoe in low_stock:
            view_item(shoe)
        
        stock_update = input("Would you like to update amount of shoes in stock(Enter 'y' -yes or 'n'- No): ")

        if stock_update == 'y':
            # if user wants to update 
            for shoe in low_stock:
                # he will enter amount for each item 
                new_quantity = int(input(f"Enter amount to add for {shoe}: "))
                index = shoe_list.index(shoe)
                # new amount will be added ontop of items amount i.e old_amoun+ new_amount
                shoe_list[index].quantity += new_quantity
            update_file()

        else:
            return 0


def seach_shoe(shoe_code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            return shoe

    return "Item doesn't exist"

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f"{shoe}\t\tTotal value:{total_value}")   

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # temp_shoe will store item with higest amount while traversing 
    temp_shoe = None
    highest_quantity = 0

    for shoe in shoe_list:
        
        if shoe.quantity > highest_quantity:
            highest_quantity = shoe.quantity
            temp_shoe = shoe

    print(f"{temp_shoe} is recomended for sale")
    return temp_shoe

# Additional funtionto update file content
def update_file():

    with open("inventory.txt",'w') as f:

        f.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoe_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()
user_choice = ""
while user_choice!= "e":

    
    print("'s' - to search product by code")
    print("'a' - to add product to inventory")
    print("'va' - to view all products in inventory")
    print("'vl' - to see low stock items")
    print("'vh' -to see highest stock item")
    print("'vs'- to view total stock cost per item")
    print("'e' - to exit")

    user_choice = input("Enter from options above: ").lower()
    
    if user_choice == 's':

        code = input("Enter product code: ")

        result = seach_shoe(code)

        view_item(result)
    
    elif user_choice == 'a':

        capture_shoes()
        update_file()
        
    elif user_choice == 'va':

        view_all()

    elif user_choice == 'vl':

        re_stock()

    elif user_choice == 'vh':

        high_stock = highest_qty()

        view_item(high_stock)
    
    elif user_choice == 'vs':

        value_per_item()
    
    elif user_choice == 'e':

        break

    else:
        print("Wrong entry, please choose from options provided")