# Script 18, Random Joke Generator.
# store Quotes in a List 
# Use random.choice(list)
import requests
import random
url="https://api.chucknorris.io/jokes/random"

response=requests.get(url,timeout=10)
print(f"Staus Code: {response.status_code} \n")
data=response.json()
# print("Pretty Response:")
# print(json.dumps(data,indent=4))
joke=data["value"]
random_joke=["Chuck Norris once had sex with a dinosaur and then they became extinct."
,"Chuck Norris is so American, he eats tyranny and shits apple pie."
,"Chuck Norris can access the DB from the UI."
,"Chuck Norris can rear-end his own car."
,"Chuck Norris taught Prometheus how to wipe his ass."
]
joke_list=random.choice(random_joke)
print(f"Joke:{joke}")
print(f"Joke:{joke_list}")