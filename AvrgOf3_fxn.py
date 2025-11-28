def calc_avg(a,b,c=3):  #default parameter
    avg=(a+b+c)//3
    return avg

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))       
c=int(input("Enter third number: "))
result=calc_avg(a,b,c)
print(f"Average of {a},{b} and {c} is: {result}")