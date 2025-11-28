def cal_sum(a,b):  #parameters
    sum=a+b
    return sum

a=int(input("Enter first number: "))
b=int(input("Enter second number: ")) 

result=cal_sum(a,b) #arguments
print(f"sum of {a} and {b} is: {result}")