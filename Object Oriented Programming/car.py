class Car:
    
    name:str
    
    brand:str 
    
    fuel_type:str 
    
    def __init__(self,name,brand,fuel_type):
        
        self.name=name
        
        self.brand=brand
        
        self.fuel_type=fuel_type
        
    def display(self):
        print(self.name,self.brand,self.fuel_type)
        
    def __str__(self):
        return self.name
    

car_instance=Car("XM","BMW","Hybrid")

car_instance.display()

print(car_instance)


    