def is_prime():
    num=int(input("Enter the number:")) 
    
    is_prime=True
    
    for i in range(2,num):
        
        if num%i==0:
            is_prime=False
            break
        
    if is_prime==True:
        print("Prime")
        
    else:
        print("Not prime")
    
is_prime()