
class Transaction:
    def __init__(self, date, description, category, transaction_type, amount):
        self.amount = amount
        self.category = category
        self.date = date
        self.type = transaction_type
        self.description = description

    def to_dict(self):
        return {
            "transaction_type": self.type,
            "category": self.category,
            "description": self.description,
            "date": self.date,
            "amount": self.amount
        }


class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_expenses(self):
        return [t for t in self.transactions if t.type == "expense"]
    
    def get_income(self):
        return [t for t in self.transactions if t.type == "income"]
    

class Report:
    def __init__(self, budget):
        self.budget = budget

    def total_expenses(self):
        return sum(t.amount for t in self.budget.get_expenses())

    def total_income(self):
        return sum(t.amount for t in self.budget.get_income())
    
    def balance(self):
        return self.total_income() - self.total_expenses()
    
    def percent_spent(self):
        if self.total_income() == 0:
            return "N/A"
        else:
            return self.total_expenses() / self.total_income() * 100

    def generate_summary(self):
       income = self.total_income()
       expenses = self.total_expenses()

       return {
           "income": income,
           "expenses": expenses,
           "balance": income - expenses,
           "percent_spent": (expenses / income * 100) if income else 0
       }


    def display_summary(self, summary):
        print(f'''
                      ========== Financial Report ==========
                      Total Income: 💲{summary["income"]}
                      Total Expenses: 💲{summary["expenses"]}
                      Balance: 💲{summary["balance"]}
                      Percent Spent: {summary["percent_spent"]:.2f}%
                ''')


import json

class Storage:
    def save(self, transactions):
        data = [t.to_dict() for t in transactions]
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                return [Transaction(**t)for t in data]
        except FileNotFoundError:
            return []
        
class App:
    def __init__(self):
        self.budget = Budget()
        self.report = Report(self.budget)
        self.storage = Storage()
        loaded_transactions = self.storage.load()
        self.budget.transactions = loaded_transactions

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
            
            choice = int(input("\n1. Add Income\n2. Add expense\n3. View Balance\n4. View Transactions\n5. Report Summary\n6. Exit Program\n"))

            if choice < 1 or choice > 6:
                print("Invalid input. Please select a option from the menu.")
                continue
            elif choice == 1:
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
                "Have a Great Day")
                break

App().run()
