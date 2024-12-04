student_data= { "hari":[20,20,20],"Akku":[10,20,20],"Appu":[10,10,10],"Babu":[40,40,40]}

user_input=int(input("enter index :"))

for index,element in enumerate(student_data):

    if index==user_input:
        marks=student_data.get(element)
        avg=sum(marks)/len(marks)
        
print(avg)


#To print name with avg mark

# for index,element in enumerate(student_data):
#     marks=student_data.get(element)
#     avg=sum(marks)/len(marks)
#     print(f" {element}  : {avg}")
        
        
student_dict={k:sum(v)/len(v)  for k,v in student_data.items() }
print(student_dict)