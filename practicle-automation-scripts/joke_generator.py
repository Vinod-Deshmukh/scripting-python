# Script 18, Random Joke Generator.
# store Quotes in a List 
# Use random.choice(list)
import requests
import json
url="https://api.chucknorris.io/jokes/random"

response=requests.get(url,timeout=10)
print(response.status_code)