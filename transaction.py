class Transaction:
    def __init__(self, date, description, category, transaction_type, amount):
        self.date = date
        self.description = description
        self.category = category
        self.transaction_type = transaction_type
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "description": self.description,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "amount": self.amount
        }
