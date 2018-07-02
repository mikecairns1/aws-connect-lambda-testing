from datetime import date
from botocore.vendored import requests
import json
import os

print('Loading lambda_handler function')
def lambda_handler(event, context):
    ev = json.dumps(event)
    print(ev)    
    InboundNum = event['Details']['ContactData']['SystemEndpoint']['Address']
    InboundNum = InboundNum[-10:] #trimming it down to a 10 digit number for better playback
    ANI = event['Details']['ContactData']['CustomerEndpoint']['Address']
    ANI = ANI[-10:] # Right String to remove +1
    return {"ANI": ANI, "InboundNum": InboundNum}
