#str-palindrome
str=input("Enter a string: ")

str_rev=str[::-1]

if str == str_rev:
    print("It is palindrome")
else:
    print("Not a palindrome")  


#find avg of el in list
list=[23,45,67,89,54,78.9]

sum=0
n=len(list)
for i in list:
    sum+=i

avg=sum/n
print(f"Average of elements in list is: {avg}")


#take 2 list as input merge them and sort
def merg_sort(L1,L2):
    result=[]
    for i in L1:
        result.append(i)
    for y in L2:
        result.append(y)
    result.sort()
    return result

L1=list(map(int,input("enter num:").split()))
L2=list(map(int,input("Enter nums:").split()))

Sorted_List=merg_sort(L1,L2)
print(Sorted_List)



#odd tuple and even tuple
t=(1,2,3,4,5,6,7,8,9,10)
t_list=list(t)

Even=[]
Odd=[]
for el in t_list:
    if el%2==0:
        Even.append(el)
    else:
        Odd.append(el)

print(tuple(Even))
print(tuple(Odd)) 



#return duplicates
list=list(map(int,input("Enter numbers : ").split()))

seen=set()
duplicate=set()

for el in list:
    if el in seen:
        duplicate.add(el)
    else:
        seen.add(el)

print(duplicate) 


#dictionary question - student management
student = {}
def std(action_key):
    match(action_key):
        case "A":
            stu=input("Enter Student name: ")
            marks=int(input("Enter marks : "))
            student[stu]=marks
            print(student)
        case "B":
            stu=input("enter student name: ")
            if stu in student.keys():
                marks=int(input("Enter marks: "))
                student.update({stu:marks})
                print(f"Updated marks:{student}")
            else:
                marks=int(input("Student not found! Enter marks: "))
                student.update({stu:marks})
                print(f"Updated marks:{student}")
        case "C":
            stu=input("Enter student name : ")
            if stu in student.keys():
                print(f"{stu}'s data exist")
            else:
                print(f"No data found related to {stu}")
        case "D":
            for name, marks in student.items():
                print(f"name : {name}, marks : {marks}")
        case _: print ("default input")

print("Enter A for adding new student details.\nEnter B for updating marks of a student")
print("Enter C to seach a student.\nEnter D for printing all students data along with marks")
print("Type stop to exit")
while(True):
    action_key=input("Enter you Action_Key: ").upper()
    if(action_key == "STOP"):
        break
    std(action_key)



#common element in two list
def check_common(L1, L2):
    for el in L1:
        if el in L2:
            print(f"Share common element")
            break
print("share no common elements")


L1=list(map(int, input("Enter list items with space: ").split()))
L2=list(map(int, input("Enter list items with space: ").split()))

check_common(L1,L2)



#dictionary maping question 

words =["apple","banana","kiwi","cherry","mango"]
dic={}
for el in words:
    dic[el]=(len(el))

print(dic)