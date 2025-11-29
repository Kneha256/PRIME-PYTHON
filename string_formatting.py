#string is a sequence of characters and is immutable
#slicing
str="hello"
print(str[0:4]) #or str[:4]
print(str[len(str)::-1])


#normal formating
a=8
b=6

#print("sum of {} and {} is {}".format(a,b,a+b))

#index based formating
print("sum of {1} and {0} is {2}".format(a, b, a+b))  

#value based formating
print("value of {a} and {b}".format(a=3,b=5))

#f-string formatting - literal string interpolation
print(f"sum of {a} and {b} is {a+b}")


