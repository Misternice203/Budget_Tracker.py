class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_expenses(self):
        return [t for t in self.transactions if t.type == "expense"]
    
    def get_income(self):
        return [t for t in self.transactions if t.type == "income"]
