sandwich_orders = ["ハム", "ツナ", "イチゴ", "パストラミ", "パストラミ", "パストラミ"]
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"注文リスト：{sandwich}")
	finished_sandwiches.append(sandwich)

print(" ")

while "パストラミ" in finished_sandwiches:
	finished_sandwiches.remove("パストラミ")
	print("パストラミは品切れです。")

print("\n下記、注文されたサンドウィッチです。")
for finished_sandwiches in finished_sandwiches:
	print(f"{finished_sandwiches}サンドができました。")
