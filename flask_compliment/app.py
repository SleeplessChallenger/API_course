from flask import (Flask, flash, render_template,
				   redirect, request, url_for)
import os
from twilio.rest import Client


load_dotend()
app = Flask(__name__)
app.secret_key = ''

TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client()
# if we don't put anything into Client()
# then it'll take them from 'env variables'


def get_sent_messages():
	messages = client.messages.list(from_=TWILIO_PHONE_NUMBER)
	return messages

def send_message(to, body):
	client.messages.create(
						 to=to,
						 from_=TWILIO_PHONE_NUMBER,
						 body=body)

@app.route('/', methods=['GET'])
def index():
	messages = get_sent_messages()
	return render_template('base.html', messages=messages)

@app.route('/add-compliment', methods=['POST'])
def add_compliment():
	sender = request.values.get('sender', 'Someone')
	receiver = request.values.get('receiver', 'Someone')
	compliment = request.values.get('compliment', 'wonderful')
	to = request.values.get('to')
	body = f"{sender} says: {receiver} is {compliment}."
		   f"See more compliment at {request.url_for}"
	send_message(to, body)
	flash('Your message was successfully sent')
	return redirect(url_for('base'))


if __name__ == '__main__':
	app.run()
