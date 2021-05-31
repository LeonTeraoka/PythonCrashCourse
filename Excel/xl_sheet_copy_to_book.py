import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")
ws = wb["4月売上"]

for ws in wb.worksheets:
	if ws.title != "4月売上":
		wb.remove(ws)

wb.save("売上データ_4月のみ.xlsx")
