expenses_details = []

menu = {
    1: "Add Expense",
    2: "View All Expenses",
    3: "Total Spending",
    4: "Category Analysis",
    5: "Highest Expense",
    6: "Lowest Expense",
    7: "Search Expenses",
    8: "Delete Expense",
    9: "Update Expense",
    10: "Exit"
}

def expense_tracker():
    next_id = 1
    while True:
        print("\n==== EXPENSE TRACKER ====\n")
        for number, option in menu.items():
            print(f"{number}. {option}")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            expense = {
                "id": 1,
                "amount": 0,
                "category": "",
                "date": "",
                "description": ""
            }
            while True:
                try:
                    amount = int(input("Enter amount: "))
                    if amount > 0:
                        break
                    else:
                        print("Amount must be greater than zero.")
                except ValueError:
                    print("Please enter a valid amount.")
            category = input("Enter category: ")
            date = input("Enter date: ")
            description = input("Enter description: ")
            expense["id"] = next_id
            expense["amount"] = amount
            expense["category"] = category
            expense["date"] = date
            expense["description"] = description
            print("\nExpense added successfully")
            expenses_details.append(expense)
            print(f'\nExpense Details:\nID: {expense["id"]}\nAmount: ₹{expense["amount"]}\nCategory: {expense["category"]}\nDate: {expense["date"]}\nDescription: {expense["description"]}')
            next_id += 1

        elif choice == 2:
            if not expenses_details:
                print("No expenses recorded yet.")
            for expenses in expenses_details:
                print(f'\nExpense Details:\nID: {expenses["id"]}\nAmount: ₹{expenses["amount"]}\nCategory: {expenses["category"]}\nDate: {expenses["date"]}\nDescription: {expenses["description"]}')
                print("---------------------------")

        elif choice == 3:
            total = 0
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                for total_amount in expenses_details:
                    total += total_amount["amount"]
                print("\n==== TOTAL SPENDING ====\n")
                print(f"Total Amount Spent: ₹{total}")

        elif choice == 4:
            category_analysis = {}
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                for category in expenses_details:
                    if category["category"] not in category_analysis:
                        category_analysis[category["category"]] = category["amount"]
                    else:
                        category_analysis[category["category"]] += category["amount"]
                print("\n==== CATEGORY ANALYSIS ====\n")
                for category_name, total_amount in category_analysis.items():
                    print(f"{category_name.capitalize()}: ₹{total_amount}")

        elif choice == 5:
            highest_expense = 0
            highest_expense_details = {}
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                print("\n==== HIGHEST EXPENSE ====\n")
                for expense in expenses_details:
                    if not highest_expense_details or expense["amount"] > highest_expense:
                        highest_expense = expense["amount"]
                        highest_expense_details = expense
                print(f'ID: {highest_expense_details["id"]}\nAmount: ₹{highest_expense_details["amount"]}\nCategory: {highest_expense_details["category"]}\nDate: {highest_expense_details["date"]}\nDescription: {highest_expense_details["description"]}')

        elif choice == 6:
            lowest_expense = 0
            lowest_expense_details = {}
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                print("\n==== LOWEST EXPENSE ====\n")
                for expense in expenses_details:
                    if not lowest_expense_details or expense["amount"] < lowest_expense:
                        lowest_expense = expense["amount"]
                        lowest_expense_details = expense
                print(f'ID: {lowest_expense_details["id"]}\nAmount: ₹{lowest_expense_details["amount"]}\nCategory: {lowest_expense_details["category"]}\nDate: {lowest_expense_details["date"]}\nDescription: {lowest_expense_details["description"]}')

        elif choice == 7:
            search_expenses_details = []
            search = input("Enter a search term: ")
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                print("\n==== SEARCH EXPENSE ====\n")
                for expense in expenses_details:
                    if search.lower() in expense["category"].lower() or search.lower() in expense["description"].lower():
                        search_expenses_details.append(expense)
                if not search_expenses_details:
                    print("No matching expenses found.")
                else:
                    for expense in search_expenses_details:
                        print(f'ID: {expense["id"]}\nAmount: ₹{expense["amount"]}\nCategory: {expense["category"].capitalize()}\nDate: {expense["date"]}\nDescription: {expense["description"].capitalize()}')
                        print("---------------------------")

        elif choice == 8:
            while True:
                try:
                    delete = int(input("Enter the ID of expense to delete: "))
                    if delete > 0:
                        break
                    else:
                        print("Expense ID must be a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                print("\n==== EXPENSE DELETION ====\n")
                for expense in expenses_details:
                    if delete == expense["id"]:
                        expenses_details.remove(expense)
                        print(f"Expense with ID {expense['id']} is deleted successfully.")
                        break
                else:
                    print("Expense ID not found.")

        elif choice == 9:
            while True:
                try:
                    update = int(input("Enter the ID of expense to update: "))
                    if update > 0:
                        break
                    else:
                        print("Expense ID must be a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")
            if not expenses_details:
                print("No expenses recorded yet.")
            else:
                print("\n==== EXPENSE UPDATE ====\n")
                for expense in expenses_details:
                    if update == expense["id"]:
                        expense["amount"] = int(input("Enter updated amount: "))
                        expense["category"] = input("Enter updated category: ")
                        expense["date"] = input("Enter updated date: ")
                        expense["description"] = input("Enter updated description: ")
                        print("\n==== UPDATED EXPENSE ====\n")
                        print(f'ID: {expense["id"]}\nAmount: ₹{expense["amount"]}\nCategory: {expense["category"].capitalize()}\nDate: {expense["date"]}\nDescription: {expense["description"].capitalize()}')
                        break
                else:
                    print("Expense ID not found.")

        elif choice == 10:
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Please choose a number from menu")


expense_tracker()