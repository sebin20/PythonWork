#Write a Python program to remove duplicates from a list.
arr=[3,4,5,6,6,7,8,9,9]
without_duplicate=[]

for num in arr:
    if num not in without_duplicate:
        without_duplicate.append(num)
        
print(without_duplicate)
