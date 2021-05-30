import openpyxl

wb = openpyxl.load_workbook("売上データ_シート挿入.xlsx")
ws = wb.worksheets[0]

wb.remove(ws)
wb.save("売上データ_シート挿入.xlsx")
