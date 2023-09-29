import openpyxl

# Open the saved Workbook
wb = openpyxl.load_workbook('example.xlsx')

# Get the active sheet
sheet = wb.active

# Read data from the sheet
for row in sheet.iter_rows(min_row=1, max_row=100, min_col=1, max_col=4, values_only=True):
    print(row)

wb.close()
