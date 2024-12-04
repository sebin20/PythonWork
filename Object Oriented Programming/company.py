class Person:
    name:str
    age:int
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
         
    def person_info(self):
        print(f" name is : {self.name} , age is : {self.age}")
        
        
class Employee:
    emp_id:int
    salary:int
    
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
        
    def employee_info(self):
        print(f"Employee details , emp_id : {self.emp_id} , salary : {self.salary}")
        
        
class Manager(Person,Employee):
    depart:str
    def __init__(self,name,age,emp_id,salary,dep):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.dep=dep
        
    def display_manager_info(self):
        
        self.person_info()
        self.employee_info()
        print(self.dep)
        

manager=Manager("Rahul",23,105,25000,"Manager")
manager.display_manager_info()