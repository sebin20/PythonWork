num1=int(input("Enter first number: "))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))
if num1>num2 and num1>num3 :
    if num2>num3:
        print(f"Sorting order is {num1} > {num2} > {num3}")
    else :
         print(f"Sorting order is {num1} > {num3} > {num2}")
         
         
elif num2 >num1 and num2>num3:
    if num1>num3:
        print(f"Sorting order is {num2} > {num1} > {num3}")
    else :
         print(f"Sorting order is {num2} > {num3} > {num1}")
         
    
elif num3> num1 and num3> num2 :
    if num2>num1:
        print(f"Sorting order is {num3} > {num2} > {num1}")
    else :
         print(f"Sorting order is {num3} > {num1} > {num2}")
 
 
