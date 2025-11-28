num=int(input("Enter a number:"))

i=1
while(i<=10):
    if(i%6==0):
        break
    print(f"{num} * {i} = {num*i}")
    i+=1
