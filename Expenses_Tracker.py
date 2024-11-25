import time
user_name=input("Hey! What is Your Name?: ")
print(f"Welcome {user_name.capitalize()} For Your Daily Expenses")
print("Please Wait Your Your Application is Loading..")
time.sleep(4)
class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        print(f"Expense '{description}' added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\n--- Expenses List ---")
        for expense in self.expenses:
            print(f"{expense.description} | {expense.amount} | {expense.category}")
        print()

    def category_summary(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = 0
            categories[expense.category] += expense.amount
        
        print("\n--- Category Summary ---")
        for category, total in categories.items():
            print(f"{category}: {total}")
        print()

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: {total}\n")

    def delete_expense(self, description):
        found = False
        for expense in self.expenses:
            if expense.description.lower() == description.lower():
                self.expenses.remove(expense)
                print(f"Expense '{description}' deleted successfully!")
                found = True
                break
        if not found:
            print(f"Expense with description '{description}' not found.")

    def delete_all_expenses(self):
        self.expenses.clear()
        print("All expenses have been deleted.")

tracker = ExpenseTracker()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Category Summary")
    print("4. View Total Expenses")
    print("5. Delete a Specific Expense")
    print("6. Delete All Expenses")
    print("7. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        tracker.add_expense(description, amount, category)
    
    elif choice == '2':
        tracker.view_expenses()
    
    elif choice == '3':
        tracker.category_summary()
    
    elif choice == '4':
        tracker.total_expenses()
    
    elif choice == '5':
        description = input("Enter the description of the expense to delete: ")
        tracker.delete_expense(description)
    
    elif choice == '6':
        tracker.delete_all_expenses()
    
    elif choice == '7':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice, please try again.")
