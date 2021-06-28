class User:
	"""ユーザーをモデル化"""

	def __init__(self, first_name, last_name):
		"""ユーザーの名前と名字の属性を格納"""
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		"""ユーザーの名字と名前の詳細"""
		print(f"\nユーザー：{self.first_name} {self.last_name}")

	def greet_user(self):
		"""ユーザーへのあいさつメッセージ"""
		print(f"{self.first_name} {self.last_name}こんにちは")

	def reset_login_attempts(self, login):
		if login >= self.login_attempts:
			self.login_attempts = login
		else:
			print("ログインできません。")

	def increment_login_attempts(self, login):
		self.login_attempts += login
		print(f"{self.login_attempts}回ログインしました。")

class Admin(User):

	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileged():
		privileges = ["投稿を追加する", "投稿を削除する", "ユーザーを利用禁止にする"]
		print(f"管理者の権限一覧:{self.privileges}")

privileges = ["投稿を追加する", "投稿を削除する", "ユーザーを利用禁止にする"]
privileges = Admin(privileges[0])
#greet1 = User("muffn", "men")
#greet2 = User("mint", "men")

#greet1.describe_user()
#greet1.greet_user()

#greet2.describe_user()
#greet2.greet_user()

#greet1.reset_login_attempts(4)
#greet1.increment_login_attempts(3)

#greet1.reset_login_attempts(2)
#greet1.increment_login_attempts(1)
