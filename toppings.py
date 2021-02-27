requested_topping = ["マッシュルーム", "エクストラチーズ"]

#if requested_topping != "アンチョビ":
#    print("アンチョビを注文してください！")
if "マッシュルーム" in requested_topping:
	print("マッシュルームを追加する。")
elif "ペパロニ" in requested_topping:
	print("ペパロニを追加する。")
elif "エクストラチーズ" in requested_topping:
	print("エクストラチーズを追加する。")

print("\nピザができました！")
