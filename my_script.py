# goal: print the latest closing price

import json
import os
import requests
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("MY_API_KEY")
print(API_KEY)

# "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=demo"
#request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=" + API_KEY
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey={API_KEY}"
print(request_url)

response = requests.get(request_url)

print("RESPONSE STATUS: " + str(response.status_code))
#print("RESPONSE TEXT: " + response.text)

parsed_response = json.loads(response.text)

print("THE LATEST CLOSING PRICE IS: $XYZ.00")
