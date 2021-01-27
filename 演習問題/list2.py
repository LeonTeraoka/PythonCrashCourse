language = ["ruby", "python", "java", "php"]
#リスト内の値を用いてメッセージ作成
print(f"私は{language[1].title()}を勉強中")
#リスト内の要素変更
language[-1] = "C"
print(language)
#リスト内に要素追加
language.append("php")
print(language)
#リスト内に要素挿入
language.insert(0, "Swift")
print(language)
#リスト内から要素を削除、del文、pop()、remove()
del language[0]
print(language)
not_study = language.pop(-1)
print(f"私は{not_study}を勉強していません。")
language.remove("java")
print(language)
#sort()でソート
language.sort()
print(language)
#sorted()で一時的にソート
print(sorted(language))
#逆順で出力
language.sort(reverse=True)
print(language)
#リストの長さを調べるlen()関数
print(len(language))
