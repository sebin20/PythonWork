class Student:
    name:str
    age:int
    id:int
    
    def studentDefinition(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        
    def display_students(self):
        print(f"name :{self.name} age: {self.age} ID :{self.id}")
        
        
student_instance=Student()
student_instance.studentDefinition("Sebin",22,10)
student_instance.display_students()
        