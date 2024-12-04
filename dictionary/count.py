# arr=[10,20,5,40,2,3,10,20,3]

# counts={num: arr.count(num) for num in arr}
# print(counts)

text="ABABCDDEFFA"

char_freeq={ch:text.count(ch) for ch in text}
print(char_freeq)

# for k,v in char_freeq.items():
#     if v==1:
#         print(k,end=" ")

non_rec=[k for k,v in char_freeq.items() if v==1]
print(non_rec)