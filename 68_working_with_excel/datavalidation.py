import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment,Color

wb = openpyxl.load_workbook(sys.argv[1])

if 'comparison' in wb.sheetnames:
    del wb['comparison']

wb.create_sheet('comparison')
maxrow = wb['source'].max_row
maxcol = wb['source'].max_column

for c in range(1,maxcol + 1):
    wb['comparison'].cell(1,c).value = wb['source'].cell(1,c).value
    wb['comparison'].cell(1,c).font = Font(bold = True)

for r in range(2, maxrow + 1):
    for c in range(1, maxcol + 1):
        if wb['source'].cell(r, c).value == wb['target'].cell(r, c).value:
            wb['comparison'].cell(r, c).value = "True"
            wb['comparison'].cell(r, c).font = Font(bold=True, color = '0000FF')
            wb['comparison'].cell(r, c).fill = PatternFill(fill_type = 'solid', start_color = '00FF00', end_color = 'FFBD00')
        else:
            wb['comparison'].cell(r, c).value = '\''+str(wb['source'].cell(r, c).value)+'\',\''+str(wb['target'].cell(r, c).value)+'\''
            wb['comparison'].cell(r, c).font = Font(bold=True, color = '0000FF')
            wb['comparison'].cell(r, c).fill = PatternFill(fill_type = 'solid', start_color = 'FF0000', end_color = 'FFBD00')

print('Data successfully validated')
wb.save(sys.argv[1])
