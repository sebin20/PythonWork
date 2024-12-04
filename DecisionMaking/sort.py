num1=int(input("Enter first number: "))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))

if (num1>num2>num3):        # 7 6 5   6 7 5
    print(f"{num1} > {num2} > {num3}")

elif (num2>num1>num3):
    print(f"{num2}  > {num1} > {num3}")
    
elif (num3>num2>num1) :
    print(f"{num3} > {num2} > {num1}")
    
elif num1>num3>num2:
    print(f"{num1}  > {num3} >{num2}")
    
elif num2>num3>num1:
    print(f"{num2} > {num3} >{num1}")

elif num3>num1>num2:
    print(f"{num3} > {num1} > {num2}")
    