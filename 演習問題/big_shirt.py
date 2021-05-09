def make_shirt(text,size="L"):
	"""Tシャツのサイズとプリントを出力する。"""
	print(f"サイズは{size}で、柄は{text.title()}です。")

make_shirt(size="L", text="i love python")

make_shirt(size="M", text="i love python")