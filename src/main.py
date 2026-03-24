from parser import load_transactions
from categoriser import categorise
from analyser import calculate_summary

transactions = load_transactions("../data/sample_transactions.csv")

income, expenses = calculate_summary(transactions)

print(f"Income: {income}")
print(f"Expenses: {expenses}")