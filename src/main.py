from parser import load_transactions
from categoriser import categorise
from analyser import calculate_summary, category_breakdown

transactions = load_transactions("../data/sample_transactions.csv")
for t in transactions:
    t["category"] = categorise(t)
    
print("Welcome to your smart finance analyser! Please select an option:")


while (True):
    print("\nSelect an option:")
    print("1. View Summary")
    print("2. View Category Breakdown")
    print("Type 'exit' to quit")

    option_wanted = input("> ")
    
    if option_wanted == "1":
        income, expenses = calculate_summary(transactions)
        print("\n--- Summary: ---")
        print(f"Income: ${income:.2f}, Expenses: ${expenses:.2f}")
        print("----------------")
    elif option_wanted == "2":
        cat_summary = category_breakdown(transactions)
        print("\n--- Category Breakdown: ---")
        for cat, value in cat_summary.items():
            print(f"- {cat}: ${value}")
        print("---------------------------")
    elif option_wanted in ["end", "exit"]:
        print("----------------")
        print("Goodbye!")
        print("----------------")
        break
    else:
        print("----------------")
        print("Invalid option. Please try again.")
        print("----------------")