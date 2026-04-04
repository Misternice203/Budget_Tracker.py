### Budget_Tracker.py
A simple command-line budget tracker application built using Python. This project allows users to record income and expenses, view transaction history, and save data using persistent JSON storage.

## This project is actively being improved as part of my backend developer journey.

---

## Code Analysis Report

### Strengths
- **Clean separation of concerns** — each class (`Transaction`, `Budget`, `Report`, `Storage`, `App`) has a single, well-defined responsibility. This makes the code easy to read and extend.
- **Persistent storage** — JSON serialization/deserialization is implemented cleanly in `Storage`, and the `to_dict()` pattern on `Transaction` is the right approach.
- **Input validation** — date format and numeric amount inputs are guarded with `try/except` loops that retry on bad input.
- **OOP fundamentals** — classes are instantiated correctly; `Report` takes a `Budget` reference rather than duplicating data, which is good design.

### Issues Fixed in This Update
1. **`percent_spent()` return-type inconsistency** — previously returned the string `"N/A"` when income was zero, but `generate_summary()` returned `0` (an int). Both paths now consistently return a `float`.
2. **Duplicate code in `create_transaction()`** — income and expense branches shared identical date/amount/save logic, now collapsed into a single shared path.
3. **No validation for zero or negative amounts** — a new `get_valid_amount()` helper rejects any value ≤ 0.
4. **Unformatted transaction list** — the transaction view now renders a clean aligned table instead of a plain string dump.
5. **Unreachable `else` branch in `run()`** — the `else: print("Invalid input...")` after the `elif choice == 6` block could never be reached; the menu now uses `range(1, 9)` consistently.

---

## Features
* Add income transactions
* Add expense transactions
* View current balance
* View all transactions with aligned table formatting
* Filter transactions by type (income only / expense only / all)
* Delete a transaction by number
* Report summary (totals, balance, percent spent)
* Monthly summary broken down by year-month
* Persistent storage using JSON
* Simple and user-friendly CLI menu

## Concepts
This project demonstrates:
* Object-Oriented Programming (OOP)
* Class design and responsibility separation
* File handling with JSON
* Data persistence
* Input validation and error handling
* CLI app structure

## Project Structure
* `Transaction` → Represents a single income or expense entry
* `Budget` → Stores and manages the list of transactions
* `Report` → Calculates totals, balance, percent spent, and monthly breakdown
* `Storage` → Handles saving/loading data to `data.json`
* `App` → Controls user interaction and program flow

## How to Run
* Make sure Python 3.10+ is installed
* Clone the repository
* Run `python main.py`

## Menu Options
```
1. Add Income
2. Add Expense
3. View Balance
4. View Transactions   (filter by income / expense / all)
5. Report Summary
6. Monthly Summary
7. Delete Transaction
8. Exit Program
```

## Upgrade Ideas (no external APIs required)
1. **Edit transactions** — allow selecting a transaction by number and changing any of its fields (date, description, category, amount).
2. **CSV export** — add a menu option to write all transactions to a `.csv` file for use in spreadsheet applications.
3. **Budget limits by category** — let the user set a monthly spending cap per category and warn when approaching or exceeding it.
4. **Search / filter by date range** — prompt for a start and end date and show only transactions that fall within that window.
5. **Recurring transactions** — mark a transaction as recurring (weekly / monthly) and auto-generate future entries on start-up.

## Notes
This project is part of my journey toward becoming a backend developer. More features and improvements will be added over time.
