people = {
	"muffn": {
		"first_name": "muffin", 
		"last_name": "fix", 
		"age": 30, 
		"city": "ikebukuro"
		},
	
	"muffin": {
		"first_name": "men", 
		"last_name": "muff", 
		"age": 25, 
		"city": "tachikawa"
		},
	
	"mint": {
		"first_name": "mintia", 
		"last_name": "men", 
		"age": 18, 
		"city": "kitasenju"
		},
	}

print(people)

for person, privacy in people.items():
	print(f"\n名前:{person}")
	print(f"\n情報:{privacy}")
#print(muffn["last_name"].title())
#print(muffn["age"])
#print(muffn["city"].title())
