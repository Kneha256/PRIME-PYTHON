#no paramter is compulsory and can not access class or instance attributes
#stand alone functions inside a class
#class method can not access instance attributes and 1st parameter is - cls
#have a decorator - @classmethod 
#decorator make it class method and now can be accessed by object also
class Laptop:
    storage_type="ssd"

    def __init__(self, RAM, Storage):
        self.RAM=RAM
        self.storage=Storage
        
    @classmethod
    def get_storage_type(cls):   #class method but cant access another attributes
        print(f"Store type is {cls.storage_type}")
    
    @staticmethod
    def get_price(price, discount):
        final_Price=price-(discount*price/100)
        print(f"Discounted pice is {final_Price}")


    def get_info(self): #instance method
        print(f"Laptop has {self.RAM} RAM, {self.storage} of {self.storage_type}")
        
l1=Laptop("8GB", "512GB")
l1.get_price(40000,10)

