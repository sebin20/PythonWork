#Write a Python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension.
fruits=["apple","orange","mangoes","blue berry","jackfruit"]
price=[20,40,150,500,300]

fruits_dict={fruits[i]:price[i]  for i in range(len(price))}

fruits_dict_filtered={k:v for k,v in fruits_dict.items() if v>50}
print(fruits_dict_filtered)