import openpyxl

wb = openpyxl.load_workbook("売上データ_第1四半期.xlsx")
ws = wb.worksheets[-1]

wb.move_sheet(ws, offset=-3)
wb.save("売上データ _第1四半期.xlsx")
