# Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:
# 3x^3 - 2x^2 + 3x - 1
# The result should be assigned to y.
# Remember that classical algebraic notation likes to omit the multiplication operator ‒ you need to use it explicitly. Note how we change data type to make sure that x is of type float.
# Keep your code clean and readable, and test it using the data we've provided, each time assigning it to the x variable (by hardcoding it). Don't be discouraged by any initial failures. Be persistent and inquisitive.

x = input("Provide value for x: ")
x = float(x) #changing x from str (input) to float we could also use x=float(input("BLAH BLAH BLAH"))
y = 3*x**3 - 2*x**2 + 3*x-1

print("y = ", y)