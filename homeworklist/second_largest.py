# Write a Python program to find the second largest element in a list.
n = int(input("Enter the range : "))
arr=[]
for i in range(n):
    num=int(input(""))
    arr.append(num)

max_value=max(arr)
min_value=min(arr)

for i in range (len(arr)):
        if (arr[i]>=min_value and arr[i]<max_value):
              min_value=arr[i]
              
print("second largest value is :",min_value)
    