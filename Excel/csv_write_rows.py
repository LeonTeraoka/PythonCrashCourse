import csv

data_list = [
["売上データ", "", "", "", "", "",],
["", "", "", "", "" ,""],
["売上日", "顧客名称", "商品名", "単価", "数量", "計"],
["2020/5/7", "サン企画　有限会社", "商品 B", "3800", "10", "38000"],
["2020/5/8", "三和商事　株式会社", "商品 A", "7200", "7", "50400"],
["2020/5/11", "株式会社　鈴木商店", "商品 C", "1200", "100", "120000"]
]

f = open("5月売上.csv", mode="w", newline="", encoding="cp932")
writer = csv.writer(f)
for data in data_list:
	writer.writerow(data)
f.close()
