def make_album(artist, title, songs=None):
	"""アルバム情報を辞書で返す"""
	album = {'artistname': artist, 'titlename': title}
	if songs:
		album["songs"] = songs
	return album

musician = make_album('kawakami youhei', 'run away', songs=4)
print(musician)
