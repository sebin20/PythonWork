class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @property
    def get_name(self):
        
        print(self.name)
        
    @property
    def get_age(self):
        print(self.age)
        
person=Person("hari",34)

person.get_name

person.get_age