arr=[12,2,4,34,14,18]

arr.sort()

is_present=False
search_element=int(input("Enter the element :"))

low=0
upp=len(arr)-1

while(low<=upp):
    mid=(low+upp)//2
    
    if search_element==arr[mid]:
        is_present=True
        break
    
    elif search_element<arr[mid]:
        upp=mid-1
        
    elif search_element> arr[mid]:
        low=mid+1
        
print("elemnt present" if is_present==True else "not found")
