def categorise(transaction):
    '''Categorises each transaction dictionary with a new key containing the relevant category'''
    
    category = transaction["description"].lower()
    
    if "mcdonald" in category or "food" in category:
        return "Food"
    elif "coles" in category or "groceries" in category:
        return "Groceries"
    elif "salary" in category:
        return "Income"
    else:
        return "Other"