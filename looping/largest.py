num=int(input("Enter the number :"))  
max_value=0
n=num 
while n>0 : 
    last_digit=n%10 
    if last_digit>max_value :
        max_value=last_digit
    
    n=n//10     
print(f"Max digit is : {max_value}")