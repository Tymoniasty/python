#Try, Except, Finally example
x = 206
y = 0

#Divide by zero
#print()
#ZeroDivisionError: division by zero - caused by the line below:
#print(x / y)
#print()

#using a error handler for ZeroDivisionError
print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else: 
    print('something else went wrong')
finally:
    print('This is our cleanup code')
print()