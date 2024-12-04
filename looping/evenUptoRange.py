start=int(input("Enter the starting :"))
end=int(input("Enter the end :"))

reverse=True if start>end else False 
i=start

while(i<=end if reverse==False else i>=end ) :
    if i%2==0 :
        print(i)
    if reverse==False :
        i+=1
        
    else :
        i-=1
          

