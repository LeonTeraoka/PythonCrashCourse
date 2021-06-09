import csv
import openpyxl
from pathlib import Path
import datetime

# 元のブックを開く
wb = openpyxl.load_workbook("売上データ.xlsx", data_only=True)

# CSVファイル保存先のフォルダー
for sheet in wb.worksheets:
	# CSVファイルのパスを作成
	file = "売上データ /" + sheet.title + ".csv"
	# 書き込みモードでCSVファイルを開く
	f = open(file, mode="w", newline="")
	writer = csv.writer(f)
	# シートのデータをCSVファイルに書き込む
	for row in sheet:
		# 1行分のデータを入れるリスト
		values = []
		for cell in row:
			if isinstance(cell.value, datetime.datetime):
				# 日付のデータは書式を指定して文字列にする
				values.append(cell.value.strftime("%Y/%m/%d"))
			else:
				values.append(cell.value)
		writer.writerow(values)
	f.close()
