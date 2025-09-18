import requests
import json

url = "https://open.er-api.com/v6/latest/INR"

try:
    response = requests.get(url, timeout=10)  # timeout prevents hanging
    print("Status Code:", response.status_code)

    data = response.json()
    print("🌍 Pretty Response:")
    print(json.dumps(data, indent=4))

    usd = data["rates"]["USD"]
    eur = data["rates"]["EUR"]

    print("1 INR =", usd, "USD")
    print("1 INR =", eur, "EUR")

except Exception as e:
    print("⚠️ Error:", e)
