import json
with open("expenses.json","r") as file:
    expenses = json.load(file)

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    try:
        amount=int(input("enter the amount:"))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    if amount<=0:
        print("Amount must be greater than 0.")
        return
    
    category=input("enter category:").strip()
    if not category:
        print("Category cannot be empty.")
        return
    
    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    expense = {
            "amount": amount,
            "category": category,
            "description": description
            }
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    print("========== EXPENSES ==========")
    if expenses:
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. ₹{expense['amount']} | {expense['category']} | {expense['description']}")
    else:
        print("no expenses found")

def search_expenses():
    user=input("enter category:").lower()
    found = False
    for expense in expenses:
        if expense["category"].lower() == user:
            print(f"₹{expense['amount']} | {expense['category']} | {expense['description']}")
            found=True

    if not found:
        print(f"No expenses found for {user}.")

def delete_expense():
    if expenses:
        print("========== EXPENSES ==========")
        for i,expense in enumerate(expenses,1):
            print(f"{i} | {expense['amount']} | {expense['category']} | {expense['description']}")
            
        try:
            del_expense = int(input("Enter expense number to delete:"))
        except ValueError:
            print("Please enter a valid number.")
            return
        if 1 <= del_expense <= len(expenses):
            index=del_expense-1
            expenses.pop(index)
            save_expenses()
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number")
    else:
        print("No expenses found")

def view_statistics():
    print("========== STATISTICS ==========")
    total_expenses=len(expenses)
    total_amount=0
    for expense in expenses:
        total_amount+=expense['amount']
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        if category in category_totals:
            category_totals[category] += expense["amount"]
        else:
            category_totals[category] = expense["amount"]


    print(f"Total expenses: {total_expenses}")
    print(f"Total amount spent: ₹{total_amount}")
    print()
    print("Category spending:")
    for key,value in category_totals.items():
        print(f"{key}: {value}")




    

while True:
    print("================================")
    print("      PERSONAL EXPENSE TRACKER")
    print("================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Delete Expense")
    print("5. View Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_expense()
        case "2":
            view_expenses()
        case "3":
            search_expenses()

        case "4":
            delete_expense()
        case "5":
            view_statistics()

        case "6":
            break
        case _:
            print("invalid choice")