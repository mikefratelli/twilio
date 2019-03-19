import os
#pip3.6 install twilio
from twilio.rest import Client

account_sid = 'os.environ["TWILIO_SID"];
auth_token = 'os.environ["TWILIO_AUTH_TOKEN"];

client = Client(account_sid, auth_token);

call = client.calls.create(
    to="<receiving phone number>",
    from_="<twilio phone number>",
    #URL must get an http source, https won't work
    url="<hosted xml data>"
)

print(call.sid)
