# Script 18, Random Joke Generator.
# store Quotes in a List 
# Use random.choice(list)
import requests
import random
# API url
url="https://api.chucknorris.io/jokes/random"
# Local backup jokes
local_jokes=["Chuck Norris once had sex with a dinosaur and then they became extinct."
,"Chuck Norris is so American, he eats tyranny and shits apple pie."
,"Chuck Norris can access the DB from the UI."
,"Chuck Norris can rear-end his own car."
,"Chuck Norris taught Prometheus how to wipe his ass."
]
def get_api_jokes():
    """Fetch Jokes from API,return None if fails."""
    try:
        response=requests.get(url,timeout=5)
        # raises error if not 200
        response.raise_for_status()
        data=response.json()
        return data.get("value",None)
    except Exception:
        return None
def get_random_joke():
    """Randomly chooses API jokes or local jokes."""
    # 50% chance.
    if random.choice([True,False]):
        joke=get_api_jokes()
        if joke:
            return joke
        # Fallback to local jokes
        return random.choice(local_jokes)
# Main program
if __name__=="__main__":
    try:
        count=int(input("How many jokes do you want?"))
    except ValueError:
        # default to 1 if input is invalid.
        count=1
    print("\n Here are your jokes:\n")
    for i in range(count):
        print(f"{i+1}.{get_random_joke()}")
