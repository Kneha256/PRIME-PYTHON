def calc_tax(salary):
    if(salary<30000):
        return salary*0.10
    elif(salary>=30000 or salary<70000):
        return salary*0.15
    elif(salary>=70000):
        return salary*0.25
    
salary=int(input("Enter your salary: "))
#result=calc_tax(salary)
print(f"Your tax amount for salary of amount {salary} is: {calc_tax(salary)} rupees")