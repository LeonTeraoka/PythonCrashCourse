import openpyxl

wb = openpyxl.load_workbook("顧客マスタ_除外あり.xlsx")
ws = wb["Sheet1"]

# 顧客マスタの全データリスト
customer_list = []

# 顧客マスタの全行を1行ずつ読み込む
for row in ws.iter_rows(min_row=2):
	# 顧客 IDのセルが空になったら終了
	if row[0].value is None:
		break
	# コード追加:
	# 除外の列に何か入力されている場合は読み飛ばす
	if row[6].value is not None:
		continue
	value_list = []
	for c in row:
		value_list.append(c.value)
	customer_list.append(value_list)

# 確認
for customer in customer_list:
	print(customer)
