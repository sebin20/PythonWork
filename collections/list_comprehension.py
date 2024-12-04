arr=[2,3,4,5,6,7]
# squares=[]
# for num in arr:
#     square=num**2
#     squares.append(square)
# print(squares)

# squares=[ num**2  for num in arr]

# print(squares)

# cubes=[ num**3  for num in arr if num<4]

# print(cubes)

arr1=[num+1 if num > 5 else num-1 for num in arr]
print(arr1)