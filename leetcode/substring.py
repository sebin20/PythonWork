def is_subsequence(main_string, substring):
    sub_index = 0  
    main_leng = len(main_string)
    sub_length = len(substring)
    
    for char in main_string:
        if sub_index < sub_length and char == substring[sub_index]:
            sub_index += 1
        if sub_index == sub_length:
            return True
    
    return False
main_string = input("Enter the main string :")
substring = input("Enter the sub string :")

result = is_subsequence(main_string, substring)
print(result)
