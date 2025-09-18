# Script 17 currency Converter
def convert(currency_dict,userInput,amount):
    currency_convert=0
    if userInput==1:
        currency_convert=currency_dict.get("USD")*amount
        print(f"₹ {amount} = $ {currency_convert} \n")
    elif userInput==2:
        currency_convert=currency_dict.get("EUR")*amount
        print(f"₹ {amount} = € {currency_convert} \n")
    elif userInput==3:
        currency_convert=currency_dict.get("USD_I")*amount
        print(f"$ {amount} = ₹ {currency_convert} \n")
    elif userInput==4:
        currency_convert=currency_dict.get("EUR_I")*amount
        print(f"€ {amount} = ₹ {currency_convert} \n")   
       
        
        
def main():
    currency_dict={"USD":0.011,"EUR":0.0096,"USD_I":88.08,"EUR_I":103.88}
    while True:
        print("\n --Welcome To Currency Converter-- \n")
        print("1.Rupee To USD \n")
        print("2.Rupee To Euro \n")
        print("3.USD To Rupee \n")
        print("4.Euro To Rupee \n")
        print("5.Exit \n")
        userInput=int(input(" "))
        if userInput==1 or userInput==2:
            amount=int(input("Enter The Amount In ₹ to convert in $/€ "))
            convert(currency_dict,userInput,amount)
        elif userInput==3 or userInput==4:
            amount=int(input("Enter The Amount In $/€ to convert ₹ "))
            convert(currency_dict,userInput,amount)
        elif userInput==5:
            break
        else:
            print("Invalid Input ")  

    

if __name__=="__main__":
    main()