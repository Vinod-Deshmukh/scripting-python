# Script 16 Website Status Checker 2
import requests
from requests.exceptions import RequestException
url=input("Enter the website URL (including http:// or https://): ")
try:
    response=requests.get(url)
    if response.status_code==200:
        print(f"{url} is UP!")
    else:
        print(f"{url} return status code {response.status_code} (may be DOWN or Have an Issue)) ")
except RequestException as e:
    print(f"{url} is DOWN!")
    print(f"Error: {e}")