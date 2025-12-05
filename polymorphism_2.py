#same method name in different class 
#same method name with different parameters
#complie-time polymorphism

class emp:
    def get_designation(self):
        print("designation=employee")

class Teacher:
    def get_designation(self):
        print("desigrantion = teacher")

t1=Teacher()
t1.get_designation()