#Create XML file for twilio to read alerts from. This will contain the host of the issue and a brief description.

import argparse
import subprocess

parser = argparse.ArgumentParser(description='Creates the XML file for Twilio to say things')
parser.add_argument('host', help='the hostname of the server alerting')
parser.add_argument('issue', help='the issue it\'s alerting for')

args = parser.parse_args()

content = [
    '<?xml version="1.0" encoding="UTF-8"?>\n',
    '<Response>\n',
    '<Say voice="alice">Yes, this is dog</Say>\n',
    '</Response>\n'
]

#Include voice.xml with the directory path if serving it from a different location
with open('voice.xml', 'w') as i:
    i.writelines(content[:2])
    i.writelines(f'<Say voice="alice">{args.host} is experiencing {args.issue}. Please respond.</Say>\n')
    i.writelines(content[3])
#In this scenario, the xml file is hosted on an nginx server, apache should work just fine
subprocess.run(["systemctl", "restart", "nginx"])
