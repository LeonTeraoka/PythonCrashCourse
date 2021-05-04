topping = "\nトッピングは如何にしますか？"
topping += "\n選び終えたら「終了」と入力してください"
topping += "\n追加するトッピング："
order = ""
active = True
while active:
	order = input(topping)
	if order == "終了":
		print("\n以上、ご利用ありがとうございます。")
		break
	else:
		print(f"\n{order}が追加されました。")


#while order != "終了":
#	order = input(topping)
