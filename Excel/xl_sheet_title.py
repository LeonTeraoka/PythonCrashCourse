import openpyxl
wb = openpyxl.load_workbook("売上データ.xlsx")
ws = wb["4月売上"]
print(ws.title)
ws2 = wb.worksheets[1]
print(ws2.title)
