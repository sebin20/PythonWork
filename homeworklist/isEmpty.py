#Write a Python program to check if a list is empty.
n=int(input())
arr=[]
isEmpty=False
for i in range(n):
    num=int(input(""))
    arr.append(num)
    
length=len(arr)
if length==0:
    isEmpty=True
print(isEmpty)