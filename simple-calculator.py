# number1=int(input("Enter the first Number:"))
# number2=int(input("Enter the second Number:"))
# operation=input("Enter '+' for addition, '-' for substraction, '*' for multiplication and '/' for division. ")
# result=0
i=1
while i==1:
    number1=int(input("Enter the first Number:"))
    number2=int(input("Enter the second Number:"))
    operation=input("Enter '+' for addition, '-' for substraction, '*' for multiplication and '/' for division. ")
    result=0
    if operation=='+':
        result=number1+number2
        print(f"{number1} + {number2} = {result}")
    elif operation=='-':
        result=number1-number2
        print(f"{number1} - {number2} = {result}")
    elif operation=='*':
        result=number1*number2
        print(f"{number1} * {number2} = {result}")    
    else:
        result=number1/number2
        print(f"{number1} / {number2} = {result}")    
    i=int(input("Enter '1' to continue , Enter '0' to stop:" )) 