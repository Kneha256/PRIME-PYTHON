#muliple inheritence - a class is derived from more than one parent class

class teacher:
    def __init__(self, salary):
        self.salary=salary

class student:
    def __init__(self, cgpa):
        self.cgpa=cgpa

class Teacher_assistant(teacher, student):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        student.__init__(self, cgpa)
        self.name=name

TA1=Teacher_assistant(56000, 7.5, "sneha")

print(TA1.name, TA1.salary, TA1.cgpa)