#a private data class storing the total sales and total income
class _data:
    #initialize the data class
    def __init__(self, totalSales, totalIncome) :
        self.totalSales = totalSales
        self.totalIncome = totalIncome

    #prints the total sales and income of the business throughtout the waiters
    def get_totals(self):
        print(print(f"Today there has been a total of {sales.totalSales} with the gross income of {sales.totalIncome}"))

#importing the classes
from errorhandling import *
from stock import * 
from waiters import *
from tables import *


#global variables
stocktxt = "Stock.txt"
waiterstxt = "Login.txt"
staffDict = {}
stockDict = {}
tablesDict = {}
totalSales = {}
sales = _data(0,0)

#creates the stock object 
def create_stock_object():
    count = 0
    #finding the length of the text file
    with open(stocktxt, "r") as file:
        for line in file:
            count += 1

    #creates instances of the class with default values
    for i in range(1, count+1):
        stockDict[i] = stock()

    #reads through the file and strips the values and adds it to the object
    with open(stocktxt, "r") as file:
        count = 0
        for line in file:
            count += 1
            values = line.strip().split(",")
            stockName, price = values
            stockDict[count].item = stockName
            stockDict[count].price = float(price)

#creates the staff object
def create_staff_object():
    #finding the length of the textfile
    count = 0
    with open(waiterstxt, "r") as file:
        for line in file:
            count += 1

    #creates instances of the class with default values
    for i in range(1, count+1):
        staffDict[i] = waiters()


    #reads through the file and strips the values and adds it to the object
    with open(waiterstxt, "r") as file:
        count = 0
        for line in file:
            count += 1
            values = line.strip().split(",")
            username, password = values
            staffDict[count].username = username
            staffDict[count].password = password
            staffDict[count].sales = 0

# creates the table object
def create_table_objects():
    #creates 6 table instances with a uniquw table num but the rest default values
    for i in range(0, 6):
        tablesDict[i] = tables('Table' + str(i+1), '', '', {}, False)

#allows a user to print a menu
def print_menu(heading, options):
    print(heading + "\n")

    #prints each option of a menu in the format of 1: Assign Tables
    for x in range(len(options)):
        print(f"{x+1}: {options[x]}")

#allows a user to login to the the system
def login():
    while True:
        #creating global variables
        global current_waiter
        global waiter_ID
        create_staff_object()
        print_menu("Welcome to HighLands Cafe", ["Login", "Total Sales" ,"Exit"])
        userSelection = errorhandling.intInput(1, 3, "Selection: ")
        if userSelection == 1:
            username = input("Enter your username: ")
            password = (input("Enter your password: "))
            for keys in staffDict:
                if staffDict[keys].username == username and staffDict[keys].password == password: #checks if the password and username are correct
                    current_waiter = staffDict[keys].username #sets the current waiter to the waiter who logged in
                    waiter_ID = keys #waiter ID is the key of the the current waiter in the staffDict
                    return True
            print("Incorrect password or username")
        elif userSelection == 2:
            sales.get_totals() #prints the total sales values
        elif userSelection == 3:
            break

#allows a user to select a table to assign
def table_selection():
    #sets the list
    Tables = []
    while True:
        for key in tablesDict:
            if tablesDict[key].waiter == '': #checks if the table is not being used
                print(f"{key+1}: {tablesDict[key].tableNum}")
                Tables.append(key+1)
        userChoice = errorhandling.intInput(0, 6, "Select a table:")
        if userChoice in Tables: #checks that the table is available
            return userChoice
        elif userChoice == 0:
            return 0
        else:
            print(f"Select a valid option: ")

#allows a user to assign a table to the users ID
def assign_tables():
    print("Select a table: ")
    selection = table_selection()
    if selection == 0:
        return #exits the current menu
    else:
        tablesDict[selection-1].waiter = current_waiter
        userSelection = errorhandling.yesNoInput(
            "Would you like to add customers to the table (y/n): ")
        if userSelection:
            amountCustomers = errorhandling.intInput(1, 10, "How many customers are seated at the table?: ")
            tablesDict[selection-1].customers = amountCustomers
            print(selection)
            print(tablesDict[selection-1].customers)
        else:
            return

#allows a user to select the table assigned to he/her ID
def select_current_tables():
    while True:
        currentTables = []
        for key, value in enumerate(tablesDict):
            if tablesDict[key].waiter == current_waiter:
                print(f"{key+1}. {tablesDict[value].tableNum}")
                currentTables.append(key+1)
        selection = errorhandling.intInput(
            0, 6, "Select a table or 0 to exit: ")
        if (selection - 1) == -1:
            return
        elif selection not in currentTables:
            print(f"Invalid selection select {currentTables}")
        else:
            return selection

