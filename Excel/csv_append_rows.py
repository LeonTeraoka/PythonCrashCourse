import csv

add_list = [
["2020/5/15", "三和商事　株式会社", "商品 B", "3800", "10", "38000",],
["2020/5/20", "三和商事　株式会社", "商品 B", "3800", "30" ,"114000"],
["2020/5/26", "サン企画　有限会社", "商品 A", "7200", "5", "36000"],
["2020/5/29", "三和商事　株式会社", "商品 B", "3800", "15", "57000"],
]

f = open("5月売上_練習.csv", mode="a", newline="", encoding="cp932")
writer = csv.writer(f)
for data in add_list:
	writer.writerow(data)
f.close()
