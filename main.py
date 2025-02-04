from expense_manager import setup_db, add_expense, load_expenses, total_expenses, category_summary

def main():
    setup_db()
    expenses = load_expenses()

    while True:
        print('\n--- Expense Tracker ---')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Show category summary')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            category = input('Enter category: ')
            description = input('Enter description: ')
            date = input('Enter date (YYYY-MM-DD): ')
            add_expense(amount, category, description, date)

        elif choice == '2':
            print('\nAll Expenses:')
            for expense in load_expenses():
                print(f'Amount: {expense[0]}, Category: {expense[1]}, Description: {expense[2]}, Date: {expense[3]}')

        elif choice == '3':
            print('\nTotal Expenses:', total_expenses())

        elif choice == '4':
            print("\nExpenses by Category:")
            summary = category_summary()
            for category, total in summary:
                print(f'{category}: {total}')

        elif choice == '5':
            print('Exiting the program.')
            break

if __name__ == "__main__":
    main()
