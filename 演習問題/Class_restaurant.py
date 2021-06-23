class Restaurant:
	"""レストランをモデル化"""

	def __init__(self, name, menu):
		"""レストラン名と料理の種類の属性を格納"""
		self.name = name
		self.menu = menu
		self.number_served = 0

	def describe_restaurant(name):
		"""レストラン名と料理の種類の詳細"""
		print(f"{self.name}レストラン名")

	def opent_restaurant(name):
		"""レストランの開店名と料理の命令を実行"""
		print(f"{self.menu}料理の種類")

	def read_served(self):
		print(f"{self.number_served}品提供されました。")

	def set_number_served(self, served):
		if served >= self.number_served:
			self.number_served = served
		else:
			print("走行距離は減らせません！")

first_restaurant = Restaurant("松屋", "牛丼")
second_restaurant = Restaurant("CoCo壱", "カレー")
third_restaurant = Restaurant("サイゼ", "ミラノ風ドリア")

print(f"最初のレストラン名：{first_restaurant.name}")
print(f"最初の料理の種類：{first_restaurant.menu}")
first_restaurant.set_number_served(3)
first_restaurant.read_served()

print(f"\n2つ目のレストラン名：{second_restaurant.name}")
print(f"2つ目の料理の種類：{second_restaurant.menu}")

print(f"\n3つ目のレストラン名：{third_restaurant.name}")
print(f"3つ目の料理の種類：{third_restaurant.menu}")
