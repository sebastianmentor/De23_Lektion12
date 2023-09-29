import yaml

# Skapa en dictionary som representerar information om en bokhandel
bokhandel = {
    "namn": "Fantasy Bokhandel",
    "adress": "Sagovägen 123, 12345 Stockholm",
    "öppettider": {
        "mån-fre": "09:00-18:00",
        "lör": "10:00-15:00",
        "sön": "Stängt"
    },
    "böcker": [
        {"titel": "Hobbiten", "författare": "J.R.R. Tolkien", "genre": "Fantasy", "pris": 120},
        {"titel": "Harry Potter och De Vises Sten", "författare": "J.K. Rowling", "genre": "Fantasy", "pris": 150}
    ],
    "anställda": [
        {"namn": "Anna Svensson", "ålder": 30, "roll": "Försäljare"},
        {"namn": "Erik Karlsson", "ålder": 25, "roll": "Lagerarbetare"}
    ]
}

# Konvertera Python-dictionary till YAML-sträng med yaml.dump()
yaml_sträng = yaml.dump(bokhandel, default_flow_style=False, allow_unicode=True)

# Skriv ut den konverterade YAML-strängen
print(yaml_sträng)


with open('example_dump.yaml', 'w', encoding='utf-8') as f:
    f.write(yaml_sträng)