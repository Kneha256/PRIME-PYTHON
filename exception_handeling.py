#it avoid distrupt code execution
#manageale errors are called exception and called as exception handeling
#try - codes which mzy/mzy not throw error
#except - inside except we write exception code if try throw any error
#else - if try not throw error then what should be output
#finally - irrespective of error occur or not but we want to print this 

try:
    num=int(input("Enter a number: "))
    ans=10/num

except ZeroDivisionError:
    print("zero is not allowed..")

except ValueError:
    print("please enter a valid number!")

else:
    print(f"output is : {ans}")

finally:
    print("this is end of program")
