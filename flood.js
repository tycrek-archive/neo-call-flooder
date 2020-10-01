require('dotenv').config()

var twilio = require('twilio');
var client = new twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

client.calls.create({
	record: true,
	url: process.env.TWIML_URL,
	to: process.env.TARGET_PHONE_NUMBER,
	from: process.env.SOURCE_PHONE_NUMBER
})
	.then((message) => console.log(message.sid))
	.catch((error) => console.warn(error));
