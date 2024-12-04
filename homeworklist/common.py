# Write a Python program to find common elements in two lists.
arr=[1,2,3,4,5,6]
arr1=[5,6,7,8,9,10]

for num in arr:
    if num in arr1:
        print(num)