import json

#Adds an expense with a specified amount and category
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

#Displays all recorded expenses
def print_expenses(expenses):
    for i, expense in enumerate(expenses, start=1):
        print(f'{i}. Amount: {expense["amount"]}, Category: {expense["category"]}')

#Calculates the total sum of all expenses
def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

#Filters expenses by a specific category
def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'] == category, expenses))

#Summarizes expenses by category, showing the total for each
def category_summary(expenses):
    summary = {}
    for expense in expenses:
        summary[expense['category']] = summary.get(expense['category'], 0) + expense['amount']
    return summary

#Saves the expenses to a JSON file (expenses.json)
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, 'w') as file:
        json.dump(expenses, file)

#Loads expenses from a JSON file
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
# Edits an existing expense's amount or category
def edit_expense(expenses):
    if not expenses:
        print("No expenses to edit.")
        return

    print('\nWhich expense would you like to edit?')
    print_expenses(expenses)

    try:
        index = int(input("Enter the number of the expense to edit: ")) - 1
        if 0 <= index < len(expenses):
            # Prompt for new values, allowing users to press Enter to keep the old value
            new_category = input(f"Enter new category for {expenses[index]['category']} (or press Enter to keep the same): ")
            new_amount = input(f"Enter new amount for {expenses[index]['amount']} (or press Enter to keep the same): ")

            # Update the expense if a new value was provided
            if new_category:
                expenses[index]['category'] = new_category
            if new_amount:
                try:
                    expenses[index]['amount'] = float(new_amount)
                except ValueError:
                    print("Invalid amount. Keeping the original amount.")
            print("Expense updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    expenses = load_expenses()

    while True:
        print('\n--- Expense Tracker ---')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Show category summary')
        print('6. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses:', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print(f'\nExpenses for {category}:')
            print_expenses(expenses_from_category)

        elif choice == '5':
            print("\nExpenses by Category:")
            summary = category_summary(expenses)
            for category, total in summary.items():
                print(f'{category}: {total}')

        elif choice == '6':
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                save_expenses(expenses)
                print('Exiting the program.')
                break

main()
