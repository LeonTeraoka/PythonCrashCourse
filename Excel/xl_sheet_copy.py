import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")
ws = wb["4月売上"]

ws_copy = wb.copy_worksheet(ws)
# シート名変更
ws_copy.title = "4月作業用"

wb.save("売上データ_作業用.xlsx")
