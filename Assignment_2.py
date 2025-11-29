#Evens between query range using function
def print_even(a,b):
    even=[]
    for num in range(a,b+1):
        if(num%2==0):
            even.append(num)
    return even

a=int(input("Enter starting range: "))
b=int(input("Enter ending range: ")) 

result = print_even(a,b)  

print(f"total number of evens between {a} and {b} is: {len(result)}")
print(f"Even numbers between {a} and {b} are:", *result, sep=" ")

#print digits
def print_digits(N):
    digits=[]
    while(N>0):
        ld=N%10
        digits.append(ld)
        N=N//10
    return digits

N=int(input("Enter a natural number: "))
result=print_digits(N)
print(f"Digits in {N} are:", *result[::-1]) 
print(f"Total number of digits in {N} is: {len(result)}")

#count digits
def count_digit(N):
    count=0
    while(N>0):
        N%10
        count+=1
        N=N//10
    return count

N=int(input("Enter a natural number: "))
result=count_digit(N)
print(f"Total number of digits in {N} is: {result}")

#sum of digits
def sum_digit(N):
    sum=0
    while(N>0):
        ld=N%10
        sum+=ld
        N=N//10
    return sum

N=int(input("Enter a natural number: "))
result=sum_digit(N)
print(f"Total number of digits in {N} is: {result}")

def div(n):
    div=[]
    for i in range(1, n+1):
        if(i%3==0 and i%5==0):
            div.append(i)
    return div

n=int(input("Enter a natural number: "))
result=div(n)
print(*result)

#is prime
def is_prime(num):
    if num == 1 or num ==2 or num == 3:
        return True
    else:
        for i in range(2, num-1, 1):
            if num%i==0:
                return False
            else:
                return True


num=int(input("Enter a number: "))
print(is_prime(num))

#7th question
def n_():
    while(True):
        n=input("Enter: ")
        if(n.isdigit()):
            print(n)
        elif(n=="quit"):
            print("program terminated")
            break
        elif(n.isalpha() and n != "quit"):
            print("Invaild Input")

n_()

#calculator
def calculator():
    a=int(input("Enter num1: "))
    b=int(input("Enter num2: "))
    operator=input("Enter valid Operator(+,-,/,*,**,%): ")
    match operator:
        case "+":
            return a + b
        case "-":
            return a-b
        case "/":
            return a//b
        case "*":
            return a*b
        case "%":
            return a%b
        case "**":
            return a**b
        case _:
            return "invaild operator"
        

print(calculator())


        
 


  

    

