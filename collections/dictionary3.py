employee={"eid":100,"name":"abhishek","salary":30000,"dep":"hr","exp":2}
print(employee)

# employee["conatct"]=2345678
# print(employee)

employee["exp"]=4

# if employee["exp"] > 5:
#     employee["salary"]+=10000
# else:
#     employee["salary"]+=5000
    
if employee["exp"] >5:
    employee["role"]="SDE"
    
else :
    employee["role"]="JDE"

print(employee)