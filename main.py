from budget import Budget
from report import Report
from storage import Storage
from transaction import Transaction
from datetime import datetime


class App:
    def __init__(self):
        self.budget = Budget()
        self.report = Report(self.budget)
        self.storage = Storage()
        loaded_transactions = self.storage.load()
        self.budget.transactions = loaded_transactions

    def display_summary(self, summary):
        print(f'''
                      ========== Financial Report ==========
                      Total Income: 💲{summary["income"]:.2f}
                      Total Expenses: 💲{summary["expenses"]:.2f}
                      Balance: 💲{summary["balance"]:.2f}
                      Percent Spent: {summary["percent_spent"]:.2f}%
                ''')

    def get_valid_date(self, prompt):
        while True:
            date_input = input(prompt).strip()
            try:
                datetime.strptime(date_input, "%Y-%m-%d")
                return date_input
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def get_valid_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    return amount
            except ValueError:
                print("Invalid response. Please enter a number.")

    def create_transaction(self, transaction_type):
        if transaction_type == "income":
            print("\nYou selected to Add Income!\n")
            desc_hint = "(Job, W2, 1099)"
            cat_hint = "(Deposit, Check, Side Hustle)"
        else:
            print("\nYou selected to Add An Expense!\n")
            desc_hint = "(Fast-food, Movie, Clothes)"
            cat_hint = "(Bill, Lunch, Groceries)"

        date = self.get_valid_date("Enter the date (YYYY-MM-DD): ")
        description = input(f"Enter A Short Description {desc_hint}: ")
        category = input(f"Enter A Category {cat_hint}: ")
        amount = self.get_valid_amount("Enter The Amount: ")

        t = Transaction(date, description, category, transaction_type, amount)
        self.budget.add_transaction(t)
        self.storage.save(self.budget.transactions)
        print("Transaction saved successfully!")

    def view_transactions(self, transactions):
        if not transactions:
            print("No transactions to display.")
            return
        print(f"\n{'#':<4} {'Date':<12} {'Description':<25} {'Category':<20} {'Type':<10} {'Amount':>10}")
        print("-" * 84)
        for i, t in enumerate(transactions, start=1):
            print(f"{i:<4} {t.date:<12} {t.description:<25} {t.category:<20} {t.transaction_type:<10} 💲{t.amount:>9.2f}")
        print("-" * 84)

    def delete_transaction(self):
        if not self.budget.transactions:
            print("No transactions to delete.")
            return
        self.view_transactions(self.budget.transactions)
        while True:
            try:
                index = int(input("\nEnter the row # of the transaction to delete, or 0 to cancel: "))
                if index == 0:
                    print("Delete cancelled.")
                    return
                if 1 <= index <= len(self.budget.transactions):
                    removed = self.budget.transactions.pop(index - 1)
                    self.storage.save(self.budget.transactions)
                    print(f"Deleted: {removed.date} | {removed.description} | 💲{removed.amount:.2f}")
                    return
                else:
                    print(f"Please enter a number between 1 and {len(self.budget.transactions)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def view_filtered_transactions(self):
        print("\n1. Income Only\n2. Expenses Only\n3. All Transactions")
        while True:
            try:
                choice = int(input("Select filter: "))
                if choice == 1:
                    self.view_transactions(self.budget.get_income())
                elif choice == 2:
                    self.view_transactions(self.budget.get_expenses())
                elif choice == 3:
                    self.view_transactions(self.budget.transactions)
                else:
                    print("Please choose 1, 2, or 3.")
                    continue
                return
            except ValueError:
                print("Invalid input.")

    def view_monthly_summary(self):
        monthly = self.report.monthly_summary()
        if not monthly:
            print("No transactions recorded yet.")
            return
        print(f"\n{'Month':<10} {'Income':>12} {'Expenses':>12} {'Balance':>12}")
        print("-" * 50)
        for month in sorted(monthly):
            m = monthly[month]
            print(f"{month:<10} 💲{m['income']:>10.2f} 💲{m['expenses']:>10.2f} 💲{m['balance']:>10.2f}")
        print("-" * 50)

    def run(self):
        while True:
            try:
                choice = int(input(
                    "\n1. Add Income\n"
                    "2. Add Expense\n"
                    "3. View Balance\n"
                    "4. View Transactions\n"
                    "5. Report Summary\n"
                    "6. Monthly Summary\n"
                    "7. Delete Transaction\n"
                    "8. Exit Program\n"
                ))
                if choice not in range(1, 9):
                    print("Please choose an option from the menu.")
                    continue
            except ValueError:
                print("Invalid input. Please enter an option from the menu.")
                continue

            if choice == 1:
                self.create_transaction("income")

            elif choice == 2:
                self.create_transaction("expense")

            elif choice == 3:
                print(f"Balance: 💲{self.report.balance():.2f}")

            elif choice == 4:
                self.view_filtered_transactions()

            elif choice == 5:
                summary = self.report.generate_summary()
                self.display_summary(summary)

            elif choice == 6:
                self.view_monthly_summary()

            elif choice == 7:
                self.delete_transaction()

            elif choice == 8:
                print("You Selected to End The Program.\nAll of Your Transactions Have Been Saved! Have a Great Day!")
                break


App().run()
