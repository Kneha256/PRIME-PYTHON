num=int(input("Enter a number:"))

i=1
while(i<=10):
    if(i%3==0):
        i+=1
        #continue
    print(f"{num} * {i} = {num*i}")   
    i+=1
