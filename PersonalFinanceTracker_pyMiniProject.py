# Expense Tracker Project ( THIS PROJECT ALLOW USER TO CALCULATE HIS/HER DAILY EXPENSES AND VIEW SUMMARIES
# LIKE tOTAL SPENDING) 


#list of all expenses in the form of dictionary 
expensesList = []

print("Welcome to Expense Tracker")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")
    
    choice = int(input("Please Enter Your Choice : "))
    
    
    # if user choose option 1
    if (choice == 1):
        date = input("Enter Date: Kis Din Khrcha Kiya Tha? :---- ")
        category = input("Enter the Type of Expence like food,traveling,shoping etc :----- ")
        description = input("Enter Short Description like Manali Trip :----- ")
        amount = float(input("Enter your Amount :---- "))
        
        expense = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        
        expensesList.append(expense)
        print(" \n DONE. Your Expense is added Successfully")
        
        # Calculate total expense so far
        total = 0

        for each_expense in expensesList:
            total = total + each_expense['amount']

        print(f"Previous + Current Expense = ₹{total:.2f}")
        print(f"FULL TOTAL EXPENSE = ₹{total:.2f}")
        
    
        
    # if user choose option 2    
    elif (choice == 2):
        if(len(expensesList)==0):
            print("No Expense Added.")
        else:
            print("Here is your All the Expenses")    
            count = 1
            for eachKharcha in expensesList:
                print(f"\n Expense No {count} -> {eachKharcha['date']}, {eachKharcha['category']}, {eachKharcha['description']}, {eachKharcha['amount']}")
                
                count = count+1
                
    # if choice is 3 : View Total Expending            
    elif (choice == 3):
        total = 0
        for eachkhrcha in expensesList:
            total = total + eachkhrcha['amount']
            
        print("\n TOTAL EXPENSE = ",total) 
        
    
    # if user choose 4 : to Exit        
        
    elif (choice == 4):
        print("ThankYou For using Expense Tracker")
        break
    
    else:
        print("Invalid Choice")
        
         