#allows the user to change the amount of customers at the table
def change_customer():
    selection = select_current_tables()
    if selection == None:
        return
    amountCustomers = errorhandling.intInput(
        1, 10, "How many people are seated at the table: ")
    tablesDict[selection-1].customers = amountCustomers

#allows a user to add items to a table
def add_to_order():
    selection = select_current_tables()
    if selection == None:
        return #exits menu
    for key in stockDict: #prints the items
        print(f"{key}: {stockDict[key].item} R{stockDict[key].price} ")
    userChoice = errorhandling.intInput(
        1, 13, "Choose an item you will like to add: ")
    quantity = errorhandling.intInput(1, 100, "Quantity: ")
    itemKey = (len(tablesDict[selection-1].orders) + 1)
    tablesDict[selection-1].orders[itemKey] = (userChoice, quantity)
    addItem = errorhandling.yesNoInput(
        "Would you like to add another item y/n: ")
    if addItem:
        add_to_order()
    else:
        return

#allows a user to prepare a bill
def prepare_bill():
    total = 0
    selection = select_current_tables()
    if selection == None:
        return
    #prints the bill in the terminal
    print("----------------------------------------------------------")
    print(f"The bill for {tablesDict[selection-1].tableNum}\n")
    print(f"{'':>17}{'Item':<17}{'Quantity':<17}Price\n")
    for key in (tablesDict[selection-1].orders):
        itemID, quantity = tablesDict[selection-1].orders[key]
        item = stockDict[itemID].item
        quantity = tablesDict[selection-1].orders[key][1]
        price = stockDict[itemID].price
        total = total + (price*quantity)
        print(f"{'':>17}{item:<17}{quantity:<17}R{price}")
    print(f"\nThe total of your order was R{total}\n")
    print(f"You were helped by {current_waiter} ")
    print("----------------------------------------------------------")
    tablesDict[selection-1].billPrepared = True #changes the billprepared attribute to true
    staffDict[waiter_ID].sales = staffDict[waiter_ID].sales + total #increases the waiters total

#allows a user to create a textfile for the bill
def complete_sale():
    total = 0
    selection = select_current_tables()
    if selection == None:
        return
    if tablesDict[selection-1].billPrepared == True:
        fileName = input("Please enter file name: ")
        with open(fileName, "w") as file:
            file.write(f"The bill for {tablesDict[selection-1].tableNum}\n")
            file.write(f"{'':>17}{'Item':<17}{'Quantity':<17}Price\n")
            for key in (tablesDict[selection-1].orders):
                itemID, quantity = tablesDict[selection-1].orders[key]
                item = stockDict[itemID].item
                quantity = tablesDict[selection-1].orders[key][1]
                price = stockDict[itemID].price
                total = total + (price * quantity)
                file.write(f"{'':>17}{item:<17}{quantity:<17}R{price}")
            file.write(f"\nThe total of your order was R{total}\n")
            file.write(f"You were helped by {current_waiter} ")
            file.write("added to file")
        sales.totalSales = sales.totalSales + 1
        sales.totalIncome = sales.totalIncome + total

        #resets the values
        tablesDict[selection-1].waiter = ''
        tablesDict[selection-1].customers = 0
        tablesDict[selection-1].orders = {}
        tablesDict[selection-1].billPrepared = False

    else:
        print("Please prepare bill first.")
        return
    
#prints the cashup for the waiter
def cash_up():
    print(f"Your total cash up is: {staffDict[waiter_ID].sales}")

#allows navigation between the different menus
def main_menu():
    create_stock_object()
    create_table_objects()

    if login():
        while True:
            options = ["Assign Tables", "Change customers", "Add to order",
                       "Prepare Bill", "Complete Sale", "Cash up", "Logout"]
            print_menu(
                f"Welcome {current_waiter}\nWhat would you like to do today?", options)
            choice = errorhandling.intInput(1, 7, "Selection: ")
            match choice:
                case 1:
                    assign_tables()
                case 2:
                    change_customer()
                case 3:
                    add_to_order()
                case 4:
                    prepare_bill()
                case 5:
                    complete_sale()
                case 6:
                    cash_up()
                case 7:
                    login()
                case _:
                    print("Something went wrong try again :(")


if __name__ == '__main__':
    main_menu()
    