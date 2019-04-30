import math

""" Primary Program Variables """
# Rent for Austin Waters:
RENT = 0

# Current AT&T Internet and TV Bundle:
INTERNET = 0

# Allowance for Utilities:
UTIL = 0

# Paying parents back for phone, insurance, etc.:
REIMBURSE_PARENTS = 0

# This a lump sum meant for paying 2520 rent, which will eventually be used
# towards student loans:
STULOANS = 0

# Estimate for gas/fuel expenses:
GAS = 0

# Estimate for groceries:
GROCERIES = 0

# Any potential lump sums not addressed:
ADDITIONAL = 0

# The last date that these amounts were updated/recalculated:
DATE = "April 29th, 2019"

# This is the amount of money I can expect to see in my paycheck:
PAY = 0

""" End Primary Program Variables """

# File reading
def readVars():
    global RENT
    global INTERNET
    global UTIL
    global REIMBURSE_PARENTS
    global STULOANS
    global GAS
    global GROCERIES
    global ADDITIONAL
    global DATE
    global PAY
    file1 = open("vars.txt","r")
    RENT = int(file1.readline())
    INTERNET = int(file1.readline())
    UTIL = int(file1.readline())
    REIMBURSE_PARENTS = int(file1.readline())
    STULOANS = int(file1.readline())
    GAS = int(file1.readline())
    GROCERIES = int(file1.readline())
    ADDITIONAL = int(file1.readline())
    DATE = str(file1.readline())
    PAY = float(file1.readline())
    file1.close()
    return

def writeVars():
    global RENT
    global INTERNET
    global UTIL
    global REIMBURSE_PARENTS
    global STULOANS
    global GAS
    global GROCERIES
    global ADDITIONAL
    global DATE
    global PAY
    # try:
    file1 = open("vars.txt","w")
    file1.write(str(RENT) + '\n')
    file1.write(str(INTERNET) + '\n')
    file1.write(str(UTIL) + '\n')
    file1.write(str(REIMBURSE_PARENTS) + '\n')
    file1.write(str(STULOANS) + '\n')
    file1.write(str(GAS) + '\n')
    file1.write(str(GROCERIES) + '\n')
    file1.write(str(ADDITIONAL) + '\n')
    userIN = (str(input("What is today's date?")) + '\n')
    DATE = userIN
    file1.write(userIN)
    file1.write(str(PAY) + '\n')
    file1.close()
    # except:
    # print("ERROR. Changes not saved.")
        

# The following three lists are lists used to process user Inputs:
yesList = ["Yes", "yes", "Y", "y"]
noList = ["No", "no", "N", "n"]
quitList = ["Quit", "quit", "Exit", "exit", "Stop", "stop"]

# printExpenses() prints an easy to read summary of what I'm spending on (and how much on each)
def printExpenses():
    print("\nAs of {} the following are the calculations for my expenses:".format(DATE))
    print("Rent: ${}".format(RENT))
    print("Internet/Cable: ${}".format(INTERNET))
    print("Utilities: ${}".format(UTIL))
    print("Paying Parents: ${}".format(REIMBURSE_PARENTS))
    print("Student Loans: ${}".format(STULOANS))
    print("Gas Estimate: ${}".format(GAS))
    print("Grocery Estimate: ${}".format(GROCERIES))
    print("Additional Costs: ${}\n".format(ADDITIONAL))

# getTotalCosts() returns a float of the money I'm spending
def getTotalCosts():
    return (RENT + INTERNET + UTIL + REIMBURSE_PARENTS + STULOANS + GAS + GROCERIES + ADDITIONAL)

# getMonthlyPay() will return an estimate of how much I take home per month (2 paychecks)
def getMonthlyPay():
    return (PAY*2)

# printPay() will print my  take-home pay info; so after all witholdings (single paycheck and monthly)
def printPay():
    print("\nPaycheck: ${}".format(PAY))
    print("Monthly: ${}".format(getMonthlyPay()))

# getAvailableFunds() will return the amount of funds available after paying all expenses.
def getAvailableFunds():
    return (getMonthlyPay()-getTotalCosts())

# def calcPercentage(percent, base) takes a percentage and a base number. It returns the percentage OF the base number
def calcPercentage(percent, base):
    return ((percent*base)/100)

