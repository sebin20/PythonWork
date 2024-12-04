f1=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\all_names.txt","r")
f2=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\failed.txt","r")

all_students=[]    # or all_students=set()
fail_students=[]   # or fail_students=set()

for name in f1:
    name=name.rstrip("\n")     
    all_students.append(name)   #all_students.add(name
    
for name in f2:
    name=name.rstrip("\n")
    fail_students.append(name)
    
    
pass_students=set(all_students).difference(set(fail_students))
print(pass_students)