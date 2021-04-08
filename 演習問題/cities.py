cities = {
	"usa": {
		"country": "ニューヨーク",
		"population": "3.282億人",
		"fact": "自由",
	},

	"japan": {
		"country": "tokyo",
		"population": "1.263億人",
		"fact": "社畜",
	},

	"china": {
		"country": "北京",
		"population": "13.98億人",
		"fact": "共産党",
	},
}

for city, details in cities.items():
	print(f"\n国:{city}")
	country = f"{details['country']}"
	population = f"{details['population']}"
	fact = f"{details['fact']}"
	print(f"\t地域:{country}")
	print(f"\t人口:{population}")
	print(f"\t特徴:{fact}")

