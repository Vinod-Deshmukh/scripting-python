# Script 17 currency Converter
import requests
import json
def get_live_rates():
    """Fetch live currency rates for INR <-> USD and EUR."""
    try:
        url = "https://open.er-api.com/v6/latest/INR"
        response = requests.get(url,timeout=10)
        print("Status Code:", response.status_code)

        data = response.json()
        print("🌍 Raw API Response:")
        print(json.dumps(data, indent=4))
        usd = data["rates"]["USD"]   # 1 INR = ? USD
        eur = data["rates"]["EUR"]   # 1 INR = ? EUR

        # Also store reverse (for USD→INR, EUR→INR)
        return {"USD": usd, "EUR": eur, "USD_I": 1/usd, "EUR_I": 1/eur}
    except Exception as e:
        print("⚠️ Could not fetch live rates. Using fallback values.")
        return {"USD": 0.011, "EUR": 0.0096, "USD_I": 88.08, "EUR_I": 103.88}

def convert(currency_dict,userInput,amount):
    currency_convert=0
    if userInput==1:
        currency_convert=currency_dict.get("USD")*amount
        # :.2f to round upto 2 decimal places
        print(f"₹ {amount} = $ {currency_convert:.2f} \n")
    elif userInput==2:
        currency_convert=currency_dict.get("EUR")*amount
        print(f"₹ {amount} = € {currency_convert:.2f} \n")
    elif userInput==3:
        currency_convert=currency_dict.get("USD_I")*amount
        print(f"$ {amount} = ₹ {currency_convert:.2f} \n") 
    elif userInput==4:
        currency_convert=currency_dict.get("EUR_I")*amount
        print(f"€ {amount} = ₹ {currency_convert:.2f} \n")   
       
        
        
def main():
    # currency_dict={"USD":0.011,"EUR":0.0096,"USD_I":88.08,"EUR_I":103.88}
    currency_dict=get_live_rates()
    while True:
        print("\n --Welcome To Currency Converter-- \n")
        print("1.Rupee To USD \n")
        print("2.Rupee To Euro \n")
        print("3.USD To Rupee \n")
        print("4.Euro To Rupee \n")
        print("5.Exit \n")
        try:
            userInput=int(input(" "))
        except ValueError:
            print("❌ Please enter a valid number\n")
            continue    
        if userInput==1 or userInput==2:
            amount=int(input("Enter The Amount In ₹ to convert in $/€ "))
            convert(currency_dict,userInput,amount)
        elif userInput==3 or userInput==4:
            amount=int(input("Enter The Amount In $/€ to convert ₹ "))
            convert(currency_dict,userInput,amount)
        elif userInput==5:
            break
        else:
            print("❌ Invalid choice. Please select 1–5.")  

    

if __name__=="__main__":
    main()