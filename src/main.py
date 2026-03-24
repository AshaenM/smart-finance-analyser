from parser import load_transactions

transactions = load_transactions("../data/sample_transactions.csv")

for t in transactions:
    print(t)