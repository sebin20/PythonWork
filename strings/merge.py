text1="PQR"
text2="ABC"
max_length=len(text1) if len(text1)>len(text2) else len(text2)
result=""
for i in range(0,len(text1)):
    result=result+text1[i]+text2[i]
    
print(result)