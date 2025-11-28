#converting one datatype into anothertype
#1-imploicit type conversion done by python automatically
a=2
b=3.5
print(type(a+b))

a=4
b=2
print(type(a/b))
print(type(a//b))

#2-explicit type conversion done by user
a=4
b=2
div=int(a/b)
print(div,type(div))

x="123"
y=int(x)
print(y,type(y))