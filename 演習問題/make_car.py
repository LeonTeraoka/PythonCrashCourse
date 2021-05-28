def build_car(maker, brand, **make_car):
	"""自動車についての情報を出力"""
	make_car["company"] = maker
	make_car["model"] = brand
	return make_car

car = build_car("スバル", "レガシィ",
						color="ブルー",
						recorder=True)
print(car)