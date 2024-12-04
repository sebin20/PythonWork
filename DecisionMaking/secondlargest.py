num1=int(input("Enter first number: "))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))
if (num1 >num2 and num2 >num3) or (num1 <num2 and num2 <num3) :   #  5 6 7   7 6 5  
     second_largest=num2
    
elif (num1 >num2 and num1<num3) or (num2>num1 and num1 >num3) :    #6 5 7  6 7 5
     second_largest=num1
   
    
elif (num1>num3 and num3>num2) or (num2 >num3 and num3>num1) : #7 5 6   5 7 6 
     second_largest=num3
   
     
print(f"Second largest no is {second_largest}")
