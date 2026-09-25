# Mini-ATM
🏧 Mini ATM System

A simple Mini ATM System developed using Python, Tkinter, and SQLite. This project simulates basic ATM operations through a graphical user interface (GUI).

📌 Project Overview

The Mini ATM System allows users to create and manage bank accounts and perform basic ATM operations such as checking balance, depositing money, withdrawing money, and viewing account information.

The project uses Tkinter to create the graphical interface and SQLite to store account information in a local database.

✨ Features

- 🔐 Account login
- 🆕 Create a new account
- 💰 Check account balance
- 💵 Deposit money
- 💸 Withdraw money
- 👤 Account information
- 🗄️ SQLite database for storing account data
- 🖥️ User-friendly graphical interface
- ⚠️ Input validation and error messages

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
Tkinter| Graphical User Interface
SQLite| Database management
sqlite3| Python module for SQLite database

📂 Project Structure

Mini-ATM/
│
├── atm.py
├── atm.db
├── README.md
└── screenshots/

«File names may be different depending on your project structure.»

⚙️ How It Works

1. Start the Application

Run the Python program:

python atm.py

The ATM application will open in a graphical window.

2. Create an Account

The user can enter the required account details and create a new account.

The account information is stored in the SQLite database.

3. Login

The user enters their account credentials to access the ATM system.

4. Perform ATM Operations

After successful login, the user can perform operations such as:

- Check Balance
- Deposit Money
- Withdraw Money
- View Account Details
- Logout

🗄️ Database

The project uses SQLite for local data storage.

The database file is:

atm.db

SQLite is useful for this project because it does not require a separate database server.

🔄 Basic Workflow

Start Application
       ↓
Create Account / Login
       ↓
Verify Account
       ↓
ATM Dashboard
       ↓
 ┌───────────────┐
 │ Check Balance │
 │ Deposit Money │
 │ Withdraw Money│
 │ Account Info  │
 │ Logout        │
 └───────────────┘
       ↓
      Exit

🎯 Purpose of the Project

The main purpose of this project is to understand how a real-world application can combine:

- Python programming
- GUI development
- Database connectivity
- User input handling
- Functions
- Conditional statements
- Error handling
- CRUD operations

📚 Learning Outcomes

Through this project, I learned:

- How to create a GUI using Tkinter
- How to create and connect an SQLite database
- How to insert, update, and retrieve database records
- How to create buttons and input fields
- How to use functions to organize a Python project
- How to validate user input
- How to connect a GUI application with a database

🚀 Future Improvements

Some features that can be added in the future:

- 🔑 Change PIN
- 📜 Transaction history
- 🧾 Generate transaction receipts
- 👥 Multiple account types
- 💳 Card number generation
- 🔒 Improved authentication and security
- 📊 Transaction reports
- 🌐 Online/database-server support

⚠️ Disclaimer

This is an educational mini-project created for learning purposes. It is not intended to be used as a real banking or ATM system.

👨‍💻 Author

Shailendra Rajak

This project was created as a learning project to practice Python, Tkinter, and SQLite.

⭐ If You Like This Project

If you find this project useful for learning, consider giving the repository a ⭐ on GitHub.
