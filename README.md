# neo-call-flooder

Spam call phone numbers using Twilio.

## Disclaimer

**For educational purposes only!** Do not use this to spam call any number you don't own. I'm not responsible nor liable for any legal issue this may cause.

## Installation

### Requirements

1. Node.js & NPM
2. A Twilio account with:
   - usable account credit
   - a Programmable Voice API phone number
   - a TwiML Bin (sample data found in [`twiml.xml`](twiml.xml))
3. A phone number to test it on (either your own or ask a friend for permission)

### Install

```bash
$ git clone https://github.com/tycrek/neo-call-flooder && cd neo-call-flooder
$ npm i
$ cp default.env .env
```

## Run

1. Open `.env` and add your information.
   - Target and source phone numbers should be in the format of `+12223334444`
   - `MAX` is the desired maximum calls to make. Default is `0` which loops until `CTRL+C` is pressed.
2. Run `npm start` to start the flooder. Press `CTRL+C` to stop the flooder (or wait for `MAX_CALLS` calls to be placed).
