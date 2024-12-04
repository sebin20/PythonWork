#validate years from 1800-2024

from re import fullmatch
year=input("Enter the year:")
pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"

matcher=fullmatch(pattern,year)

if matcher==None:
    print("Invalid")
    
else:
    print("valid")


