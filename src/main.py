from parser import load_transactions
from categoriser import categorise

transactions = load_transactions("../data/sample_transactions.csv")

for t in transactions:
    t["category"] = categorise(t)
    print(t)