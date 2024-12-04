#Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary.
fruits=["apple","orange","mangoes","blue berry","jackfruit"]
price=[100,120,150,500,300]

fruits_dict={fruits[i]:price[i]  for i in range(len(price))}
print(fruits_dict)