# savingsOptions will direct the user through showing different amounts/percentages they can put into savings
# based upon how much they are making/spending from month to month
def savingsOptions():
    avail = getAvailableFunds()
    print("\nAssuming your expenses are for the month, and that you get 2 paychecks/month, you could save:")
    print("\nIf you don't put anything into savings, you will have ${} of available funds".format(math.floor(avail)))
    input("")
    print("\n5% of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(5,avail)),math.floor(calcPercentage(95,avail))))
    input("")
    print("\n10% of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(10,avail)),math.floor(calcPercentage(90,avail))))
    input("")
    print("\n15% of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(15,avail)),math.floor(calcPercentage(85,avail))))
    input("")
    print("\n20% of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(20,avail)),math.floor(calcPercentage(80,avail))))
    input("")
    print("\n25% (1/4) of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(25,avail)),math.floor(calcPercentage(75,avail))))
    input("")
    print("\n33% (1/3) of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(33,avail)),math.floor(calcPercentage(66,avail))))
    input("")
    print("\n50% (1/2) of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(50,avail)),math.floor(calcPercentage(50,avail))))
    input("")
    print("\n66% (2/3) of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(66,avail)),math.floor(calcPercentage(33,avail))))
    input("")
    print("\n75% (3/4) of your free funds, and put ${} into savings.\n   You would have ${} left over.".format(math.floor(calcPercentage(75,avail)),math.floor(calcPercentage(25,avail))))
    input("")
    print("\nOr, you can put all leftover money into savings: 100% = ${}".format(math.floor(avail)))

# setTempVals() is called upon if the user does not want to use the pre-calculated values for expenses/pay.
def setTempVals():
    global RENT
    global INTERNET
    global UTIL
    global REIMBURSE_PARENTS
    global STULOANS
    global GAS
    global GROCERIES
    global ADDITIONAL
    global PAY
    while(True):
        try:
            RENT = int(input("What do you pay for rent?\n>>"))
            INTERNET = int(input("What do you pay for Internet/Cable?\n>>"))
            UTIL = int(input("What do you pay for Utilities?\n>>"))
            REIMBURSE_PARENTS = int(input("Amount paying others for repayment and/or services?\n>>"))
            STULOANS = int(input("How much do you pay in (student) loans?\n>>"))
            GAS = int(input("How much do you expect to pay in Gas this month?\n>>"))
            GROCERIES = int(input("How much do you expect to pay in Grocieries this month?\n>>"))
            ADDITIONAL = int(input("Enter any additional costs you expect to have this month\n>>"))
            PAY = float(input("How much do you expect to earn in on paycheck this month?\n>>"))
            break
        except:
            print("Something went wrong. For all entries except for Pay, please use integers")
            continue
    userIn= input("Would you like to set these as your permanent values?")
    if userIn in yesList:
        writeVars()
    mainMenu()


# processUserChoice() takes the input from main menu and executes the proper program functionality
def processChoice (userIn):
    if userIn == "1":
        print("\n-- BEGIN EXPENSE REPORT --")
        printExpenses()
        input("Press Enter to Continue")
        print("-- END EXPENSE REPORT --")
        mainMenu()
    elif userIn == "2":
        print("\n-- BEGIN EARNINGS REPORT --")
        printPay()
        input("Press Enter to Continue")
        print("-- END EARNINGS REPORT --")
        mainMenu()
    elif userIn == "3":
        print("\n-- BEGIN FREE FUNDS --")
        print("\nAfter expenses, you have ${} free this month".format(math.floor(getAvailableFunds())))
        input("Press Enter to Continue")
        print("-- END FREE FUNDS --")
        mainMenu()
    elif userIn == "4":
        print("\n-- BEGIN SAVINGS PLAN --")
        savingsOptions()
        input("Press Enter to Continue")
        print("-- END SAVINGS PLAN --")
        mainMenu()
    elif userIn in quitList:
        main()
    else:
        print("\nResponse not recognized. Please try again")
        input("Press Enter to Continue")
        mainMenu()

# mainMenu will show the main options for using the program
def mainMenu():
    print("\n1) Print Expenses")
    print("2) Print Pay")
    print("3) Print Available Funds")
    print("4) Show options for saving this month")
    userIn = str(input(">>"))
    processChoice(userIn)

# main will initialize the program
def main():
    while(True):
        print("Welcome to my Budgeting App!")
        printExpenses()
        input("Press Enter to Continue")
        print("Do these values seem right? Yes = Continue | No = Input new values | Quit = Exit Program\n")
        userIn = input(">>")
        if userIn in yesList:
            mainMenu()
        elif userIn in noList:
            setTempVals()
        elif userIn in quitList:
            break
        else:
            print("Invalid response, please try again")
            continue

readVars()
main()





