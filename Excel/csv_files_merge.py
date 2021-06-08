import csv
from pathlib import Path

#「売上月別」フォルダー内CSVファイルの読み込み
rows = []
skip_num = 0
for file in Path("売上月別").glob(".csv"):
	f = open(file)
	reader = csv.reader(f)
	for row in reader:
		if reader.line_num <= skip_num:
			continue
		rows.append(row)
		f.close()
		skip_num = 3

# 書き込み
f = open("第1四半期売上.csv", mode="w", newline="")
writer = csv.writer(f)
for row in rows:
	writer.writerow(row)
f.close()
