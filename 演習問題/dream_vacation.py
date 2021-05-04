vacation = {}

active = True

while active:
	name = input("\nあなたのお名前は？")
	dream = input("世界中どこでも好きなところに行けるとしたら、どこに行きたいですか？")

	vacation[name] = dream

	repeat = input("誰か他に回答してくれる人はいますか？(yes/no)")
	if repeat == "no":
		active = False

print("\n---投票終了---")
for name, dream in vacation.items():
	print(f"{name}さんが行きたいのは{dream}")
