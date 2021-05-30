import openpyxl

wb = openpyxl.load_workbook("売上データ_シート挿入.xlsx")
ws = wb["Sheet1"]
ws.title = "第1四半期"

wb.save("売上データ_第1四半期.xlsx")
