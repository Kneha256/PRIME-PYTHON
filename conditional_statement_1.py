#if-elif-else statement to categorize age groups
age=int(input("Enter your age: "))

if (age < 13):
    print("You are a Child")
elif(age>13 and age<=18):
    print("You are a Teenager")
else:
    print("You are an Adult")
