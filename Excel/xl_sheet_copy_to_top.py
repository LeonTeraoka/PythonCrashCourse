import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")
ws = wb["4月売上"]

ws_copy = wb.copy_worksheet(ws)
ws_copy.title = "4月作業用"

# 末尾に作成されたシートのコピーを先頭に移動
wb.move_sheet(ws_copy, offset=-3)

wb.save("売上データ_作業用.xlsx")
