import openpyxl

wb = openpyxl.load_workbook("顧客マスタ.xlsx")
ws = wb["Sheet1"]

# 顧客マスタの全データリスト
customer_list = []

for row in ws.iter_rows(min_row=2):
	if row[0].value is None:
		break
	value_list = []
	for c in row:
		value_list.append(c.value)
	customer_list.append(value_list)

# 検索結果リスト
target_list = []

# 顧客の検索
for customer in customer_list:
	# 検索条件(顧客IDがKで始まるか)
	if customer[0].startswith("K"):
		target_list.append(customer)

# 確認
for target in target_list:
	print(target)
