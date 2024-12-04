#Write a Python program to merge two lists and sort the resulting list.
arr1=[1,22,3,14]
arr2=[6,7,8,9]

# arr3=arr1+arr2
# arr3.sort()
# print(arr3)

arr1.extend(arr2)
print(arr1)