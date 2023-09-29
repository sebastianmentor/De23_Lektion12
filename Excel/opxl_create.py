import openpyxl
import random
import names
import datetime
import radar
import animal_list

lista_med_djur = animal_list.animal_list()

# Create a Workbook
wb = openpyxl.Workbook()

# Get the active sheet (default sheet)
sheet = wb.active

# Change the sheet title
sheet.title = "Mina Djur!"


# Write some data to the sheet
#-------Rad 1---------------
sheet['A1'] = 'Namn'
sheet['B1'] = 'Ålder'
sheet['C1'] = 'Art'
sheet['D1'] = datetime.datetime.now()
#-------Rad 2---------------
sheet['A2'] = 'Hump'
sheet['B2'] = '12'
sheet['C2'] = 'Kamel'
sheet['D2'] = datetime.datetime.now()
#-------Rad 3---------------
sheet['A3'] = 'Kalle'
sheet['B3'] = '5'
sheet['C3'] = 'Anka'
sheet['D3'] = radar.random_datetime()
#-------Rad 4 till 100------
for i in range(4,101):
    sheet[f'A{i}'] = names.get_first_name()
    sheet[f'B{i}'] = random.randint(1,20)
    sheet[f'C{i}'] = random.choice(lista_med_djur)
    sheet[f'D{i}'] = radar.random_datetime()

# Save the workbook to a file
wb.save('example.xlsx')

print("Workbook saved successfully!")
