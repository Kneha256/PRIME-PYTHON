info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]


#question 1: Print all the unique subjects from the info list.
courses_set = set()
for el in info:
    courses_set.add(el[1])

print(f"All the unique subjects are: {list(courses_set)}")

#question 2 - list students enrolled in english
list = []
for name,course in info:
    if(course=="English"):
        list.append(name)

print(f"Students having English as subject are: {list}")

#question 3 - create a dictonary with sudents as keys and set of courses
students_dict={}

for name, course in info:
    if name not in students_dict:
        students_dict.update({name: set()})
        students_dict[name].add(course)
    else:
        students_dict[name].add(course)

print(f"Students with their courses: {students_dict}")

