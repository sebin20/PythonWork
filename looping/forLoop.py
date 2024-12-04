start=int(input("Enter the start :"))
end=int(input("Enter the end :"))
if start<end :
    
   for num in range (start,end+1) :
       print(num)
       
else :
    for num in range(start,end-1,-1):
        print(num)