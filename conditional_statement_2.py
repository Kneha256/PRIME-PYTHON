#Nested if-else statement for user authentication
user_name=input("Enter user name:")
password=input("Enter your password:")

if(user_name=="admin"):
    if(password=="Pass"):
        print("Access Granted")
    else:
        print("Wrong Password")
else:
    print("Wrong User Name")
