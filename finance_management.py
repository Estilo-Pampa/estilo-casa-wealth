class FinanceManager:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_budget_status(self):
        total_expenses = self.get_total_expenses()
        return self.budget - total_expenses

class Expense:
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date
