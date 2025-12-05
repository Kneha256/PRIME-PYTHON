class Laptop:
    storage_type="ssd"

    def __init__(self, RAM, Storage):
        self.RAM=RAM
        self.storage=Storage

    def get_storage_type(cls):   #class method but cant access another attributes
        print(f"Store type is {cls.storage_type}")

    def get_info(self): #instance method
        print(f"Laptop has {self.RAM} RAM, {self.storage} of {self.storage_type}")

l1=Laptop("16GB", "512GB")
l1=Laptop("16GB", "512GB")
l1.get_info()
l1.get_storage_type()
