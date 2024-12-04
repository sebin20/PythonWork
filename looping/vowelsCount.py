vowels="aeiou"
string=input("Enter the string : ").lower()
length=len(string)
count=0
i=0

while i<length :
    if string[i] in vowels :
        count+=1
    i+=1
    
print(f"Count is {count}")