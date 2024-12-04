#validate mail id
#starts with aplhabet 
#numbers (optional)
# @gmail.com
#before at 6 to 64 characters

from re import fullmatch
pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

gmail=input("Enter the mail id :")

matcher=fullmatch(pattern,gmail)
print("Invalid" if matcher==None else "Valid")