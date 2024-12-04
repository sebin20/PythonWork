#Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

names=["abhishek","ajay","arun","appu","ram"]
age=[21,22,34,45,28]

dictionary_comp={names[i]:age[i] for i in range(len(age))}
print(dictionary_comp)
