🏦 Banking System (Python OOP Console Project)

A simple console-based Banking System built using Python.
This project is developed for  understand OOP, file handling, and basic of Python.

📌 Project Overview

This project allows users to manage bank accounts using a menu-driven console application.

Users can:

Create a new bank account
View all accounts
Deposit money
Withdraw money
Check account balance
Delete an account
Save data permanently using file handling
🧠 Key Concepts Used

This project helps you learn:

Object-Oriented Programming (OOP)
Classes and Objects
Encapsulation (basic level)
Methods and constructors
Lists and dictionaries
Loops and conditions
File handling (read/write)
Exception handling
Basic problem solving

📁 Project Structure
banking_system/
│
├── main.py                  # Main program (user interface)
├── models/
│   └── bank_account.py      # BankAccount class (data model)
├── services/
│   └── bank_service.py      # Business logic (all operations)
├── data/
│   └── accounts.txt        # Stores account data permanently


⚙️ Features
1. Create Account
Add a new bank account with:
Account Number
Customer Name
Initial Balance
2. View All Accounts
Display all saved accounts
3. Deposit Money
Add money to an existing account
4. Withdraw Money
Withdraw money with balance check
5. Check Balance
View current account balance
6. Delete Account
Remove an account permanently
7. Data Persistence
All data is saved in a file (accounts.txt)
Data is loaded when program starts

🚀 How to Run This Project
Step 1: Clone the repository
https://github.com/nipuninduwaraedu/Banking_system.git
Step 2: Go to project folder
cd banking-system
Step 3: Run the program
python main.py

💡 Example Menu
===== BANKING SYSTEM =====

1. Create Account
2. View All Accounts
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Delete Account
7. Exit
8. 
📊 Data Format (File Storage)

Data is stored in this format:

AccountNumber,CustomerName,Balance
1001,Nipun,5000.0
1002,Kamal,7000.0

🧩 How It Works (Simple Flow)

User Input
   ↓
main.py (menu)
   ↓
BankService (logic)
   ↓
BankAccount (data)
   ↓
File (storage)

⚠️ Limitations

This is a learning project:

No login system
No database (uses file storage only)
No GUI (console-based only)
No security features

🔮 Future Improvements

Database (MySQL / SQLite)
User login system
Transaction history
GUI (Tkinter or web app)
API backend (FastAPI / Flask)

📚 Author

Built as a learning project for Python OOP practice and internship preparation.

⭐ If you like this project

Give it a star ⭐ on GitHub and feel free to improve it.


