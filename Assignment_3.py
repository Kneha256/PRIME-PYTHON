#find avg of el in list
"""
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

#dictionary question:
student = {
    "neha":45,
    "shreya":42,
    "kavya":38,
    "rahul":48,
    "reema":32,
    "shruti":44
}

print(type(student))
print(student) """




