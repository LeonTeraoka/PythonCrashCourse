movie_theater = "\n映画館へようこそ！"
movie_theater += "\n年齢はおいくつですか？"
movie_theater += "\n年齢："
age = int()

while age < 100:
	movie = input(movie_theater)
	age = int(movie)

	if age < 3:
		print("無料です。")
	elif age < 12:
		print("1000円です。")
	else:
		print("1500円です。")
		break