bicycles = ["trek", "cannondale", "redline", "specialized", "woom"]
print("リストの最初の3つの要素です。")
print(bicycles[:3])
print("リストの中央の3つの要素です。")
print(bicycles[1:4])
print("リストの最後の3つの要素です。")
print(bicycles[2:])
print("----------------------------")
print(bicycles[0])
print(bicycles[0].title())
print("----------------------------")

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-3])

print("----------------------------")
message = f"私の最初の自転車は{bicycles[0].title()}でした。"
print(message)
