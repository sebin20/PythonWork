list1=["apple","mango","Onion","potato","Orange"]
lst2=[100,200,300]

dict_fruit={}

# j=1

# if len(list1)==len(lst2):
#     for i in range(len(list1)):
#         dict_fruit[list1[i]]=lst2[i]
        
# elif len(list1)>len(lst2):
#     for i in range(len(lst2)):
#         dict_fruit[list1[i]]=lst2[i]
        
#     for i in range(len(lst2),len(list1)):
#         dict_fruit[list1[i]]=j
#         j+=1

# print(dict_fruit)




for i in range(len(lst2)):
    list_one_elements=list1[i]
    list_two_elements=lst2[i]
    
    dict_fruit[list_one_elements]=list_two_elements

balance_elemnts=list1[len(lst2):]

for index,element in enumerate(balance_elemnts):
    dict_fruit[element]=index+1

print(dict_fruit)    