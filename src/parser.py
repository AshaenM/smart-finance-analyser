import csv

def load_transactions(file_path):
    transactions = []
    
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            transactions.append(row)
            
    return transactions