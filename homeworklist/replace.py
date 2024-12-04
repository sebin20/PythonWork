#Write a Python program to replace an element in a list with another element.

arr = ["apple", "orange", "mango", "kiwi"]

for i in range(len(arr)):
    if arr[i] == "apple":
        arr[i] = "Banana"

print(arr)
