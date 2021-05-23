def send_message(message, completed_messages):
	"""メッセージを出力"""
	print(message)
	while message:
		msg = message.pop()
		print(f"\n送信中：{msg}")
		completed_messages.append(msg)


def sent_messages(completed_messages):
	print(message)
	"""メッセージを移す"""
	for completed_message in completed_messages:
		print(f"\n送信済:{completed_message}")


message = ["おはよう", "こんにちは", "こんばんは"]
completed_messages = []

send_message(message, completed_messages)
sent_messages(completed_messages)