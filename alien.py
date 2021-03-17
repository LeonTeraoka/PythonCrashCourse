#alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
#print(f"最初のX座標: {alien_0['x_position']}")

#if alien_0["speed"] == "fast":
#	x_increment = 1
#elif alien_0["speed"] == "medium":
#	x_increment = 2
#else:
#	x_increment = 3

#alien_0["x_position"] = alien_0["x_position"] + x_increment

#print(f"新しいX座標: {alien_0['x_position']}")

alien_0 = {"color": "green", "points": 5}
#print(f"エイリアンは{alien_0['color']}です。")

#alien_0["color"] = "yellow"
#print(f"エイリアンは{alien_0['color']}になりました")
#alien_0["x_position"] = 0
#alien_0["y_position"] = 25
print(alien_0)

del alien_0["points"]
print(alien_0)
#alien_0 = {"color": "green"}

#new_points = alien_0["points"]
#print(alien_0["color"])
#print(f"{new_points}点獲得しました！")