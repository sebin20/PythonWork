text1=input("Enter first string : ")
text2=input("Enter second string : ")
smallest_text=text1 if len(text1)<len(text2) else text2
largest_text=text1 if len(text1)>len(text2) else text2
result=""
for i in range(0,len(smallest_text)):
    result=result+text1[i]+text2[i]

balance_text=result+ largest_text[len(smallest_text):]
print(balance_text)