import csv

# ヘッダー行数
header_num = 3

f = open("4月売上.csv", encoding="cp932")
reader = csv.reader(f)
for row in reader:
	if reader.line_num <= header_num:
		continue
	print(row)
f.close()