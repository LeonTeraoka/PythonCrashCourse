#for twenty in range(1, 21):
#	print(twenty)

#for million in range(1, 1000001):
	#print(million)


million = [million for million in range(1, 1000001)]
print(f"{min(million)}")
print(f"{max(million)}")
print(f"{sum(million)}")

twenty = [twenty for twenty in range(1, 21, 1)]
print(twenty)

thirty = [value for value in range(3, 33, 3)]
print(thirty)

cubic = []
for value in range(1, 11):
	cubic = value**3
	print(cubic)


cubic_number = [value**3 for value in range (1, 11)]
print(cubic_number)
