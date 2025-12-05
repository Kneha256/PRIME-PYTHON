#resusing attributes and methods from (parent) base class to (child)derived class
class emp:     #parent class
    start_time="10am"
    end_time="5pm"

    def change_end_time(self, new_end_time):
        self.end_time=new_end_time

class teacher(emp):     #derived class
    def __init__(self, name, subject):
        self.name=name
        self.subject=subject

t1=teacher("shreya", "computer")
t1.change_end_time("8pm")
print(t1.name, t1.subject, t1.end_time)    #accessing emp class attributes also