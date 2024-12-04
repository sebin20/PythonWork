bracket_pairs={'(':')','{':'}','[':']','<':'>'}

symbol_stack=[]

user_input=input("Enter the string :")

top=-1

is_valid=True

for sym in user_input:
    if sym in bracket_pairs:
        top=top+1
        symbol_stack.append(sym)
    
    elif top==-1:
        is_valid=False
    
    elif sym == bracket_pairs.get(symbol_stack[top]) :
        top=top-1
        symbol_stack.pop()
        
    else :
        is_valid=False
    
if len(symbol_stack)==0 and is_valid:
    print("It is valid..")
    
else:
    print("It is invalid...")
