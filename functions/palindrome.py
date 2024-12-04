num=int(input("Enter the number to check palindrome :")) 

def palindrome(num):
    rev=0
    n=num #23
    while n>0 : 
        reminder=n%10 
        rev=rev*10 +reminder  
        n=n//10   
   
    if rev==num :
         print("Its a palindrome...")
    
    else :
        print("Its not palindrome..")
        
palindrome(num)
