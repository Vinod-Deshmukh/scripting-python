# utility script 7 Temptature Converter.
temp=input("Enter C or c for celsius and F or f for Fahrenheit:")
if temp == "C" or temp == "c":
    tempC=int(input("Enter the temprature in Celsius which  you want to convert into F: "))
    tempF=int((tempC*9/5)+32)
    print(F"temperature you entered in C is {tempC} C")
    print(f"your temprature in F is {tempF} F")
elif temp == "F" or temp == "f":
    tempF=int(input("Enter the temprature in F which  you want to convert into C: "))
    tempC=int((tempF-32)*5/9)
    print(F"temperature you entered in Fahrenheit is {tempF} F")
    print(f"your temprature in C is {tempC} C")
else:
    print("Invalid Input")
