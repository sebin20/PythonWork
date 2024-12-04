limit=int(input("Enter the limit  : "))#5
a=0 # 
b=1 #
print(a,end=" ")
print(b,end=" ")
for i in range(limit-2):
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum
    