lst=[ 1,
    2,
    [10,29],
    [1,2,5,[10,3]],
    100]

list_objects=[]
for item in lst:
    if isinstance(item,list):
        list_objects.append(item)

print(max(list_objects,key=len))
# print(max(list_objects,key=lambda it:len(it)))