num=int(input("Enter the number : "))
sum=0
n=num
length=len(str(num))
while num!=0 :
    last_digit= num%10
    sum=sum + pow(last_digit,length)
    num=num//10 
        
if n==sum:
       print(f"{n} is an Amstrong number")
    
else :
       print(f"{n} is not an Amstrong number")