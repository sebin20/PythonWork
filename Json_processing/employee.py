from json import load

f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\JSON_FILES\\employee.json")

data=load(f)

for emp in data:
    print(emp)