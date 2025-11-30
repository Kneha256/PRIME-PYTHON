str = input("Enter a string: ")

count=0
i=0
while(i<len(str)):
    if(str[i] == " "):
        count+=1
        i+=1
    else:
        i+=1

print(f"Number of spaces in Input string are: {count}")


#methos 2
count=0
for i,el in enumerate(str):
    if(i<=len(str)-1 and el==" "):
        count+=1

print(count)
