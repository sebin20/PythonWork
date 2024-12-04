num=int(input("Enter the number :"))  #23
count=0
n=num  #23
while n>0 : 
    n=n//10      
    count+=1
   
print(f"count of the digits in {num} : {count}")
