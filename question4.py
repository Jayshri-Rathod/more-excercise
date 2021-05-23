number1=int(input("enter first number"))
number2=int(input("enter second number"))
number3=int(input("enter third number"))
if number1>number2 and number1>number3:
    print(number1,"is gretest")
elif number2>number1 and number2>number3:
    print(number2,"is gretest")
elif number3>number2 and number3>number1:
    print(number3,"is gretest")