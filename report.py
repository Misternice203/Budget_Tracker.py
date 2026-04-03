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
