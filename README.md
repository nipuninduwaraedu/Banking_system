Python
OOP
Console App
Learning Project
Banking System
A console-based banking application built with Python. Developed to understand object-oriented programming, file handling, and core Python fundamentals.
Overview
This project lets users manage bank accounts through a menu-driven console interface. Users can create accounts, view records, deposit and withdraw funds, check balances, and delete accounts — with all data saved permanently using file handling.

Key concepts
Classes & Objects
Encapsulation
Methods & Constructors
Lists & Dictionaries
Loops & Conditions
File Handling
Exception Handling
Problem Solving
Project structure
banking_system/ ├── main.py # Menu-driven user interface ├── models/ │ └── bank_account.py # BankAccount class (data model) ├── services/ │ └── bank_service.py # Business logic & all operations └── data/ └── accounts.txt # Persistent account storage
Features
Create account
Add a new account with number, customer name, and initial balance.
View all accounts
Display a list of every saved account in the system.
Deposit & withdraw
Add funds or withdraw with an automatic balance check.
Check balance
View the current balance of any account instantly.
Delete account
Permanently remove an account from the system.
Data persistence
All data is saved to file and loaded automatically on startup.
How to run
1
Clone the repository
git clone https://github.com/nipuninduwaraedu/Banking_system.git
2
Navigate to the project folder
cd banking-system
3
Run the program
python main.py
Data storage format
# accounts.txt AccountNumber,CustomerName,Balance 1001,Nipun,5000.0 1002,Kamal,7000.0
Program flow
User input
→
main.py
→
BankService
→
BankAccount
→
accounts.txt
Limitations & future improvements
Current limitations
No login system
File storage only (no database)
Console-based, no GUI
No security features
Planned improvements
MySQL / SQLite database
User login system
Transaction history
GUI (Tkinter or web)
REST API (FastAPI / Flask)
Author
N
Nipun Induware
Built as a learning project for Python OOP practice and internship preparation.
github.com/nipuninduwaraedu/Banking_system
If you find this project useful, give it a star on GitHub and feel free to fork and improve it.
