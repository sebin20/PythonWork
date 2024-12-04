#Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.

first_dict={1:10,2:20,3:-30,4:-4,5:55}
second_dict={k:abs(v)for k,v in first_dict.items() } 
print(second_dict)