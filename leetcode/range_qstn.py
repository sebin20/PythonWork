num = [1,3,4,5,6,9]
op = []
leng = len(num)

i = 0
while i < leng:
    j = i
    
    while j + 1 < leng and num[j] + 1 == num[j + 1]:
        j += 1

    if i == j:
        op.append(str(num[i]))
    else:
        op.append(f"{num[i]}->{num[j]}")
    
    i = j + 1

print(op)

         