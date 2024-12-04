# arr=[10,20,30,40,50,60]
# odd_positions_elements=[arr[i] for i in range(0,len(arr)) if i%2!=0]
#                       #[num for index,num in enumerate(arr)  if index%2!=0]

# for i in range(1,len(arr),2) :
#     elements=odd_positions_elements.pop()
#     arr[i]=elements
# print(arr)

arr = [10, 20, 30, 40, 50, 60]

odd_positions_elements = [arr[i] for i in range(1, len(arr), 2)]

odd_positions_elements.reverse()

for i in range(len(odd_positions_elements)):
    arr[1 + 2 * i] = odd_positions_elements[i]  # Update 2nd, 4th, 6th positions

print(arr)
