import json
import sqlite3

DB_FILE = "expenses.db"
EXPENSES_JSON = "expenses.json"

# Database setup
def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        amount REAL,
                        category TEXT,
                        description TEXT,
                        date TEXT)''')
    conn.commit()
    conn.close()

def add_expense(amount, category, description, date):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)", 
                   (amount, category, description, date))
    conn.commit()
    conn.close()

def load_expenses():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT amount, category, description, date FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def total_expenses():
    expenses = load_expenses()
    return sum(expense[0] for expense in expenses)

def category_summary():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    summary = cursor.fetchall()
    conn.close()
    return summary

def save_expenses_to_json():
    expenses = load_expenses()
    with open(EXPENSES_JSON, 'w') as file:
        json.dump([{'amount': e[0], 'category': e[1], 'description': e[2], 'date': e[3]} for e in expenses], file)

def load_expenses_from_json():
    try:
        with open(EXPENSES_JSON, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

