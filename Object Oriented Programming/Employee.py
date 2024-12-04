class Employee:
    id:int
    name:str
    dep: str
    salary:int
    
    def set_employee(self,id,name,dep,salary):
        self.name=name
        self.id=id
        self.dep=dep
        self.salary=salary
        
        
    def display_Names(self):
        print(f" name is :{self.name} \n id is :{self.id} \n dep is :{self.dep} \n salary is :{self.salary}")
        
employe=Employee()
employe.set_employee(10,"Sebin","CSE",20000)
employe.display_Names()