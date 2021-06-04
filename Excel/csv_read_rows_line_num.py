import csv

f = open("4月売上.csv", encoding="cp932")
reader = csv.reader(f)
for row in reader:
	print(reader.line_num)
f.close()
