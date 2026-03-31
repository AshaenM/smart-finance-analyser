def calculate_summary(transactions):
    '''Calculates the total income and expense and returns them as 2 separate float variables'''
    
    income = 0
    expenses = 0
    
    for t in transactions:
        if float(t["amount"]) > 0:
            income += float(t.get("amount"))
        else:
            expenses += float(t.get("amount"))
   
    return income, expenses

def category_breakdown(transactions):
    '''Sorts each expense into the relevant category and returns a dictionary containing every category with the total sum of expenses'''
    
    breakdown = {}

    for t in transactions:
        cat = t.get("category", "Other")
        amount = float(t["amount"])

        if amount < 0:
            breakdown[cat] = breakdown.get(cat, 0) + abs(amount)

    return breakdown