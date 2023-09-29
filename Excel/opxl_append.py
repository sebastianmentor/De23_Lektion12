import openpyxl
import random
import names
import radar
from animal_list import animal_list

lista_med_djur = animal_list()
# Load an existing workbook
filename = 'example.xlsx'
wb = openpyxl.load_workbook(filename)

# Select the active sheet
sheet = wb.active

# Append new rows of data to the sheet
new_data = []

for _ in range(100):
    new_data.append([
        names.get_first_name(),
        random.randint(1,20),
        random.choice(lista_med_djur),
        radar.random_datetime()
    ])

for row in new_data:
    sheet.append(row)

# Save the workbook back to the file
wb.save(filename)
print(f"Data appended successfully to {filename}")

