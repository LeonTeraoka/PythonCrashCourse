available_toppings = ["マッシュルーム", "オリーブ", "ピーマン", "エクストラチーズ", 
						"ペパロニ", "パイナップル", "エクストラチーズ"]

requested_toppings = ["マッシュルーム", "フライドポテト", "エクストラチーズ"]

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"トッピングに{requested_topping}を追加します。")		
	else:
		print(f"申し訳ありません、{requested_topping}はありません")

print("\nピザができました！")


#else:
#	print("プレーンピザでよろしいですか？")

#for requested_topping in requested_toppings:
#	if requested_topping == "ピーマン":
#		print("申し訳ありません。ピーマンは品切れです。")
#	else:
#		print(f"ピザに{requested_topping}を追加します。")

#if requested_topping != "アンチョビ":
#    print("アンチョビを注文してください！")
#if "マッシュルーム" in requested_topping:
#	print("マッシュルームを追加する。")
#elif "ペパロニ" in requested_topping:
#	print("ペパロニを追加する。")
#elif "エクストラチーズ" in requested_topping:
#	print("エクストラチーズを追加する。")

#print("\nピザができました！")
