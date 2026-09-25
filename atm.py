import sqlite3
import tkinter as tk
from tkinter import messagebox

current_account = None

# --- Database functions ---
def init_db():
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts (
                    account_number TEXT PRIMARY KEY,
                    pin TEXT NOT NULL,
                    balance REAL NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_number TEXT NOT NULL,
                    type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    balance_after REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    # Add a sample account if none exists
    c.execute("SELECT * FROM accounts")
    if not c.fetchall():
        c.execute("INSERT INTO accounts VALUES ('123456', '4321', 5000.0)")
    conn.commit()
    conn.close()

def get_account(account_number, pin):
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE account_number=? AND pin=?", (account_number, pin))
    result = c.fetchone()
    conn.close()
    return result

def create_account():
    account_number = simple_input("Enter new account number:")
    if not account_number:
        return

    pin = simple_input("Enter PIN:")
    if not pin:
        return

    balance = simple_input("Enter initial balance:")
    if not balance:
        return

    try:
        balance = float(balance)

        conn = sqlite3.connect("atm.db")
        c = conn.cursor()

        # Check if account already exists
        c.execute(
            "SELECT * FROM accounts WHERE account_number=?",
            (account_number,)
        )

        if c.fetchone():
            messagebox.showerror(
                "Error",
                "Account number already exists!"
            )
            conn.close()
            return

        # Create new account
        c.execute(
            "INSERT INTO accounts (account_number, pin, balance) VALUES (?, ?, ?)",
            (account_number, pin, balance)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Account created successfully!"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid balance."
        )

def update_balance(account_number, new_balance):
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, account_number))
    conn.commit()
    conn.close()

def log_transaction(account_number, t_type, amount, balance_after):
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (account_number, type, amount, balance_after) VALUES (?, ?, ?, ?)",
              (account_number, t_type, amount, balance_after))
    conn.commit()
    conn.close()

def get_transactions(account_number):
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("SELECT type, amount, balance_after, timestamp FROM transactions WHERE account_number=? ORDER BY timestamp DESC", (account_number,))
    result = c.fetchall()
    conn.close()
    return result

# --- GUI functions ---
def login():
    global current_account
    acc = acc_entry.get()
    pin = pin_entry.get()
    account = get_account(acc, pin)
    if account:
        current_account = account
        messagebox.showinfo("Login", "Login successful!")
        show_menu()
    else:
        messagebox.showerror("Error", "Invalid account or PIN")

def check_balance():
    messagebox.showinfo("Balance", f"Your balance is ₹{current_account[2]}")

def deposit():
    global current_account
    amount = simple_input("Enter deposit amount:")
    if amount:
        new_balance = current_account[2] + float(amount)
        update_balance(current_account[0], new_balance)
        log_transaction(current_account[0], "Deposit", float(amount), new_balance)
        current_account = (current_account[0], current_account[1], new_balance)
        messagebox.showinfo("Deposit", f"Deposited ₹{amount}. New balance: ₹{new_balance}")

def withdraw():
    global current_account
    amount = simple_input("Enter withdrawal amount:")
    if amount:
        if float(amount) <= current_account[2]:
            new_balance = current_account[2] - float(amount)
            update_balance(current_account[0], new_balance)
            log_transaction(current_account[0], "Withdraw", float(amount), new_balance)
            current_account = (current_account[0], current_account[1], new_balance)
            messagebox.showinfo("Withdraw", f"Withdrew ₹{amount}. New balance: ₹{new_balance}")
        else:
            messagebox.showerror("Error", "Insufficient funds")

def view_transactions():
    txns = get_transactions(current_account[0])
    if not txns:
        messagebox.showinfo("Transactions", "No transactions found.")
        return
    txn_win = tk.Toplevel(root)
    txn_win.title("Transaction History")
    for t in txns:
        tk.Label(txn_win, text=f"{t[3]} - {t[0]} ₹{t[1]} (Balance: ₹{t[2]})").pack()

def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("ATM Menu")

    tk.Button(menu_window, text="Check Balance", command=check_balance).pack(pady=5)
    tk.Button(menu_window, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(menu_window, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(menu_window, text="View Transactions", command=view_transactions).pack(pady=5)

def simple_input(prompt):
    input_win = tk.Toplevel(root)
    input_win.title("Input")
    tk.Label(input_win, text=prompt).pack()
    entry = tk.Entry(input_win)
    entry.pack()
    result = []

    def submit():
        result.append(entry.get())
        input_win.destroy()

    tk.Button(input_win, text="Submit", command=submit).pack()
    input_win.wait_window()
    return result[0] if result else None

# --- Main window ---
root = tk.Tk()
root.title("ATM Login")

tk.Label(root, text="Account Number").pack()
acc_entry = tk.Entry(root)
acc_entry.pack()

tk.Label(root, text="PIN").pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

tk.Button(root, text="Login", command=login).pack()
tk.Button(
    root,
    text="Create Account",
    command=create_account
).pack(pady=5)

init_db()
root.mainloop()

