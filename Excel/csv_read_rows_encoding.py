import csv

f = open("4月売上.csv", encoding="utf-8")
reader = csv.reader(f)
for row in reader:
	print(row)
f.close()
