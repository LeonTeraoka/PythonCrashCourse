import openpyxl
from pathlib import Path
wb = openpyxl.load_workbook("売上データ.xlsx")
Path("Copy").mkdir(exist_ok=True)
wb.save("Copy/売上データ_コピー.xlsx")
