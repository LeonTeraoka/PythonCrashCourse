import openpyxl
wb = openpyxl.load_workbook("売上データ.xlsx")
wb.save("売上データ_コピー.xlsx")
