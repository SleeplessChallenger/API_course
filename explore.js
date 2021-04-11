const Twilio = require("twilio");

const client = new Twilio(
	'ACCOUNT SID',
	'AUTH TOKEN'
	);

client.messages
	.list()
	.then(messages =>
		console.log(`The most recent message is ${messages[0].body}`))
	.catch(err => console.error(err));

console.log('Gathering your message log');
