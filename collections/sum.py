arr=[]
n=int(input("Enter no of elements: "))
for i in range(n):
    element=int(input("Enter the element: "))
    arr.append(element)
    
print(arr)

sum=int(input("Enter the sum : "))
pair_found=False

for i in range(0,len(arr)-1):
    
    for j in range(i+1,len(arr)):
        
        if arr[i] + arr[j]==sum:
            
            print(f"pair is : {arr[i]} , {arr[j]}")
            pair_found=True
            
    if pair_found==True:
        break
        