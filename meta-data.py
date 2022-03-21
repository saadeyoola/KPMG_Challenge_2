import json
import requests
import re

req = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document')

f = open("/etc/ec2_metadata.env","w+")
pattern = re.compile(r'(?<!^)(?=[A-Z])')

for key in req.json().keys():
    env = pattern.sub('_', key).upper()
    f.write("{}={}\n".format(env, req.json()[key]))

f.close()
