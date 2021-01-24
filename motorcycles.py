motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("honda")
print(motorcycles)
print("------------------")

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
print("--------------------")

del motorcycles[0]
del motorcycles[1]
print(motorcycles)
print("-------------------")

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop(0)
print(f"最近手に入れたバイクは{last_owned.title()}です。")
print(motorcycles)
too_expensive = "yamaha"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}は私には高すぎます。")
print("--------------------")
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}は私には高すぎます。")

