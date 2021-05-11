import openpyxl

ex = openpyxl.load_workbook('collegeDetails.xlsx')
colnum = 65
cell = chr(colnum)
rownum = 2
while (ex['student'][cell + str(rownum)].value != None):
    print(ex['student'][cell + str(rownum)].value, end=' ')
    colnum += 1
    cell = chr(colnum)

print()
ws = ex['professor']  # To set a current sheet in a workbook
print(ws['A2'].value)  # to access a cell in a worksheet
print(ws.cell(3, 1).value)  # to access a cell using rownumber and column number
