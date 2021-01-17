print ("2-3 個人的なメッセージ")

name = "Eric"
print (f"こんにちは{name.title()}、今日はPythonを学びますか？")

print("2-4 名前の大文字小文字")
print(name.title())
print(name.upper())
print(name.lower())

print("2-5 名言の引用")
name = "アルベルト・アインシュタイン"
print(f'{name}は"挫折を経験したことがない者は、何も新しいことに挑戦したことがないということだ。"と言った')

print("2-6 名言の引用2")
famous_person = "アルベルト・アインシュタイン"
message = f'{famous_person}は"挫折を経験したことがない者は、何も新しいことに挑戦したことがないということだ。"と言った'
print(message)

print("2-7 名前から空白を取り除く")
name = "muffin fix "
print (name.rstrip() + "a")
name = " muffin fix"
print("a" + name.lstrip())
name = " muffin fix "
milk = "milk"
print(f"\t{milk}{name.strip()}\n{name.strip()}{milk}")
