cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ["bmw", "アウディ", "日産", "すばる"]
cars.sort()
print(cars)
print("-------------------")
cars = ["bmw", "audi", "toyota", "subaru"]
print("元のリスト")
print(cars)
print("\nソートされたリスト")
print(sorted(cars))
print("\n元のリストを再表示")
print(cars)
print("-------------------")
cars.reverse()
print(cars)
#len(cars)
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())