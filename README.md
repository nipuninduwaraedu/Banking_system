<div align="center">

# 🏦 Banking System

**A console-based Banking System built with Python**

Developed to understand Object-Oriented Programming, file handling, and core Python fundamentals.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-FF6B6B?style=for-the-badge)
![Console](https://img.shields.io/badge/Type-Console%20App-4CAF50?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Learning%20Project-FFA500?style=for-the-badge)

</div>

---

## 📌 Overview

This project lets users manage bank accounts through a **menu-driven console interface**. Users can create accounts, view records, deposit and withdraw funds, check balances, and delete accounts — with all data saved permanently using file handling.

---

## 🧠 Key Concepts Used

| Concept | Description |
|---|---|
| 🏗️ Classes & Objects | Core building blocks of OOP |
| 🔒 Encapsulation | Bundling data with methods |
| ⚙️ Methods & Constructors | Defining behavior and initialization |
| 📋 Lists & Dictionaries | Core Python data structures |
| 🔁 Loops & Conditions | Control flow fundamentals |
| 📂 File Handling | Read/write persistent data |
| ⚠️ Exception Handling | Graceful error management |

---

## 📁 Project Structure

```
banking_system/
│
├── main.py                  # Menu-driven user interface
├── models/
│   └── bank_account.py      # BankAccount class (data model)
├── services/
│   └── bank_service.py      # Business logic & all operations
└── data/
    └── accounts.txt         # Persistent account storage
```

---

## ⚙️ Features

| # | Feature | Description |
|---|---|---|
| 1 | ➕ Create Account | Add account with number, name & initial balance |
| 2 | 👁️ View All Accounts | Display every saved account in the system |
| 3 | 💰 Deposit Money | Add funds to an existing account |
| 4 | 💸 Withdraw Money | Withdraw with automatic balance check |
| 5 | 🔍 Check Balance | View current balance of any account |
| 6 | 🗑️ Delete Account | Permanently remove an account |
| 7 | 💾 Data Persistence | Auto-save & load from file on startup |

---

## 🚀 How to Run

**Step 1 — Clone the repository**
```bash
git clone https://github.com/nipuninduwaraedu/Banking_system.git
```

**Step 2 — Navigate to the project folder**
```bash
cd banking-system
```

**Step 3 — Run the program**
```bash
python main.py
```

---

## 💡 Example Menu

```
===== BANKING SYSTEM =====
1. Create Account
2. View All Accounts
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Delete Account
7. Exit
==========================
```

---

## 📊 Data Storage Format

Data is stored in `accounts.txt` in the following format:

```
AccountNumber,CustomerName,Balance
1001,Nipun,5000.0
1002,Kamal,7000.0
```

---

## 🧩 Program Flow

```
User Input  →  main.py (menu)  →  BankService (logic)  →  BankAccount (model)  →  accounts.txt (storage)
```

---

## ⚠️ Current Limitations

> This is a learning project — the following features are not yet implemented:

- ❌ No login or authentication system
- ❌ No database (uses plain file storage)
- ❌ No GUI (console-based only)
- ❌ No security features

---

## 🔮 Future Improvements

- [ ] Database integration (MySQL / SQLite)
- [ ] User login & authentication system
- [ ] Transaction history log
- [ ] GUI using Tkinter or a web framework
- [ ] REST API backend using FastAPI or Flask

---

## 📚 Author

**Built by Nipun Induware** — as a learning project for Python OOP practice and internship preparation.

🔗 [github.com/nipuninduwaraedu/Banking_system](https://github.com/nipuninduwaraedu/Banking_system)

---

<div align="center">

⭐ **If you find this project useful, give it a star on GitHub!** ⭐

*Feel free to fork it and improve it.*

</div>
