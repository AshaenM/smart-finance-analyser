def categorise(transaction):
    category = transaction["description"].lower()
    
    if "mcdonald" in category or "food" in category:
        return "Food"
    elif "coles" in category or "groceries" in category:
        return "Groceries"
    elif "salary" in category:
        return "Income"
    else:
        return "Other"