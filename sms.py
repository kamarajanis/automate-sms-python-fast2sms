#https://www.fast2sms.com/dashboard/dev-api

import sys
import requests

numberss=sys.argv[1]
messagess=sys.argv[2]

print(numberss)
print(messagess)

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"YOUR_API_KEY",
               "sender_id":"FSTSMS",
               "message":messagess,
               "language":"english",
               "route":"p",
               "numbers":numberss}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

if response.status_code==200:
    print("Message Sent Successfully")
else:
    print("Message Not Sent Try again")

#print("\n")
#print(response)
#print(type(response))
#print(response.status_code)          
#print(type(response.status_code))

