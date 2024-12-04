num=int(input("Enter the number :"))  
n=2
if num!=2 :
  while n<num: 
    if num%n ==0:
        flag=0
        break
    else :
        flag=1
       
    n=n+1
    
else :
    flag=1
if flag==1:
    print(f"{num} is prime..")

else :
    print(f"{num} is not prime..")
