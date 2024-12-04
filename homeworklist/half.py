# Write a Python program to split a list into two halves.
arr = [1, 2, 3, 4, 5, 6, 7, 8]

mid_index = len(arr) // 2

first_half = arr[:mid_index]
second_half = arr[mid_index:]

print("First half:", first_half)
print("Second half:", second_half)


len()