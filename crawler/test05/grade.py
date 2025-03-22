import random, openpyxl

# create a workbook
wb = openpyxl.Workbook()

# create a sheet
sheet = wb.active
sheet.title = 'Grade'

# create a header
titles = ['Name', 'Chinese', 'Math', 'English']
for col_index, title in enumerate(titles):
    sheet.cell(1, col_index + 1, title)

names = ['Alice', 'Bob', 'Cindy', 'David', 'Eva']
for row_index, name in enumerate(names):
    sheet.cell(row_index + 2, 1, name)
    for col_index in range(2, 5):
        sheet.cell(row_index + 2, col_index, random.randint(60, 100))

# save the workbook
wb.save('grade.xlsx')
