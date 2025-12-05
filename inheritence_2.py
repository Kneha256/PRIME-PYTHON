#single level - one parents class & one base class
class emp:
    s_time="9am"
    e_time="5pm"

class staff(emp):
    def __init__(self, name, department):
        self.name=name
        self.department=department

s1=staff("Arjun Prasad", "Academic")
s2=staff("Reema Ritu", "Examination")

print(f"{s2.name}, {s2.department} department, timing {s2.s_time} to {s2.e_time}")