def build_profile(first, last, **user_info):
	"""ユーザーの全情報を格納した辞書を作成"""
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info

user_profile = build_profile("muffin", "men",
							location="Japon",
							field="CS")
print(user_profile)
