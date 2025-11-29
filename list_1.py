#list is collection of items and it is mutable and indexing starts from 0
#list can store hetrogeneous data types
#empty list marks=[] 

#slicing
marks=[23,45,67,89,54,"hello",78.9]
print(marks[-2:-5:-1])

#append - add element at the end
marks.append(100)
print(marks)

#insert (marks.insert(index,value))- add element at specific position 
marks.insert(6, "world")
print(marks)

#sort() - sort the list in ascending order
num=[2,7,4,98,65,45,99,1]
num.sort()
print(num)

#sort in decreasing order
num.sort(reverse=True)
print(num)

#revere() - reverse the list
num.reverse()
print(num)

#index() - returns the index of first occurence of the value
print(num.index(45))
