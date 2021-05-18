def make_pizza(*toppings):
	"""注文されたピザの要約を出力する"""
	print("\n以下のトッピングのピザを作ります。")
	for topping in toppings:
		print(f"-{topping}")

make_pizza("ペパロニ")
make_pizza("マッシュルーム","ピーマン","エクストラチーズ")






#pizza = {
#	"crust": "レギュラー",
#	"toppings": ["マッシュルーム", "エクストラチーズ"],
#	}

#注文の要約
#print(f"あなたが注文したのは{pizza['crust']}生地のピザで、"
#	"トッピングは以下の注文の通りです。")

#for topping in pizza["toppings"]:
#	print(f"\t{topping}")
