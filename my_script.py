# goal: print the latest closing price

import json
import os
import requests
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("MY_API_KEY")
#print(API_KEY)

# "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=demo"
#request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=" + API_KEY
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey={API_KEY}"
print(request_url)

response = requests.get(request_url)

print("RESPONSE STATUS: " + str(response.status_code))
#print("RESPONSE TEXT: " + response.text)

parsed_response = json.loads(response.text)

# breakpoint()
# (pdb) type(parsed_response)
#> <class 'dict'>
#
# (pdb) parsed_response.keys()
#> dict_keys(['Meta Data', 'Time Series (Daily)'])
#
# (pdb) type(parsed_response["Time Series (Daily)"])
#> <class 'dict'>
#
# (pdb) parsed_response["Time Series (Daily)"].keys()
#> dict_keys(['2019-02-19', '2019-02-15', '2019-02-14' ... '2018-09-26', '2018-09-25'])
#
# (pdb) parsed_response["Time Series (Daily)"]["2019-02-19"]
#> {'1. open': '1601.0000', '2. high': '1634.0000', '3. low': '1601.0000', '4. close': '1627.5800', '5. volume': '3673878'}

print(parsed_response["Time Series (Daily)"]["2019-02-19"]["4. close"])
# > '1627.5800'

print("THE LATEST CLOSING PRICE IS: $XYZ.00")

#
# BUT THE LATEST DAY WON'T ALWAYS BE "2019-02-19"
# ... SO HERE'S A WAY TO GET THE LATEST DAY, WHATEVER IT IS
#
tsd = parsed_response["Time Series (Daily)"] #> 'dict'
#
# What keys or attributes does this dictionary have?
# ... see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/dictionaries.md
day_keys = tsd.keys() #> 'dict_keys' of all the day values
#
# convert weird dict_keys datatype to a list so we can work with it!
days = list(day_keys) #> 'list' of all the day values
print(days[0]) # 'str' of the latest day!
latest_day = days[0] #> '2019-02-19'
#
print(parsed_response["Time Series (Daily)"][latest_day]["4. close"])
# > '1627.5800'
#
print(tsd[latest_day]["4. close"])
# > '1627.5800'
