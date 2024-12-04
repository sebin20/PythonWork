# class Operations:
#     def add(self,num1,num2):
#         print(num1+num2)
        
#     def add(self,num1,num2,num3):            error because add(2) gets replaced with add(3)
#         print(num1+num2+num3)
         
# obj=Operations()
# obj.add(10,20)


class Operations:
    def add(self,*args):
        print(sum(args))
        
obj=Operations()
obj.add(10,20)