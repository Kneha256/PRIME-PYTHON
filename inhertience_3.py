#multi level inheritence - a class is derived from another class
class emp:
    s_time="9am"
    e_time="5pm"

class staff(emp):
    def __init__(self,department):
        self.department=department


#super() key word can be used to call constructor of parent class
class Accounts(staff):      
    def __init__(self, salary, department):
        super().__init__(department)
        self.salary=salary

s1=Accounts(25000, "Academic")
s2=Accounts(45000, "Examination")

print(s1.salary, s1.e_time, s1.department)