from parser import load_transactions
from categoriser import categorise
from analyser import calculate_summary, category_breakdown

transactions = load_transactions("../data/sample_transactions.csv")

for t in transactions:
    t["category"] = categorise(t)

income, expenses = calculate_summary(transactions)
print(f"Income: {income}, Expenses: {expenses}")

cat_summary = category_breakdown(transactions)
print("Category breakdown:", cat_summary)