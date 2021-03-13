current_users = ["admin", "muffin", "muffn", "milk", "mint"]
new_users = ["noname", "mofin", "muffin", "muffn", "bon"]

for new_users in new_users:
	if new_users in current_users:
		print("使用できません。")
	else:
		print("使用できます。")




#user_name = []

#if user_name:
#	for user_name in user_name:
#		print(f"こんにちは{user_name.title()}")

#if user_name in user_name == "admin":
#	print("こんにちはadmin、状況のレポートを見ますか？")
#else:
#	print("ユーザー募集中です！")
#	print("こんにちはJaden、またログインしてくれてありがとう。")