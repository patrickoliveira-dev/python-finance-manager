# Finance Manager

A command-line personal finance management application developed in Python.

This project was created as a practical study of software development fundamentals, including Object-Oriented Programming (OOP), data persistence, modular architecture, data filtering, sorting, reporting, and JSON manipulation.

## Features

### Financial Records

* Add financial transactions
* Edit transactions
* Delete transactions
* Automatic date and time registration
* Income and expense tracking
* Categorized transactions

### Categories

#### Income Categories

* Salary
* Freelance
* Investments
* Others

#### Expense Categories

* Food
* Transportation
* Housing
* Health
* Leisure
* Internet
* Education
* Others

### Analysis and Organization

* List all transactions
* Filter by:

  * All transactions
  * Income
  * Expenses
  * Category
* Sort by:

  * Value
  * Date
  * Category
* Balance calculation
* Income summary
* Expense summary

### Reports

* Export complete financial report to a text file
* Report includes:

  * Total income
  * Total expenses
  * Current balance
  * Detailed transaction history

### Technical Features

* JSON persistence
* Object-Oriented Programming (OOP)
* Modular architecture
* Input validation
* Error handling for corrupted JSON files

---

## Technologies

* Python 3
* JSON
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
finance_manager/
│
├── main.py
├── movimentacoes.py
│
├── dados/
│   └── movimentacoes.json
│
├── models/
│   └── movimentacao.py
│
├── README.md
└── .gitignore
```

---

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd finance_manager
```

Run the application:

```bash
python main.py
```

---

## Learning Objectives

This project was built to practice:

* Classes and objects
* Constructors (`__init__`)
* Class methods
* Data serialization
* File handling
* Error handling
* Modularization
* Data filtering
* Data sorting
* Report generation
* Git and GitHub workflow

---

## Future Improvements

* Financial statistics dashboard
* Monthly reports
* Recurring transactions
* Budget management
* Savings goals
* Transaction IDs
* CSV export
* Graph generation
* Database integration
* Graphical user interface (GUI)

---

## Author

Patrick Barboza Oliveira