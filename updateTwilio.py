import os
import sys
from twilio.rest import Client
#from dotenv import load_dotenv
#dotenv_path = "twilio.env"
#load_dotenv(dotenv_path)

lambdaurl=sys.argv[1]
account_sid=sys.argv[2]
auth_token=sys.argv[3]
TWILIO_PHONE=sys.argv[4]
#account_sid=os.getenv('TWILIO_ACCOUNT_SID')
#auth_token=os.getenv('TWILIO_AUTH_TOKEN')
#TWILIO_PHONE=os.getenv('TWILIO_PHONE')

client = Client(account_sid, auth_token)

incoming_phone_number = client \
    .incoming_phone_numbers(TWILIO_PHONE) \
    .update(sms_url=lambdaurl)

print(incoming_phone_number.friendly_name)
