import json  # Importera json-modulen i Python

# Skapa en lista med böcker, där varje bok är ett dictionary.
böcker = [
    {"titel": "Moby Dick", "författare": "Herman Melville", "år": 1851},
    {"titel": "Krig och fred", "författare": "Leo Tolstoy", "år": 1869},
    {"titel": "Stolthet och fördom", "författare": "Jane Austen", "år": 1813}
]

# Konvertera Python-listan (med dictionaries) till en JSON-sträng.
json_sträng = json.dumps(böcker, indent=4)  # 'indent=4' gör JSON-strängen lättläst.
print(json_sträng)  # Skriv ut den formaterade JSON-strängen.

# Antag att vi får JSON-data från en fil eller en webbserver, och vill konvertera den till Python-objekt.
mottagen_json = '''
[
    {"titel": "Moby Dick", "författare": "Herman Melville", "år": 1851},
    {"titel": "Krig och fred", "författare": "Leo Tolstoy", "år": 1869},
    {"titel": "Stolthet och fördom", "författare": "Jane Austen", "år": 1813}
]
'''

# Parsa JSON-strängen till en Python-lista (med dictionaries).
konverterade_böcker = json.loads(mottagen_json)

# Skriv ut titeln på varje bok i den konverterade listan.
for bok in konverterade_böcker:
    print(bok['titel'])
