from twilio.rest import Client


client = Client(
		'ACCOUNT SID',
		'AUTH TOKEN'
				)

# for msg in client.messages.list():
# 	print(msg.body)

# to delete messages from your account
for msg in client.messages.list():
	print(f"Deleting {msg.body}")
	msg.delete()

msg = client.messages.create(
	to='Number send to',
	from_='+12012524949',
	body='Hello, from Daniil!')

print(f"Created a new message: {msg.sid}")
