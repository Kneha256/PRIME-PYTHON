#file io is performed to read or perform some operation from files having different types(extension)
#first step is always to open a file(load) with appropriate mode
#last step is to closing a file is always important
f=open("sample.txt","r")
data=f.read()           #- read whole data
data=f.readline()       #  - to raed a single line
print(data)
print(type(data))
#pointer concept while reading or writing a file
#write operation will overwrite with new data
f=open("sample.txt", "w")      
f.write("I want to get placed \nin a good company at good package")
f.close()

f=open("sample.txt", "a")
f.write("\ni an studying everything,\nthat can help me to get placed")
f.close()

f=open("sample.txt","r")   
data=f.read()
print(data)

#modes
#by default file always open in "r" read mode
#write "w" mode first truncate \ overwrite everything then add new data in it
#append "a" mode add new data at the end of the file
#"x" mode help to create new file and then add something in it
# f1=open("sample2.txt", "x")
# f1.write("some random text in it")
# f1.close()
#"+" allow both read and write
#"t" allow to open a file in text format
#"b" allow to open in binary format
#"r+" - start overwriting from beginning  
#"a+" - point at end of the data and any thing will perform from end
#"w+" - completely truncate and again point at stating of the file
f=open("sample.txt", "w+")
f.write("123")
data=f.read()
print(data)

# "with" keyword to perform io file operation
# no need to close the file
with open("sample.txt", "r+") as f:
    f.write("t")
    print(f.read())


#deleting a file
#use os module - a built in module in python stand for operating system
#os module is use when we want to interact with os of system in python
#os.remove() to delete a file from system
import os
os.remove("sample2.txt")