import csv

def load_transactions(file_path):
    '''Reads the CSV file and returns a list of dictionaries for each record'''
    
    transactions = []
    
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            transactions.append(row)
           
    return transactions