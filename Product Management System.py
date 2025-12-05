class Product:
    count=0
    def __init__(self, name, price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):
        print(f"price of {self.name} is {self.price} rupees")
    
    @classmethod
    def get_count(cls):
        print(f"total number of products are {cls.count}")

    @staticmethod
    def get_discount(price, discount_percent):
        discounted_price=price-(discount_percent*price/100)
        print(f"total discounted price = {discounted_price}")


p1 = Product("phone",20000)
p2 = Product("Laptop",76000)
p2.get_info()
p2.get_count()
p2.get_discount(p2.price, 10)



