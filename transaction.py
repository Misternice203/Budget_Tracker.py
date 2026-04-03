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
