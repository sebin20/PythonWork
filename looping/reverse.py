num=int(input("Enter the number to reverse :"))  #23
rev=0
n=num #23
while n>0 : 
    reminder=n%10 #3   2
    rev=rev*10 +reminder  # 3   30+2
    n=n//10      #2
   
print("Reversed number : ",rev)
