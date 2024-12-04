arr=[2,2,3,3,4,5,4,4,5,6,3,6,8]
arr.sort()
duplicate=[]
for i in range(0,len(arr)-1):
    j=i+1
    
    result=arr[j]-arr[i]
    if result==0:
        if arr[i] not in duplicate:
            duplicate.append(arr[i])
print(duplicate)