pizza = {
	"crust": "レギュラー",
	"toppings": ["マッシュルーム", "エクストラチーズ"],
	}

#注文の要約
print(f"あなたが注文したのは{pizza['crust']}生地のピザで、"
	"トッピングは以下の注文の通りです。")

for topping in pizza["toppings"]:
	print(f"\t{topping}")
