class Laptop:
    storage_type="ssd"

    def __init__(self, RAM, Storage):
        self.RAM=RAM
        self.storage=Storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM, {self.storage} of {self.storage_type}")

l1=Laptop("16GB", "512GB")
l1=Laptop("16GB", "512GB")
l1.get_info()
