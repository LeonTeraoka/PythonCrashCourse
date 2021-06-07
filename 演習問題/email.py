def show_draft_email(draft_emails, sent_emails):
	"""
	下書きを送信し、各下書きが送信後にsent_emailsに移動する
	"""
	while draft_emails:
		current_email = draft_emails.pop()
		print(f"送信中：{current_email}")
		sent_emails.append(current_email)

def show_sent_email(sent_emails):
	"""送信されたすべてのメール件名を出力する"""
	print("\n以下のタイトルが送信されました")
	for sent_email in sent_emails:
		print(sent_email)

draft_emails = ["昇給の件", "勤務日報の件", "謝罪の件"]
sent_emails = []

show_draft_email(draft_emails, sent_emails)
show_sent_email(sent_emails)
