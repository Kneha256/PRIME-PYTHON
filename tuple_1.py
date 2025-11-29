#tuple with single element
tup1 = (5,)

#empty tuple
tup2 = ()


#tuple is immutable
tup = (3,5,6,2,1,3,2,2)

sum=0
for i in tup:
    sum+=i
print(f"sum of elements in tuple is: {sum}")

#sliceing
print(tup[1:5])

#index() - returns the index of first occurence of the value
print(tup.index(6))

#count() - returns the count of occurences of the value
print(tup.count(2))