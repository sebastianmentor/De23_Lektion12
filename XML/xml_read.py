import xml.etree.ElementTree as ET

# Ladda XML-fil
tree = ET.parse('exempel.xml')
root = tree.getroot()

# Iterera över element i XML-filen
for person in root.findall('person'):
    age = person.get('ålder')
    first_name = person.find('förnamn').text
    last_name = person.find('efternamn').text
    
    print(f'{first_name} {last_name} är {age} år gammal.')
