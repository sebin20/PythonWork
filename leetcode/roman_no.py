roman = {"I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000}
user_input = input("Enter Roman No : ").upper()
integer = 0
for i in range(len(user_input)):
    if i < len(user_input) - 1 and roman[user_input[i]] < roman[user_input[i + 1]]:
        integer -= roman[user_input[i]]
    else:
        integer += roman[user_input[i]]
print("Integer value:", integer)