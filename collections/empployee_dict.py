
employee={"id":100,"name":"ram","dep":"cs" ,"age":20, "salary":25000}
# print(employee["id"])

# to print without error 
print(employee.get("salary"))
print(employee.get("depart"))


#to remove a key-value
employee.pop("dep")
print(employee)

#to get keys
employe_keys=employee.keys()        # for k in employee.keys():
print(employe_keys)                 #     print(k)


#to get values of a dict
employe_value=employee.values()                # for val in employee.values():
print(employe_value)                           # print(val)

for k,v in employee.items():
    print(k,v)
    


