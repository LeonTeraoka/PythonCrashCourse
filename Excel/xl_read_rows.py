import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")
ws = wb["4月売上"]

for row in ws.iter_rows(min_row=4):
	print(row)
