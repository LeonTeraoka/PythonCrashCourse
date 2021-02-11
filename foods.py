my_foods = ["ピザ", "だんご", "ケーキ"]
friend_foods = my_foods[:]

#これはコピーとしては正しく動作しません
#friend_foods = my_foods

my_foods.append("チョコレート")
friend_foods.append("アイスクリーム")

print("私が好きな食べ物")
print(my_foods)
print("\n友達が好きな食べ物")
print(friend_foods)
for my_foods in my_foods[0:2]:
	print(my_foods)