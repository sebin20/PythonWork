arr=[10,20,5,40,2,3]
even_squares={num:num**2 for num in arr if num%2==0}
odd_cubes={num:num**3  for num in arr if num%2!=0}
print(even_squares)
print(odd_cubes)