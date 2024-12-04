class BankAccount:
    
    name:str
    
    mpin:int
    
    acc_type:str
    
    balance:int
    
    def __init__(self,name,mpin,accc_type,balance):
        
        self.name=name
        
        self.__mpin=mpin  #( __ used to convert publoic to private)
        
        self.acc_type=accc_type
        
        self.__balance=balance  # private
        
    def get_balance(self):
        
        print(self.__balance)
        
        
    def __str__(self):
        
        return str(self.__mpin)
        
bank=BankAccount("Abhishek",2345,"savings",25000)

print(bank.acc_type)

bank.get_balance()
        
print(bank)