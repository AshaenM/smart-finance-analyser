def calculate_summary(transactions):
    income = 0
    expenses = 0
    
    for t in transactions:
        if float(t["amount"]) > 0:
            income += float(t.get("amount"))
        else:
            expenses += float(t.get("amount"))
    
    return income, expenses