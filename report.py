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
            return 0.0
        return self.total_expenses() / self.total_income() * 100

    def monthly_summary(self):
        monthly = {}
        for t in self.budget.transactions:
            if len(t.date) < 7:
                continue
            month_key = t.date[:7]
            if month_key not in monthly:
                monthly[month_key] = {"income": 0.0, "expenses": 0.0}
            if t.transaction_type == "income":
                monthly[month_key]["income"] += t.amount
            else:
                monthly[month_key]["expenses"] += t.amount
        for month_key in monthly:
            monthly[month_key]["balance"] = (
                monthly[month_key]["income"] - monthly[month_key]["expenses"]
            )
        return monthly

    def generate_summary(self):
       income = self.total_income()
       expenses = self.total_expenses()

       return {
           "income": income,
           "expenses": expenses,
           "balance": income - expenses,
           "percent_spent": (expenses / income * 100) if income else 0
       }
