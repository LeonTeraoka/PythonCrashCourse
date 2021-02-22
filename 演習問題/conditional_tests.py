greeting = "Hello"
if greeting == "Hello":
	print("true")
if greeting == "yo":
	print("false")
if greeting.lower() == "hello":
	print("true")
if greeting.lower() == "Hello":
	print("false")

number = 20
if number == 20:
	print("true")
if number == 19:
	print("false")
if number >= 19:
	print("true")
if number >= 21:
	print("false")
if number <= 21:
	print("true")
if number <= 19:
	print("false")

number_0 = 22
number_1 = 22
if number_0 >= 21 and number_1 >=21:
	print("true")
number_0 = 18
if number_0 >= 21 or number_1 >= 21:
	print("false")

greetings = ["Hello", "hi", "hey",]
if "hi" in greetings:
	print("true")
if "yo" not in greetings:
	print("false")
