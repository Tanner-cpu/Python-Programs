import string
#These open the input and output file.
Infile = open("pythonIn.txt", "r")
Outfile = open("pythonOut.txt", "w")
#This function operates by reading through the database and displays each indivudal key and its values
def displayData():
    print()
    for key in sorted(dictionary.keys()):
        print("%s: %s" % (key, dictionary[key]))
        
#This function takes an item number arguement and searches it in the dictionary. If the number is found,
#then it prints the values that are held within that key. And error is given if the part number was not
#found in the dictionary.
def displayPart(number):
    if partNumber in dictionary:
        print("Part Name:",dictionary[partNumber][0],"  
Price:",dictionary[partNumber][1]," Quantity Available:",dictionary[partNumber][2])
    else:
        print("ERROR: Part was not found.")
#This function takes an arguement of an item number, and searches if the given item key is already in the
#dictionary. If it is, it prints an error. If not, it allows the user to fill in a name, price,
#and the quantity available for a new item. After the data has been filled in, it adds the new item to the
#database.
def addPart(number):
    if newItemNumber in dictionary:
        print("ERROR: This item number is already in the list.")
    else:
        newName = str(input("Part Name: "))
        newPrice = float(input("Part Price: "))
        newPrice = round(newPrice, 2)
        newQuantity = int(input("Quantity Available: "))
        dictionary[newItemNumber] = newName, newPrice, newQuantity
        print("SUCCESS: Item was successfully added to the list!")  
#This function sorts the data in order according to the keys, and writes it to the output file.
#the \t is used for spacing, so the data is neatly presented. 
def outfileData():
    Outfile.write("Part Number\tPart Name\tPart Price\tPart Quantity\n")
    for key in sorted(dictionary.keys()):
        Outfile.write("%s\t\t%s\t%s\t\t%s\n" % (key,dictionary[key]
[0],dictionary[key][1],dictionary[key][2]))
#This function reads in strings from an input file, and splits up each individual lines into four
#separate parts, assuming the lines in the input file has only 4 columns of data. It, then, converts
#the first and fourth part into integers, and the third part into a float. Lastly, it stores the data
#in a dictionary.
def loadDictionary():
    for line in Infile:
        myString = line
        myPart = myString.split()
        myPart[0] = int(myPart[0])
        myPart[2] = float(myPart[2])
        myPart[3] = int(myPart[3])
        dictionary[myPart[0]] = myPart[1], myPart[2], myPart[3]
#This function evaluates the input of the user when it comes to yes or no decision making. It reads
#in the input as a string and converts it to lowercase. It, then, compares that string to 'no' or 'yes'
#and returns True or False to evalaute the decision. If the user inputs any other string, an error is
#printed to the screen. 
def continueDecision():
    while True:
        resumeSearch = str(input("Would you like to try this task again? (yes or 
no): ").lower())
        if resumeSearch == 'no':
            print()
            return False
        elif resumeSearch == 'yes':
            return True
        else:
            print("INVALID INPUT: Please type yes or no.")
#This function allows the user to stock the quantity available of any certain item in the dictionary.
#It takes the argument of an item number, and displays the current amount available for that item. It,
#then, asks how much would the user like to add. Lastly, it calculates the new quantity available for
#that item, and assigns the new values to the dictionary. 
def stockItem(number):
    print("The current quantity available for this part(",dictionary[restockItem]
[0],") is",dictionary[restockItem][2])
    increaseQuantity = int(input("Enter the amount of available items you would 
like to add: "))
    newQuantity = dictionary[restockItem][2] + increaseQuantity
    newQuantity = int(newQuantity)
    dictionary[restockItem] = dictionary[restockItem][0], dictionary[restockItem]
[1], newQuantity
    print("SUCCESS: The new quantity available for this 
part(",dictionary[restockItem][0],") is",dictionary[restockItem][2])
#This function takes in the argument of an item number and calculates an order for it. It prompts the user
#to input the quantity ordered. If there is enough quantity available for that order, it calculates the order, and prints
#a reciept. It, then, asks for confirmation. If the user chooses yes, then it affects the data in the database. If not,
#it leaves the data unchanged. It prints an error for an invalid input. If the item did not have enough in stock
#to complete the order, it notifies how many are left in stock. If the item is sold out, it notifies the user as well. 
def calculateOrder(item):
    confirmation = False
    orderedQuantity = int(input("Enter the quantity desired: "))
    if orderedQuantity <= dictionary[orderedItem][2]:
        total = orderedQuantity * dictionary[orderedItem][1]
        salesTax = 0.10 * total
        total = salesTax + total
        total = round(total, 2)
        print("\nPart Name:",dictionary[orderedItem][0],"\nPart 
Number:",orderedItem,"\nPart Price: $",dictionary[orderedItem][1],"\nQuantity 
Ordered:",orderedQuantity,"\nTotal: $",total)
        while confirmation == False:
            confirm = str(input("\nWould you like to confirm this purchase?(yes or 
no): ").lower())
            if confirm == 'yes':
                newQuantityAvailable = dictionary[orderedItem][2] - orderedQuantity
                newQuantityAvailable = int(newQuantityAvailable)
                dictionary[orderedItem] = dictionary[orderedItem][0], 
dictionary[orderedItem][1], newQuantityAvailable
                print("SUCCESS: Your order was complete.")
                confirmation = True;
            elif confirm == 'no':
                print("We're sorry to hear that.")
                confirmation = True;
            else:
                print("INVALID INPUT: Please type yes or no")
                            
    else:
        print("ERROR: Not enough stock available to place this order")
        if dictionary[orderedItem][2] == 0:
            print("This part is currently sold out.")
        else:
            print("Quantity available:",dictionary[orderedItem][2])
#This skips the header line in the input file.       
next(Infile)
dictionary = {}
#This calls the function to load the dictionary.
loadDictionary()
#This prints an introduction of the program.
print("""Name: Tanner Boswell\nClass: CS 424-01 Principles of Programming 
Languages\n
This program reads in data from a text file
that includes the attributes of many items, and
stores the given data into a functional database.
The user is able to retrieve item data, place orders
for any available item, restock the quantity of any
item, and add any desired item to the database.
Afterwards, the updated database is written onto
another file.
""")
#This assigns the contents of the main menu to variables that be reused.
text = "Main Menu"
menuTitle = text.center(24)
menu = """1. Display Database
2. Retrieve Item Data
3. Place Order
4. Restock Item
5. Add Item
6. Terminate
"""
#This loop continues until the user selects the option to terminate the program. 
while True:
    #These print the menu to the screen, and prompts the user to select an option
    #in if-elif-else format.
    print(menuTitle)
    print(menu)
    Infile.seek(0)
    x = (input("Select an option from the menu: "))
    #If the user selects option 1, the program displays the data by calling the
    #displayData function. 
    if x == '1':
        displayData()
        print("\n")
    #If the user selects option 2, the program prompts the user to enter an item
    #number, calls the displayPart function, and loops until the continueDecision
    #function is equal to false, which turns runOption2 to false.
    elif x == '2':
        runOption2 = True
        while runOption2 == True:
            partNumber = int(input("Enter a part number to retrieve item data: "))
            displayPart(partNumber)
            if continueDecision()== False:
                runOption2 = False
                
    #If the user selects option 3, the program prompts the user to enter an item
    #number they would like to order. If the item is found in the dictionary, it
    #calls the calculateOrder function. If the item number was not found, it prints
    #an error to the sceen. It loops this option until the continueDecision 
function
    #is equal to false, which turns runOption3 to false. 
    elif x == '3':
        runOption3 = True
        while runOption3 == True:
            orderedItem = int(input("Enter the part number you would like to order:
"))
            if orderedItem in dictionary:
                calculateOrder(orderedItem)
            else:
                print("ERROR: Part was not found.")
            if continueDecision()== False:
                runOption3 = False
                
    #If the user selects option 4, the program prompts the user to enter the item
    #number of the part that will be restocked. If the item is found in the 
dictionary,
    #it calls the stockItem function. If the item was not found, it prints an error
to
    #the screen. It loops this option until the continueDecision function is equal 
to
    #false, which turns runOption4 to false.
    elif x == '4':
        runOption4 = True
        while runOption4 == True:
            restockItem = int(input("Enter the part number of the item that needs 
to be restocked: "))
            if restockItem in dictionary:
                stockItem(restockItem)
            else:
                print("ERROR: Part was not found.")
            if continueDecision()== False:
                runOption4 = False
    #If the user selects option 5, the program prompts the user to enter the item
    #number of the item that will be added to the list. It, then, calls the addPart
    #function, and loops this option until the continueDecision function is equal 
to
    #false, which turns runOption5 to false. 
    elif x == '5':
        runOption5 = True 
        while runOption5 == True:
            newItemNumber = int(input("Enter the item number you wish to add to the
list: "))
            addPart(newItemNumber)
            if continueDecision()== False:
                runOption5 = False
    #If the user selects option 6, the program calls the outfileData function and 
breaks from
    #the loop of the main menu.
    elif x == '6':
        outfileData()
        break;
    #If the user selects an option that isn't available, it prints an error to the 
screen. 
    else:
        print("ERROR: Invalid option.\n")
#This notifies the user that the program is complete, and closes the used files.
print("Program Complete")
Infile.close()
Outfile.close()
