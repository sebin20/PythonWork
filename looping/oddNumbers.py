end=int(input("Enter the end :"))
start=int(input("Enter the starting :"))

if start>end :
    start,end=end,start

while start<end:
    if start%2!=0:
        print(start)
   
    start+=1