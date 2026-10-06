import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#========The beginning of the class==========
class Shoe:
    '''
    Initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
    '''

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # This code returns the cost of the shoe in this method.
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        '''
        This code returns the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        
        '''
        This code returns a string representation of a class.
        '''
        return (f"Country: {self.country}, Code: {self.code}, "
            f"Product: {self.product}, Cost: {self.cost}, "
            f"Quantity: {self.quantity}")

#=============Shoe list===========
#The list will be used to store a list of objects of shoes.

shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function opens the file inventory.txt
    and reads the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(",")
                shoe = Shoe(
                    data[0],
                    data[1],
                    data[2],
                    float(data[3]),
                    int(data[4]),
                )
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("The inventory file could not be found.")
    except (ValueError, StopIteration):
        print("The inventory file contains invalid data.")

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    #defensive programming: check if shoe_list is empty
    if not shoe_list:
        print("No shoes available to restock.")
        return

    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    #Tell user what shoe has the lowest stock and ask if they want to restock it
    print(f"Lowest stock item: {lowest_shoe.product}")
    print(f"Current quantity: {lowest_shoe.quantity}")

    restock_choice = input("Do you want to restock this item? (yes/no): ")
    if restock_choice.lower() == "yes":
        try:
            restock_quantity = int(input("Enter the quantity to restock: "))

            lowest_shoe.quantity += restock_quantity

            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    file.write(
                        f"{shoe.country},{shoe.code},{shoe.product},"
                        f"{shoe.cost},{shoe.quantity}\n"
                    )
            print(f"Restocked {restock_quantity} units of {lowest_shoe.product}.")
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"Code: {shoe.code}")
            print(f"Product: {shoe.product}")
            return shoe

    print(f"Shoe with code {code} not found.")
    return None

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()

        print(
            f"Product: {shoe.product} | "
            f"Code: {shoe.code} | "
            f"Value: {value:.2f}"
        )

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

    print(
        f"{highest_shoe.product} is for sale. "
        f"Quantity available: {highest_shoe.quantity}"
    )

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Load the shoe data before displaying the menu.
read_shoes_data()

while True:
    print("\n===== NIKE WAREHOUSE INVENTORY =====")
    print("1. View all shoes")
    print("2. Capture a new shoe")
    print("3. Restock lowest quantity shoe")
    print("4. Search for a shoe")
    print("5. View value per item")
    print("6. View highest quantity shoe")
    print("7. Exit")

    choice = input("Please select an option: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        result = search_shoe()
        if result:
            print(result)

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Exiting Nike Warehouse Inventory.")
        break

    else:
        print("Invalid option. Please select a number from 1 to 7.")
        