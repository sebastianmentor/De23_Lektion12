import csv

filename = 'exempel.csv'

data = [
    {'Förnamn': 'John', 'Efternamn': 'Doe', 'Ålder': 30},
    {'Förnamn': 'Jane', 'Efternamn': 'Doe', 'Ålder': 25},
    {'Förnamn': 'Mike', 'Efternamn': 'Jordan', 'Ålder': 55},
]

# Definiera kolumnordningen
fieldnames = ['Förnamn', 'Efternamn', 'Ålder']

with open(filename, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Skriv header
    writer.writeheader()
    
    # Skriv data
    writer.writerows(data)

print(f"{filename} har skapats och data har skrivits till den!")
