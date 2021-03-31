import openpyxl
wb = openpyxl.load_workbook("売上データ.xlsx")
print(wb.sheetnames)