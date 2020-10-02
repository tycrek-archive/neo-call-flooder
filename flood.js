require('dotenv').config()

const client = new require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

// Set this to 0 for infinite
const max = 0;

// Don't change this
let count = 1;

console.info(`:: Flooding [ ${process.env.TARGET_PHONE_NUMBER} ] from [ ${process.env.SOURCE_PHONE_NUMBER} ]`);
console.info(`:: Starting flood of ${max} calls`);

// Call finish method when necessary
placeCall().then(finished).catch(console.error);
process.on('SIGINT', finished);

function placeCall() {
	return new Promise((resolve, reject) =>
		client.calls.create({ record: true, url: process.env.TWIML_URL, to: process.env.TARGET_PHONE_NUMBER, from: process.env.SOURCE_PHONE_NUMBER, /* sendDigits: (true) ? '1' : null  */ })
			.then((call) => {
				console.info(`:: Call ${count++} placed with ID [ ${call.sid.substring(0, 8) + '...' + call.sid.substring(call.sid.length - 8)} ]`);
				count < max + 1 || max === 0 ? placeCall().then(resolve).catch(reject) : resolve();
			})
			.catch(reject));
}

function finished() {
	console.info(`:: Finished flood of ${count - 1} calls`);
	process.exit(0);
}
