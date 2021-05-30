import openpyxl

wb = openpyxl.load_workbook("売上データ_第1四半期.xlsx")
ws = wb.worksheets[-1]

to_top = 1 - len(wb.worksheets)
wb.move_sheet(ws, offset=to_top)
wb.save("売上データ_第1四半期.xlsx")
