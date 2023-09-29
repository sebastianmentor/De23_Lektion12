import yaml

with open('example2.yaml', 'r', encoding='utf-8') as f:
    yaml_sträng = f.read()

data = yaml.safe_load(yaml_sträng)

# Skriv ut detaljer om bokhandeln
print("Bokhandel: ", data['bokhandel']['namn'])
print("Adress: ", data['bokhandel']['adress'])
print("Öppettider: ", data['bokhandel']['öppettider']['mån-fre'])

# Lista alla böcker och deras detaljer
print("\nBöcker:")
for bok in data['bokhandel']['böcker']:
    print(f"{bok['titel']} av {bok['författare']}, Genre: {bok['genre']}, Pris: {bok['pris']}kr")

# Lista alla anställda och deras detaljer
print("\nAnställda:")
for anställd in data['bokhandel']['anställda']:
    print(f"{anställd['namn']}, Ålder: {anställd['ålder']}, Roll: {anställd['roll']}")
