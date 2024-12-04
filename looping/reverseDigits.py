num=int(input("Enter the number to reverse :")) 
rev=0
n=num 
while n>0 : 
    reminder=n%10 
    print(reminder,end=" ")
    n=n//10    