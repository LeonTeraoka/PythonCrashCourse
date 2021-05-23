def simple_message(message, completed_messages):
	"""メッセージを出力"""
	while message:
		msg = message.pop()
		completed_messages.append(msg)

def show_messages(completed_messages):
	"""メッセージを移す"""
	for completed_message in completed_messages:
		print(completed_message)

message = ["おはよう", "こんにちは", "こんばんは"]
completed_messages = []

simple_message(message, completed_messages)
show_messages(completed_messages)


#def display_message(message):
#	"""メッセージを出力"""
#	print(f"メッセージ：{message.title()}")

#display_message("hello world")
