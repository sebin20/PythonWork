text=input("Enter the text: ").casefold()
vowels="aeiou"
v_count=0
c_count=0
for ch in text:
    if ch in vowels:
        #print(ch,end=" ")
        v_count=v_count+1
    else :
        c_count=c_count+1
print()
print("vowel count :",v_count)
print("consonents count :",c_count)