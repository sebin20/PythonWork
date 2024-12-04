strs = ["dog","racecar","car"]
first_word = strs[0]
longst = ""

for j in range(1, len(first_word) + 1):
    all_match = True
    for i in range(1, len(strs)):
        if strs[i][0:j] != first_word[0:j]:
            all_match = False
            break

    if all_match:
        longst = first_word[0:j]
    else:
        break

if longst == "":
    print("\"\"")
else:
    print(longst)






















# strs=["flower","flowe","floweight"]
# #      012345    len=6

# first_word=strs[0]
# count=0
# longst=""

# # 1 2 3 4 5 6 

# for j in range(1,len(first_word)+1):
#     if first_word[0:j] == strs[1][0:j] and first_word[0:j] == strs[2][0:j]:
#         longst=first_word[0:j]
        
#     else:
#         break
        
# if longst=="":
#     print(" \"\" ")
# else:
#     print(longst)
        
    
        