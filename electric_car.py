class Car:
	"""自動車を表すシンプルな実装例"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"走行距離は{self.odometer_reading}kmです。")

	def update_odometer(self, km):
		if km >= self.odometer_reading:
			self.odometer_reading = km
		else:
			print("走行距離は減らせません！")

	def increment_odometer(self, km):
		self.odometer_reading += km

class ElectricCar(Car):
	"""電気自動車に特有の情報を表すクラス"""

	def __init__(self, make, model, year):
		"""
		親クラスの属性を初期化する
		次に電気自動車に特有の属性を初期化する
		"""
		super().__init__(make, model, year)
		self.battery_size = 75

	def describe_battery(self):
		"""バッテリーのサイズの説明文を出力する"""
		print(f"この車のバッテリーは{self.battery_size}-kWhです。")

	def fill_gas_tank(self):
		"""電気自動車にはガソリンのタンクは存在しない"""
		print(f"この自動車にはガソリンのタンクはありません！")

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
