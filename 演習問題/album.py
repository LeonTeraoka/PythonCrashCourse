def make_album(artist, title,):
	"""アルバム情報を辞書で返す"""
	album = {}

	making_album = True

	while making_album:
		artist = input("アーティスト:")
		title = input("タイトル:")
		album[artist] = title

		repeat = input("(yes/no)")
		if repeat == 'no':
			making_album = False

musician = make_album('kawakami youhei', 'run away',)
print(musician)
