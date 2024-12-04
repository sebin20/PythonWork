arr=[2,4,5,5,7,8,9,6]

element=int(input("Enter the number :"))

flag=False

for i in range(len(arr)):
    if arr[i]==element:
        flag=True
        idex=i
        break
        
print("elemnet found" if flag==True else "not found")
print("Element found at index",i)