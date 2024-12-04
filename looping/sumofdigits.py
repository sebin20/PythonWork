num=int(input("Enter the number :"))  
sum=0

while num>0 : 
    last_digit=num%10 
    sum=sum+last_digit
    num=num//10     
print(f"Sum is {sum}")