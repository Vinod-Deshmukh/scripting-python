# Script 18, Random Joke Generator.
# store Quotes in a List 
# Use random.choice(list)
import requests
import json
url="https://api.chucknorris.io/jokes/random"

response=requests.get(url,timeout=10)
print(f"Staus Code: {response.status_code} \n")
data=response.json()
# print("Pretty Response:")
# print(json.dumps(data,indent=4))
joke=data["value"]
print(f"Joke: {joke}")
