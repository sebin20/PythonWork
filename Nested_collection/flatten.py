arr=[[10,20],
     [20,30],
     [30,40],
     [40,50]]
result=[]
for ls in arr:
    for num in ls:
        result.append(num)
print(result)


# OR

result2=[]
for ls in arr:
    result2.extend(ls)
print(result2)

#or

ls=[num for ar in arr for num in ar]
print(ls)
