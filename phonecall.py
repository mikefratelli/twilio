import os
#pip3.6 install twilio
from twilio.rest import Client

parser = argparse.ArgumentParser(description='sends phone call to specified number')
parser.add_argument('number', help='the phone number of the agent to call')
args = parser.parseargs()

account_sid = 'os.environ["TWILIO_SID"];
auth_token = 'os.environ["TWILIO_AUTH_TOKEN"];

client = Client(account_sid, auth_token);

call = client.calls.create(
    to=args.number,
    from_="<twilio phone number>",
    #URL must get an http source, https won't work
    url="<hosted xml data>"
)

print(call.sid)
