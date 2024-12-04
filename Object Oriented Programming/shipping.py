class Shipping:
    def calculate_shipping_cost(Self,weight):
        print(weight*5)
        
        
class ExpressShipping(Shipping):
    def calculate_shipping_cost(Self,weight):
        print(weight*20)
        

class StandardShipping(Shipping):
    def calculate_shipping_cost(Self,weight):
        print(weight*10)
        
exp_shp=ExpressShipping()
exp_shp.calculate_shipping_cost(10)

std_insta=StandardShipping()
std_insta.calculate_shipping_cost(10)