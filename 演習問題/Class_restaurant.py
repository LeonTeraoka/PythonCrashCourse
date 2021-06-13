class Restaurant:
	"""レストランをモデル化"""

	def __init__(self, name, menu):
		"""レストラン名と料理の種類の属性を格納"""
		self.name = name
		self.menu = menu

	def describe_restaurant(name):
		"""レストラン名と料理の種類の詳細"""
		print(f"{self.name}レストラン名")

	def opent_restaurant(name):
		"""レストランの開店名と料理の命令を実行"""
		print(f"{self.menu}料理の種類")

restaurant = Restaurant("松屋", "牛丼")

print(f"レストラン名：{restaurant.name}")
print(f"料理の種類：{restaurant.menu}")
