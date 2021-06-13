class User:
	"""ユーザーをモデル化"""

	def __init__(self, first_name, last_name):
		"""ユーザーの名前と名字の属性を格納"""
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		"""ユーザーの名字と名前の詳細"""
		print(f"\nユーザー：{self.first_name} {self.last_name}")

	def greet_user(self):
		"""ユーザーへのあいさつメッセージ"""
		print(f"{self.first_name} {self.last_name}さんこんにちは")

greet1 = User("muffn", "men")
greet2 = User("mint", "men")

greet1.describe_user()
greet1.greet_user()

greet2.describe_user()
greet2.greet_user()
