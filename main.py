from budget import Budget
from report import Report
from storage import Storage
from transaction import Transaction


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
                      Total Income: 💲{summary["income"]}
                      Total Expenses: 💲{summary["expenses"]}
                      Balance: 💲{summary["balance"]}
                      Percent Spent: {summary["percent_spent"]:.2f}%
                ''')

    def create_transaction(self, transaction_type):
        if transaction_type == "income":
            print("\nYou selected to Add Income!\n")
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter A Short Description (Job, W2, 1099): ")
            category = input("Enter A Category (Deposit, Check, Side Hustle): ")
            amount = float(input("Enter The Amount: "))

            t = Transaction(date, description, category, "income", amount)
            self.budget.add_transaction(t)
            self.storage.save(self.budget.transactions)

        else:
            print("\nYou selected To Add A Expense!\n")
            date = input("Enter The Date (YYYY-MM-DD): ")
            description = input("Enter A Short Desctription (fast-food, Movie, Clothes): ")
            category = input("Enter A Category (Bill, Lunch, Groceries): ")
            amount = float(input("Enter The Amount: "))

            t = Transaction(date, description, category, "expense", amount)
            self.budget.add_transaction(t)
            self.storage.save(self.budget.transactions)


    def run(self):
        while True:
            try:
                choice = int(input("\n1. Add Income\n2. Add expense\n3. View Balance\n4. View Transactions\n5. Report Summary\n6. Exit Program\n"))
            except ValueError:
                print("Invalid input. Please enter a option from the menu.")
                continue

            if choice == 1:
                self.create_transaction("income")

            elif choice == 2:
                self.create_transaction("expense")
            
            elif choice == 3:
                print("Balance:", self.report.balance())

            elif choice == 4:
                print("You selected to View your Transactions.")
                for t in self.budget.transactions:
                    print(f"\n{t.date} | {t.description} | {t.category} | {t.type} | {t.amount}\n")

            elif choice == 5:
                summary = self.report.generate_summary()
                self.display_summary(summary)


            elif choice == 6:
                print("You Selected to End The Program.\n All of Your Transactions Have Been Saved!" \
                " Have a Great Day!")
                break
            else:
                print("Invalid input. Please enter a option from the menu.")

App().run()
