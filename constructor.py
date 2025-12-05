#initialize an object and automatically get called while an object is created for one tym only
#self parameter says that it is storing the current instance(object) of the class
#default constructor(self parameter only) and parametrized constructor(more parameters including self)
#in python there will be only one constructor inside a class unlike java and cpp
# class student:
#     def __init__(self, name, age, course):
#         print("constructor called....")
#         self.name="name"
#         self.age= age
#         self.course="course"
    
#     def get_age(self):    #
#         return self.age

# s1=student("neha", 22, "CSE")
# print(s1.name, s1.age, s1.course)
# print(s1.get_age())


#attributes - class attributes and instance(object) attributes
#class attributes are common for all the objects. ex - college name
#instance attributes are specific for specific instance. ex name

class Student:              #class attributes
    college_name="Lovely professional University"

    def __init__(self, name, reg):
        self.name=name
        self.reg=reg

s1=Student("neha",12216645)
print(Student.college_name,s1.name,s1.reg)

#class attribute can be invocked by both class name or object name 
#instance attributes can be invoked by object name only
print(s1.college_name,s1.name,s1.reg)
print(Student.college_name,s1.name,s1.reg)

#instance attribute is having higher priority 