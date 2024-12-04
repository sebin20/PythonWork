limit=int(input("Enter the limit  : "))#5
a=0 
b=1 
print(a,end=" ")
print(b,end=" ")
i=1
while i<limit-1:
    print(a+b,end=" ")
    
    a,b=b,a+b
    i+=1
    
    

    