arr=[2,3,4,5,6,7,8,9]
left=0
right=len(arr)-1
sum=14

while(left<right):
    curr_sum=arr[left]+arr[right]
    
    if curr_sum==sum:
        
        print(f"pair is : {arr[left]},{arr[right]}")
        break
    elif curr_sum >sum:
        right-=1
        
    elif curr_sum<sum:
        left+=1