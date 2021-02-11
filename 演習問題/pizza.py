pizzas = ["chicago", "sicilian", "greek", "meat"]
friend_pizzas = pizzas[:]
friend_pizzas.append("pepperoni")
print(pizzas)
print(friend_pizzas)

for pizza in pizzas:
	print(f"私は{pizza.title()}が好きです。")
print("私はピザが大好きです！")
