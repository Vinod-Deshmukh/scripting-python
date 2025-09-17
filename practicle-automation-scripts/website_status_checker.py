# Script 16 Website Status Checker

# Import the requests library to make HTTP requests
import requests

# Ask the user to input the website URL
website_url = input("Enter the website URL (including http:// or https://): ")

# Try to send a GET request to the website
try:
	response = requests.get(website_url)
	# If the request is successful, check the status code
	if response.status_code == 200:
		print(f"{website_url} is UP!")
	else:
		print(f"{website_url} returned status code {response.status_code} (may be DOWN or have issues)")
except requests.exceptions.RequestException as e:
	# If there is any error (like connection error), print that the website is down
	print(f"{website_url} is DOWN! Error: {e}")
 