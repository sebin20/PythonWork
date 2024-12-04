# st=set()
# sets={"red","blue","grey","red"}
# # print(type(st))
# sets.add("yellow")
# print(sets)


# arr=[10,20,30,40,20,40,50]
# # st=set(arr)
# # print(st)
# st=set()
# for num in arr:
#     st.add(num)
# print(st)


# set1={1,2,3,4,5,99,77}
# set2={1,2,3,4,5,6,7,8}
# intersection_set=set1.intersection(set2)
# print(intersection_set)

# union_set=set1.union(set2)
# print(union_set)

# diff=set1.difference(set2)
# print(diff)

# set1.remove(5)
# print(set1)

# print(set1.issubset(set2))
# print(set2.issuperset(set1))

# symmetric_difference=(AUB)-(A^B)

# symm=set1.symmetric_difference(set2)
# print(symm)

# set1.update(set2)
# print(set1)

text="this is a test to remove duplicate words this test is simple"
text2="this simple test remove duplicate words"
wordst=text.split(" ")
wordst2=text2.split(" ")

set1=set(wordst)
set2=set(wordst2)
# print(set1)

# wordss=" ".join(set6)
# print(wordss)

print(set1.issuperset(set2))
