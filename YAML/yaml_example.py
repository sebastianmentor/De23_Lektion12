import yaml


with open('example.yaml', 'r', encoding='utf-8') as f:
    yaml_sträng = f.read()


data = yaml.safe_load(yaml_sträng)

for bok in data['böcker']:
    print(bok['titel'])
