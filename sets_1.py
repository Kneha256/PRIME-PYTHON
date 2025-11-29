#set is immutable and unordered collection of unique elements
#empty set
s=set()
s.add(5) #adding elements to set
s.add(10)
s.add("neha")
s.add('d')
s.remove("neha") #removes specific element
print(s)
# print(s.pop())  #random element will be removed
# print(s)

# s.clear()   #removes all elements from set
# print(s)

#union of two sets
s1={1,2,10,4}
print(s.union(s1)) #will return union of two sets

#intersection of two sets
print(s.intersection(s1)) #will return common elements in both sets

