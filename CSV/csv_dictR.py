import csv

filename = 'exempel.csv'

with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
