# class GrandParent:
#     def m1(self):
#         print("Grand parent class m1")
        
# class Parent:
#     def m2(self):
#         print("parent class m2")

# class Child(Parent,GrandParent):
#     def m3(self):
#         print("Child class m3")

# child_insta=Child()

# child_insta.m3()

# child_insta.m2()

# child_insta.m1()

class GrandParent:
    def m(self): 
        print("Grand parent class m") 
        
class Parent:
    def m(self): 
        print("parent class m") 

class Child(Parent,GrandParent):
    def m3(self):
        print("Child class m3")

child_insta=Child()

child_insta.m3()

child_insta.m()