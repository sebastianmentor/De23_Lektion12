import csv

filename = 'example.csv'

with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Läs header
    header = next(reader)
    print(f'Header: {header}')
    
    # Läs resten av raderna
    for row in reader:
        print(row)
