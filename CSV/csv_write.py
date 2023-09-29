import csv

filename = 'example.csv'
data = [
    ['Förnamn', 'Efternamn', 'Ålder'],  # Header
    ['John', 'Doe', 30],  # Rad 1
    ['Jane', 'Doe', 25],  # Rad 2
]

with open(filename, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    
    for row in data:
        writer.writerow(row)

print(f"{filename} skapad framgångsrikt!")
