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
