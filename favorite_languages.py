favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
}

not_vote = ["jen", "sarah"]

#print("以下の言語が投票されました。")
#for language in set(favorite_languages.values()):
#	print(language.title())
for name in not_vote:
	print(f"{name.title()}さん、投票してください！")

del favorite_languages["jen"] 
del favorite_languages["sarah"]

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}、投票ありがとう。")

#if name not in favorite_languages.keys():
#	print(f"{other.title()}さん投票してください！")
#langueage = favorite_languages["sarah"].title()
#print(f"Sarahの好きなプログラミング言語は{langueage}です。")
#for name, language in favorite_languages.items():
#	print(f'{name.title()}の好きなプログラミング言語は{language.title()}です。')
#friends = ["phil", "sarah"]
#for name in favorite_languages.keys():
#	print(name.title())

#	if name in friends:
#		language = favorite_languages[name].title()
#		print(f"\t{name.title()}、あなたの好きなプログラミング言語は{language}ですね！")