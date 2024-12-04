first=input("Enter first string: ")
second=input("Enter second string: ")
if len(first)!=len(second):
    print("Not anagram")
    
else:
    f=sorted(first)
    s=sorted(second)
    if f==s:
        print("anagram")
    else:
        print("Not anagram")
            
                
