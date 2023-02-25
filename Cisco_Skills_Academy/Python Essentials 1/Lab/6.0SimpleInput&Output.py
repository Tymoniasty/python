# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
# The results have to be printed to the console.
# You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
# Test your code ‒ does it produce the results you expect?

variable1=float(input("Please provide number1: "))
variable2=float(input("Please provide number2: "))
print(variable1+variable2)
print(variable1-variable2)
print(variable1*variable2)
if variable1 <=0 or variable2 <=0:
    print("Can't divide by 0!\nPlease provide number higher than 0!")
else:
    print(variable1/variable2)
print("\nThat's all, folks!")