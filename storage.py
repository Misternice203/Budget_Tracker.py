from transaction import Transaction

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
