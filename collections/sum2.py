lst=[2,3,4,5]

total=0
for i in range(len(lst)):
    total+=lst[i]
# print(total)

for i in range(len(lst)):
    print(total-lst[i],end=" ")