arr1=[2,3,4,5,6,8]
i=0
j=i+1
# arr1.sort()
while(i<len(arr1)-1):
    if arr1[j]-arr1[i]==1:
        i+=1
        j=i+1
    else :
        print(arr1[i]+1,"is missing")
        break
    
       