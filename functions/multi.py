def multiplication(num,n=10):
        
    for i in range(1,n+1):
        print(f"{num} * {i}= {num*i}")


num=int(input("Enter the number :"))
n=input("Enter the range :")
if n :
    multiplication(num,int(n))
else :
    multiplication(num)
        