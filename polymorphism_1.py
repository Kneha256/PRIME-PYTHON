#poly=  many, morphism - types/forms
#overriding - redefining a parent class inside a child class

class emp:
    def get_designation(self):
        print("designation=employee")

class Teacher(emp):
    def get_designation(self):
        print("desigrantion = teacher")

t1=Teacher()
t1.get_designation()