from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelarate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    

class GT(Bike):
    
    def start(self):
        print("Start GT")
        
        
    def accelarate(self):
        print("Accelerate gt")
        
    def stop(self):
        print("GT Stoped")
        
        
gt=GT()

gt.start()

gt.accelarate()

gt.stop()