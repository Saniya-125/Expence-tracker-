# Expense Tracker Project...

expenses =[] #list of expenses in form of dictionary
print("Welcome!✨ to Expense Tracker💸💶🪙")

while True:
    print("==== MENU ====")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Spendings")
    print("4.Exit")

    choice=int(input("Please enter your choice: "))
# Add Expense
    if(choice ==1):
        date=input("Enter date: ")
        category= input ("enter catogery: ")
        description = input ("give more details of your spending")
        amount = float(input("Enter the amount you spend: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount,
        }

        expenses.append(expense)
        print("\n Expenses added Successfully!")

# view all expenses
    elif(choice ==2):
        if (len(expenses)==0):
            print("no expenses added,Kindly add the expenses")
        else:
            print("========this is your all spendings=========")
            count= 1
            for eachSpending in expenses:
                print(f" Expense number{count} -->{eachSpending["date"]},{eachSpending["category"]},{eachSpending["description"]},{eachSpending["amount"]},") 
                count= count+1

#view total spending
    elif(choice ==3):
        total= 0
        for eachSpending in expenses:
            total= total+eachSpending["amount"]

        print("Total amount =",total)

#exit
    elif(choice ==4):
        
            print("Thankyou for using our system.")
            break
        
#invalid choise
    else:
        print("Invalid choice,Try Again ")
    
