favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
}

#langueage = favorite_languages["sarah"].title()
#print(f"Sarahの好きなプログラミング言語は{langueage}です。")
for name, language in favorite_languages.items():
	print(f'{name.title()}の好きなプログラミング言語は{language.title()}です。')
